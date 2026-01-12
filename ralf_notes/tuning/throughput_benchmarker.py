import time
import random
from typing import List
from ollama import Client
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

from .models import ThroughputBenchmarkResults, ThroughputTest, SystemProfile, LatencyBenchmarkResults
from .sample_generator import SampleCodeGenerator

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
        latency_results: LatencyBenchmarkResults,
        model_name: str,
        num_ctx: int,
        benchmark_config: 'BenchmarkConfig'
    ) -> ThroughputBenchmarkResults:
        """
        Benchmark throughput with different concurrency levels.

        Args:
            profile: System profile for constraints.
            latency_results: Latency benchmark results to inform delays/timeouts.
            model_name: Model to test.
            num_ctx: Context size to use for benchmarking.
            benchmark_config: The benchmark configuration object.

        Returns:
            Optimal concurrency and delay settings.
        """
        if benchmark_config.intensity == "quick":
            delays = [0, 1.0]
            parallel_levels = [2, min(4, profile.cpu_threads)]
        elif benchmark_config.intensity == "full":
            delays = [0, 0.2, 0.5, 1.0, 2.0]
            parallel_levels = [2, 4, min(8, profile.cpu_threads // 2), profile.cpu_threads]
        else: # normal
            delays = [0, 0.5, 1.0]
            parallel_levels = [2, min(4, profile.cpu_threads)]

        seq_results = self._test_sequential(model_name, num_ctx, delays=delays)

        parallel_results = []
        if profile.cpu_threads >= 2:
            parallel_results = self._test_parallel(model_name, num_ctx, parallel_levels)

        all_results = seq_results + parallel_results
        
        if not all_results:
            return ThroughputBenchmarkResults(
                optimal_parallel_requests=1,
                optimal_delay_seconds=0.0,
                max_throughput_fps=0.0,
                recommended_batch_size=10,
                recommended_batch_delay=0.0
            )

        best = max(all_results, key=lambda r: r.throughput_fps)

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
        delays: List[float]
    ) -> List[ThroughputTest]:
        """
        Test sequential processing with different delays.
        
        Args:
            model_name: Model to test.
            num_ctx: Context size to use.
            delays: List of delays in seconds to test.
            
        Returns:
            List of ThroughputTest results for sequential processing.
        """
        results = []
        sample_code = self.sample_generator.generate_sample()

        for delay in delays:
            start = time.time()
            requests_to_make = 3 # Reduced requests for quicker simulation

            for i in range(requests_to_make):
                try:
                    # Simulate LLM call
                    simulated_latency = random.uniform(500, 2000) + (num_ctx / 100)
                    time.sleep(simulated_latency / 1000.0)

                except Exception as e:
                    print(f"Error during sequential throughput test: {e}")
                    
                if delay > 0 and i < requests_to_make - 1:
                    time.sleep(delay)

            duration = time.time() - start
            throughput = requests_to_make / duration if duration > 0 else 0

            results.append(ThroughputTest(
                parallel=1,
                delay=delay,
                throughput_fps=throughput,
                total_time=duration
            ))

        return results

    def _test_parallel(
        self,
        model_name: str,
        num_ctx: int,
        levels: List[int]
    ) -> List[ThroughputTest]:
        """
        Test parallel processing at different concurrency levels.

        Args:
            model_name: Model to test.
            num_ctx: Context size to use.
            levels: List of parallel concurrency levels to test.
            
        Returns:
            List of ThroughputTest results for parallel processing.
        """
        results = []
        sample_code = self.sample_generator.generate_sample()

        for parallel_count in levels:
            start = time.time()
            requests_to_make = 5 # Reduced requests for quicker simulation

            def process_one_simulated():
                # Simulate LLM call
                simulated_latency = random.uniform(500, 2000) + (num_ctx / 100)
                time.sleep(simulated_latency / 1000.0)
                return "dummy response"

            with ThreadPoolExecutor(max_workers=parallel_count) as executor:
                futures = [executor.submit(process_one_simulated) for _ in range(requests_to_make)]
                for future in futures:
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Error during parallel throughput test: {e}")

            duration = time.time() - start
            throughput = requests_to_make / duration if duration > 0 else 0

            results.append(ThroughputTest(
                parallel=parallel_count,
                delay=0,
                throughput_fps=throughput,
                total_time=duration
            ))

        return results

    def _calculate_batch_size(
        self,
        best: ThroughputTest,
        profile: SystemProfile
    ) -> int:
        """
        Calculate recommended batch size based on optimal throughput test.

        Args:
            best: The best ThroughputTest result.
            profile: The system profile.

        Returns:
            Recommended batch size.
        """
        if best.parallel > 1:
            base_size = 50
        else:
            base_size = 10

        memory_factor = min(2.0, profile.available_ram_gb / 8.0)

        return int(base_size * memory_factor)

    def _calculate_batch_delay(self, best: ThroughputTest) -> float:
        """
        Calculate recommended batch delay based on optimal throughput test.

        Args:
            best: The best ThroughputTest result.

        Returns:
            Recommended batch delay.
        """
        return best.delay

