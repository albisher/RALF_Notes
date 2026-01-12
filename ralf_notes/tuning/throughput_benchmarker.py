import time
import random
import logging
from typing import List, Optional, Any
from ollama import Client
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

from .models import ThroughputBenchmarkResults, ThroughputTest, SystemProfile, LatencyBenchmarkResults, BenchmarkConfig
from .sample_generator import SampleCodeGenerator

logger = logging.getLogger(__name__)

class ThroughputBenchmarker:
    """
    Box: Throughput Benchmarker

    Input: SystemProfile, LatencyBenchmarkResults
    Output: ThroughputBenchmarkResults
    Responsibility: Determine optimal concurrency and delay
    """

    def __init__(
        self,
        ollama_client: Client,
        sample_generator: SampleCodeGenerator
    ):
        self.client = ollama_client
        self.sample_generator = sample_generator

    def benchmark_throughput(
        self,
        profile: SystemProfile,
        latency_results: LatencyBenchmarkResults, # Not directly used but kept for signature
        model_name: str,
        num_ctx: int,
        benchmark_config: BenchmarkConfig,
        progress: Any = None, # ADD progress object
        main_task_id: Any = None # ADD main task ID
    ) -> ThroughputBenchmarkResults:
        """
        Benchmark throughput with different concurrency levels.

        Args:
            profile: System profile for constraints.
            latency_results: Latency benchmark results to inform delays/timeouts.
            model_name: Model to test.
            num_ctx: Context size to use for benchmarking.
            benchmark_config: The benchmark configuration object.
            progress: Rich ProgressManager object for progress updates.
            main_task_id: ID of the main progress task.

        Returns:
            Optimal concurrency and delay settings.
        """
        logger.info("Starting throughput benchmark for model: %s, context: %d, intensity: %s",
                    model_name, num_ctx, benchmark_config.intensity)
        
        if benchmark_config.intensity == "quick":
            delays = [0, 0.1]
            parallel_levels = [1, min(2, profile.cpu_threads)]
            requests_per_test = 2
        elif benchmark_config.intensity == "full":
            delays = [0, 0.1, 0.2, 0.5]
            parallel_levels = [1, 2, min(4, profile.cpu_threads // 2), profile.cpu_threads]
            requests_per_test = 5
        else: # normal
            delays = [0, 0.1, 0.2]
            parallel_levels = [1, min(2, profile.cpu_threads)]
            requests_per_test = 3

        seq_results = self._test_sequential(
            model_name,
            num_ctx,
            delays=delays,
            requests_to_make=requests_per_test,
            timeout=benchmark_config.request_timeout_seconds,
            progress=progress, # Pass progress
            main_task_id=main_task_id # Pass main task ID
        )
        logger.debug("Sequential throughput tests completed.")
        if progress and main_task_id is not None:
            progress.update(main_task_id, advance=len(delays) * requests_per_test)


        parallel_results = []
        if profile.cpu_threads >= 1: # Even 1 thread can do parallel if tasks are IO bound
            parallel_results = self._test_parallel(
                model_name,
                num_ctx,
                levels=parallel_levels,
                requests_to_make=requests_per_test * 2, # More requests for parallel tests
                timeout=benchmark_config.request_timeout_seconds,
                progress=progress, # Pass progress
                main_task_id=main_task_id # Pass main task ID
            )
            logger.debug("Parallel throughput tests completed.")
            if progress and main_task_id is not None:
                progress.update(main_task_id, advance=len(parallel_levels) * requests_per_test * 2)
        else:
            logger.info("Skipping parallel throughput tests due to insufficient CPU threads (%d)", profile.cpu_threads)

        all_results = seq_results + parallel_results
        
        if not all_results:
            logger.warning("No throughput test results found. Returning default.")
            return ThroughputBenchmarkResults(
                optimal_parallel_requests=1,
                optimal_delay_seconds=0.0,
                max_throughput_fps=0.0,
                recommended_batch_size=10,
                recommended_batch_delay=0.0
            )

        best = max(all_results, key=lambda r: r.throughput_fps)
        logger.info("Optimal throughput found: parallel=%d, delay=%.2f, throughput=%.2f fps",
                    best.parallel, best.delay, best.throughput_fps)

        return ThroughputBenchmarkResults(
            optimal_parallel_requests=best.parallel,
            optimal_delay_seconds=best.delay,
            max_throughput_fps=best.throughput_fps,
            recommended_batch_size=self._calculate_batch_size(best, profile),
            recommended_batch_delay=self._calculate_batch_delay(best)
        )

    def _test_sequential(
        self,
        model_name: str,
        num_ctx: int,
        delays: List[float],
        requests_to_make: int,
        timeout: int,
        progress: Any = None, # ADD progress object
        main_task_id: Any = None # ADD main task ID
    ) -> List[ThroughputTest]:
        """
        Test sequential processing with different delays using actual LLM calls.
        """
        results = []
        sample_code = self.sample_generator.generate_long_sample(max_length=num_ctx // 2) # Use half context size for content
        
        if progress and main_task_id is not None:
            seq_task_id = progress.add_task(f"[cyan]Sequential Tests ({model_name})...", total=len(delays) * requests_to_make, parent=main_task_id)

        for delay in delays:
            logger.debug("Testing sequential throughput with delay: %.2f seconds", delay)
            if progress and seq_task_id is not None:
                progress.update(seq_task_id, description=f"[cyan]Sequential (delay: {delay:.2f}s)")
            start = time.time()
            successful_requests = 0

            for i in range(requests_to_make):
                try:
                    self.client.generate(
                        model=model_name,
                        system="Generate a very short summary.",
                        prompt=f"Code:\n{sample_code}",
                        options={"num_ctx": num_ctx, "temperature": 0.1, "timeout": timeout}
                    )
                    successful_requests += 1
                    logger.debug("Sequential request %d successful.", i + 1)
                except Exception as e:
                    logger.warning("Sequential request %d failed: %s", i + 1, e)
                finally:
                    if progress and seq_task_id is not None:
                        progress.update(seq_task_id, advance=1)
                    
                if delay > 0 and i < requests_to_make - 1:
                    time.sleep(delay)

            duration = time.time() - start
            throughput = successful_requests / duration if duration > 0 else 0

            results.append(ThroughputTest(
                parallel=1,
                delay=delay,
                throughput_fps=throughput,
                total_time=duration,
                successful_requests=successful_requests
            ))
            logger.debug("Sequential test (delay=%.2f) completed. Throughput: %.2f fps", delay, throughput)

        return results

    def _test_parallel(
        self,
        model_name: str,
        num_ctx: int,
        levels: List[int],
        requests_to_make: int,
        timeout: int,
        progress: Any = None, # ADD progress object
        main_task_id: Any = None # ADD main task ID
    ) -> List[ThroughputTest]:
        """
        Test parallel processing at different concurrency levels using actual LLM calls.
        """
        results = []
        sample_code = self.sample_generator.generate_long_sample(max_length=num_ctx // 2) # Use half context size for content

        if progress and main_task_id is not None:
            parallel_task_id = progress.add_task(f"[cyan]Parallel Tests ({model_name})...", total=len(levels) * requests_to_make, parent=main_task_id)

        for parallel_count in levels:
            logger.debug("Testing parallel throughput with %d workers", parallel_count)
            if progress and parallel_task_id is not None:
                progress.update(parallel_task_id, description=f"[cyan]Parallel (workers: {parallel_count})")
            start = time.time()
            successful_requests = 0

            def make_llm_call():
                try:
                    self.client.generate(
                        model=model_name,
                        system="Generate a very short summary.",
                        prompt=f"Code:\n{sample_code}",
                        options={"num_ctx": num_ctx, "temperature": 0.1, "timeout": timeout}
                    )
                    return True
                except Exception as e:
                    logger.warning("Parallel LLM call failed: %s", e)
                    return False

            with ThreadPoolExecutor(max_workers=parallel_count) as executor:
                futures = [executor.submit(make_llm_call) for _ in range(requests_to_make)]
                for future in futures:
                    if future.result():
                        successful_requests += 1
                    if progress and parallel_task_id is not None:
                        progress.update(parallel_task_id, advance=1)

            duration = time.time() - start
            throughput = successful_requests / duration if duration > 0 else 0

            results.append(ThroughputTest(
                parallel=parallel_count,
                delay=0, # Delay is handled by individual LLM calls, not between batches here
                throughput_fps=throughput,
                total_time=duration,
                successful_requests=successful_requests
            ))
            logger.debug("Parallel test (workers=%d) completed. Throughput: %.2f fps", parallel_count, throughput)

        return results

    def _calculate_batch_size(
        self,
        best: ThroughputTest,
        profile: SystemProfile
    ) -> int:
        """
        Calculate recommended batch size based on optimal throughput test.
        """
        # Simplified for now. A more complex algorithm would consider
        # model latency, system memory, and expected queueing.
        base_size = 10
        if best.parallel > 1:
            base_size = int(best.parallel * 2.5) # Scale with parallelism

        # Memory factor based on available RAM (adjust if needed)
        memory_factor = min(2.0, profile.available_ram_gb / 8.0) # Assume 8GB is baseline

        recommended_batch_size = int(base_size * memory_factor)
        logger.debug("Calculated recommended batch size: %d (based on parallel=%d, memory_factor=%.2f)",
                     recommended_batch_size, best.parallel, memory_factor)
        return recommended_batch_size

    def _calculate_batch_delay(self, best: ThroughputTest) -> float:
        """
        Calculate recommended batch delay based on optimal throughput test.
        """
        # For simplicity, if best throughput was sequential with a delay, use that.
        # Otherwise, if parallel, a small delay might still be beneficial for stability.
        recommended_delay = best.delay
        if best.parallel > 1 and recommended_delay == 0:
            recommended_delay = 0.05 # Small default delay for parallel to prevent overwhelming

        logger.debug("Calculated recommended batch delay: %.2f seconds", recommended_delay)
        return recommended_delay



