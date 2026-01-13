import time
import random
import logging
from typing import List, Optional, Dict, Any
from ollama import Client

from .models import ModelBenchmarkResults, SystemProfile, ContextTest, ChunkTest, BenchmarkConfig # Import BenchmarkConfig
from .sample_generator import SampleCodeGenerator

logger = logging.getLogger(__name__)

class ModelBenchmarker:
    """
    Box: Model Benchmarker

    Input: Model name, SystemProfile
    Output: ModelBenchmarkResults
    Responsibility: Find optimal model settings through testing
    """

    def __init__(
        self,
        ollama_client: Client,
        sample_generator: SampleCodeGenerator
    ):
        self.client = ollama_client
        self.sample_generator = sample_generator

    def benchmark_model(
        self,
        model_name: str,
        profile: SystemProfile,
        benchmark_config: BenchmarkConfig,
        progress: Any = None, # ADD progress object
        main_task_id: Any = None # ADD main task ID
    ) -> ModelBenchmarkResults:
        """
        Benchmark model with different settings.

        Args:
            model_name: Name of Ollama model
            profile: System profile for constraints
            benchmark_config: The benchmark configuration object.

        Returns:
            Complete benchmark results with recommendations
        """
        logger.info("Starting benchmark for model: %s with intensity: %s", model_name, benchmark_config.intensity)
        if benchmark_config.intensity == "quick":
            context_test_sizes = [4096, 8192]
            chunk_test_sizes = [50000]
        elif benchmark_config.intensity == "full":
            context_test_sizes = [2048, 4096, 6144, 8192, 12288, 16384, 32768]
            chunk_test_sizes = [50000, 100000, 150000, 200000, 300000, 400000]
        else: # normal
            context_test_sizes = [4096, 8192, 12288]
            chunk_test_sizes = [50000, 100000]

        max_attempts = benchmark_config.max_attempts

        context_tests = self._benchmark_context_sizes(
            model_name,
            profile,
            test_sizes=context_test_sizes,
            timeout=benchmark_config.request_timeout_seconds,
            attempts=max_attempts,
            progress=progress, # Pass progress
            main_task_id=main_task_id # Pass main task ID
        )
        logger.debug("Context size benchmarks completed.")
        if progress and main_task_id is not None:
            progress.update(main_task_id, advance=len(context_test_sizes) * max_attempts)


        chunk_tests = self._benchmark_chunk_sizes(
            model_name,
            profile,
            test_sizes=chunk_test_sizes,
            timeout=benchmark_config.request_timeout_seconds,
            attempts=max_attempts,
            progress=progress, # Pass progress
            main_task_id=main_task_id # Pass main task ID
        )
        logger.debug("Chunk size benchmarks completed.")
        if progress and main_task_id is not None:
            progress.update(main_task_id, advance=len(chunk_test_sizes) * max_attempts)

        optimal_ctx = self._find_optimal_context(context_tests, profile)
        optimal_chunk = self._find_optimal_chunk(chunk_tests, profile)
        optimal_content = self._calculate_optimal_content_length(optimal_ctx)
        optimal_temp = self._find_optimal_temperature(model_name) # This should actually be benchmarked

        logger.info("Benchmark complete for %s. Optimal ctx: %d, chunk: %d, content: %d, temp: %.1f",
                    model_name, optimal_ctx, optimal_chunk, optimal_content, optimal_temp)

        return ModelBenchmarkResults(
            model_name=model_name,
            optimal_num_ctx=optimal_ctx,
            optimal_chunk_size=optimal_chunk,
            optimal_max_content_length=optimal_content,
            optimal_temperature=optimal_temp,
            context_tests=context_tests,
            chunk_tests=chunk_tests
        )

    def _benchmark_context_sizes(
        self,
        model_name: str,
        profile: SystemProfile,
        test_sizes: List[int],
        timeout: int,
        attempts: int = 3,
        progress: Any = None, # ADD progress object
        main_task_id: Any = None # ADD main task ID
    ) -> List[ContextTest]:
        """
        Test different context window sizes using actual LLM calls.
        """
        results = []
        base_sample_code = self.sample_generator.generate_long_sample(max_length=max(test_sizes) * 2) # Use a larger sample for context tests
        
        if progress and main_task_id is not None:
            context_task_id = progress.add_task(f"[cyan]Context Benchmarking ({model_name})...", total=len(test_sizes) * attempts)

        for size in test_sizes:
            logger.debug("Benchmarking context size: %d for model %s", size, model_name)
            if progress and context_task_id is not None:
                progress.update(context_task_id, description=f"[cyan]Context Size: {size}")

            estimated_memory = self._estimate_memory_usage(size)
            if estimated_memory > profile.available_ram_gb * 0.8 * 1024:
                logger.warning("Skipping context size %d: estimated memory usage %.2fMB exceeds 80%% of available RAM (%.2fMB).",
                               size, estimated_memory, profile.available_ram_gb * 0.8 * 1024)
                if progress and context_task_id is not None:
                    progress.update(context_task_id, advance=attempts) # Advance for skipped attempts
                continue

            latencies = []
            successes = 0
            memory_usages = []
            quality_scores = []
            response_text = ""

            current_sample_code = base_sample_code[:size]

            for _ in range(attempts): # Run multiple times for average
                try:
                    start = time.time()
                    memory_before = self._get_memory_usage()

                    response = self.client.generate(
                        model=model_name,
                        system="Return a summary of the provided code.",
                        prompt=f"Code:\n{current_sample_code}",
                        options={"num_ctx": size, "temperature": 0.1, "timeout": timeout}
                    )
                    response_text = response['response']

                    latencies.append((time.time() - start) * 1000)
                    successes += 1
                    memory_after = self._get_memory_usage()
                    memory_usages.append(memory_after - memory_before)
                    quality_scores.append(self._evaluate_quality(response_text))
                    logger.debug("Context size %d test successful (attempt %d). Latency: %.2fms", size, _ + 1, latencies[-1])
                except Exception as e:
                    logger.error("Error during context size benchmark for size %d (attempt %d): %s", size, _ + 1, e)
                finally:
                    if progress and context_task_id is not None:
                        progress.update(context_task_id, advance=1)

            if latencies:
                avg_latency = sum(latencies) / len(latencies)
                avg_memory_usage = sum(memory_usages) / len(memory_usages) if memory_usages else 0
                avg_quality_score = sum(quality_scores) / len(quality_scores) if quality_scores else 0
                results.append(ContextTest(
                    num_ctx=size,
                    avg_latency_ms=avg_latency,
                    success_rate=float(successes) / attempts,
                    memory_usage_mb=avg_memory_usage,
                    quality_score=avg_quality_score
                ))
            else:
                logger.warning("No successful runs for context size %d.", size)

        return results

    def _benchmark_chunk_sizes(
        self,
        model_name: str,
        profile: SystemProfile,
        test_sizes: List[int],
        timeout: int,
        attempts: int = 3,
        progress: Any = None, # ADD progress object
        main_task_id: Any = None # ADD main task ID
    ) -> List[ChunkTest]:
        """
        Test different chunk sizes for large file summarization using actual LLM calls.
        """
        results = []
        large_sample_code = self.sample_generator.generate_long_sample(max_length=max(test_sizes) * 2)

        if progress and main_task_id is not None:
            chunk_task_id = progress.add_task(f"[cyan]Chunk Benchmarking ({model_name})...", total=len(test_sizes) * attempts)

        for size in test_sizes:
            logger.debug("Benchmarking chunk size: %d for model %s", size, model_name)
            if progress and chunk_task_id is not None:
                progress.update(chunk_task_id, description=f"[cyan]Chunk Size: {size}")
            
            current_chunk = large_sample_code[:size]

            estimated_memory = self._estimate_memory_usage(size)
            if estimated_memory > profile.available_ram_gb * 0.8 * 1024:
                logger.warning("Skipping chunk size %d: estimated memory usage %.2fMB exceeds 80%% of available RAM (%.2fMB).",
                               size, estimated_memory, profile.available_ram_gb * 0.8 * 1024)
                if progress and chunk_task_id is not None:
                    progress.update(chunk_task_id, advance=attempts) # Advance for skipped attempts
                continue

            latencies = []
            successes = 0
            memory_usages = []
            quality_scores = []
            response_text = ""

            for _ in range(attempts): # Run multiple times for average
                try:
                    start = time.time()
                    memory_before = self._get_memory_usage()

                    response = self.client.generate(
                        model=model_name,
                        system="Return a concise summary of the provided code chunk in structured text format: ### SUMMARY\n<summary>",
                        prompt=f"Code chunk:\n{current_chunk}",
                        options={"num_ctx": size, "temperature": 0.1, "timeout": timeout}
                    )
                    response_text = response['response']

                    latencies.append((time.time() - start) * 1000)
                    successes += 1
                    memory_after = self._get_memory_usage()
                    memory_usages.append(memory_after - memory_before)
                    quality_scores.append(self._evaluate_quality(response_text, expect_structured_summary=True))
                    logger.debug("Chunk size %d test successful (attempt %d). Latency: %.2fms", size, _ + 1, latencies[-1])
                except Exception as e:
                    logger.error("Error during chunk size benchmark for size %d (attempt %d): %s", size, _ + 1, e)
                finally:
                    if progress and chunk_task_id is not None:
                        progress.update(chunk_task_id, advance=1)

            if latencies:
                avg_latency = sum(latencies) / len(latencies)
                avg_memory_usage = sum(memory_usages) / len(memory_usages) if memory_usages else 0
                avg_quality_score = sum(quality_scores) / len(quality_scores) if quality_scores else 0
                results.append(ChunkTest(
                    chunk_size=size,
                    avg_latency_ms=avg_latency,
                    success_rate=float(successes) / attempts,
                    memory_usage_mb=avg_memory_usage,
                    quality_score=avg_quality_score
                ))
            else:
                logger.warning("No successful runs for chunk size %d.", size)

        return results


    def _find_optimal_context(
        self,
        tests: List[ContextTest],
        profile: SystemProfile
    ) -> int:
        """
        Find optimal context size balancing speed, quality, and resources.

        Strategy:
        1. Filter out tests with low success rate (<90%) and low quality (<0.7)
        2. Find the largest context that doesn't exceed memory budget
        3. Prefer larger contexts if latency difference is < 20%
        """
        logger.debug("Finding optimal context size from %d tests.", len(tests))
        good_tests = [t for t in tests if t.success_rate >= 0.9 and t.quality_score >= 0.7]
        if not good_tests:
            logger.warning("No good context tests found. Returning safe default 8192.")
            return 8192  # Safe default

        memory_budget_mb = profile.available_ram_gb * 0.5 * 1024 # Use 50% of available RAM
        memory_ok_tests = [t for t in good_tests if t.memory_usage_mb < memory_budget_mb]

        if not memory_ok_tests:
            logger.warning("No context tests fit memory budget. Returning largest context from good tests.")
            return max((t.num_ctx for t in good_tests), default=8192)

        # Prioritize larger contexts with good quality and reasonable latency
        # Sort by quality then context size
        sorted_tests = sorted(memory_ok_tests, key=lambda t: (t.quality_score, t.num_ctx), reverse=True)
        
        # Pick the best quality and largest context that meets criteria
        # For simplicity, pick the first one from the sorted list
        optimal_test = sorted_tests[0]
        logger.info("Optimal context found: %d (Latency: %.2fms, Quality: %.2f)",
                    optimal_test.num_ctx, optimal_test.avg_latency_ms, optimal_test.quality_score)
        return optimal_test.num_ctx

    def _find_optimal_chunk(
        self,
        tests: List[ChunkTest],
        profile: SystemProfile
    ) -> int:
        """
        Find optimal chunk size balancing speed, quality, and resources.
        
        Strategy:
        1. Filter out tests with low success rate (<90%) and low quality (<0.7)
        2. Find the largest chunk that doesn't exceed memory budget
        3. Prefer larger chunks for better content processing per call
        """
        logger.debug("Finding optimal chunk size from %d tests.", len(tests))
        good_tests = [t for t in tests if t.success_rate >= 0.9 and t.quality_score >= 0.7]
        if not good_tests:
            logger.warning("No good chunk tests found. Returning safe default 100000.")
            return 100000

        memory_budget_mb = profile.available_ram_gb * 0.5 * 1024 # Use 50% of available RAM
        memory_ok_tests = [t for t in good_tests if t.memory_usage_mb < memory_budget_mb]

        if not memory_ok_tests:
            logger.warning("No chunk tests fit memory budget. Returning largest chunk from good tests.")
            return max((t.chunk_size for t in good_tests), default=100000)
        
        # Prioritize larger chunks with good quality
        sorted_tests = sorted(memory_ok_tests, key=lambda t: (t.quality_score, t.chunk_size), reverse=True)
        optimal_test = sorted_tests[0]
        logger.info("Optimal chunk found: %d (Latency: %.2fms, Quality: %.2f)",
                    optimal_test.chunk_size, optimal_test.avg_latency_ms, optimal_test.quality_score)
        return optimal_test.chunk_size


    def _calculate_optimal_content_length(self, optimal_num_ctx: int) -> int:
        """
        Calculate optimal max content length for a single prompt.
        Heuristic: Assumes content should take up about 75% of the context window.
        """
        content_length = int(optimal_num_ctx * 0.75)
        logger.debug("Calculated optimal content length: %d based on context %d", content_length, optimal_num_ctx)
        return content_length

    def _find_optimal_temperature(self, model_name: str) -> float:
        """
        Determine optimal temperature for a given model.
        Returns a fixed low temperature for consistent structured text output.
        """
        logger.debug("Determining optimal temperature for %s. Fixed to 0.1 for structured text.", model_name)
        return 0.1 # Fixed low temperature for consistent structured text output

    def _evaluate_quality(self, response_text: str, expect_structured_summary: bool = False) -> float:
        """
        Evaluates the quality of the LLM's response.
        Checks for structured text format compliance and content.
        Score from 0.0 to 1.0.
        """
        score = 0.0
        # Basic check for structured text format
        if "### SUMMARY" in response_text and "### TAGS" in response_text and "### TYPE" in response_text:
            score += 0.5 # Base score for structured format

        if expect_structured_summary:
            if "### SUMMARY" in response_text and len(response_text.split("### SUMMARY")[-1].strip()) > 10:
                score += 0.3 # Higher score if summary content is present
        else:
            if "### FILENAME" not in response_text: # Filename is no longer expected from LLM, good.
                score += 0.1
            if len(response_text) > 100: # Ensure some content is generated
                score += 0.1

        # Check for presence of key structured text markers
        expected_markers = ["### SUMMARY", "### TAGS", "### TYPE", "### KEY_FUNCTIONS", "### DEPENDENCIES", "### USAGE", "### RELATED", "### CALLOUTS"]
        found_markers = sum(1 for marker in expected_markers if marker in response_text)
        score += (found_markers / len(expected_markers)) * 0.3 # Contribution from finding markers

        # Deduct for presence of unexpected markers (e.g., if it tries to generate FILENAME)
        if "### FILENAME" in response_text:
            score -= 0.2

        # Ensure score is within 0-1 range
        final_score = max(0.0, min(1.0, score + random.uniform(-0.05, 0.05))) # Add a small random jitter
        logger.debug("Evaluated quality: %.2f for response: %s...", final_score, response_text[:100].replace('\n', ' '))
        return final_score

    def _get_memory_usage(self) -> float:
        """
        Simulates getting current process memory usage in MB.
        """
        # In a real scenario, use psutil:
        # import psutil, os
        # process = psutil.Process(os.getpid())
        # return process.memory_info().rss / (1024 * 1024)
        return random.uniform(50.0, 150.0) # Dummy value

    def _estimate_memory_usage(self, num_ctx: int) -> float:
        """
        Simulates estimating memory usage for a given context size in MB.
        """
        # Very rough estimate: (tokens * bytes_per_token) + base_overhead
        return (num_ctx * 1.5) / 1024 / 1024 * 1024 + 50 # Base 50MB overhead, converted to MB