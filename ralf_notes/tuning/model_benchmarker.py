import time
import random
from typing import List, Optional
from ollama import Client

from .models import ModelBenchmarkResults, SystemProfile, ContextTest, ChunkTest
from .sample_generator import SampleCodeGenerator

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
        benchmark_config: 'BenchmarkConfig'
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
        if benchmark_config.intensity == "quick":
            context_test_sizes = [4096, 8192]
            chunk_test_sizes = [100000]
        elif benchmark_config.intensity == "full":
            context_test_sizes = [2048, 4096, 6144, 8192, 12288, 16384, 32768]
            chunk_test_sizes = [50000, 100000, 150000, 200000, 300000, 400000]
        else: # normal
            context_test_sizes = [4096, 8192, 16384]
            chunk_test_sizes = [100000, 200000]

        context_tests = self._benchmark_context_sizes(
            model_name,
            profile,
            test_sizes=context_test_sizes
        )

        chunk_tests = self._benchmark_chunk_sizes(
            model_name,
            profile,
            test_sizes=chunk_test_sizes
        )

        optimal_ctx = self._find_optimal_context(context_tests, profile)
        optimal_chunk = self._find_optimal_chunk(chunk_tests, profile)
        optimal_content = self._calculate_optimal_content_length(optimal_ctx)
        optimal_temp = self._find_optimal_temperature(model_name)

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
        test_sizes: List[int]
    ) -> List[ContextTest]:
        """
        Test different context window sizes.
        
        Args:
            model_name: The name of the model to benchmark.
            profile: The system profile for resource constraints.
            test_sizes: A list of context sizes to test.
            
        Returns:
            A list of ContextTest results.
        """
        results = []
        sample_code = self.sample_generator.generate_sample()

        for size in test_sizes:
            estimated_memory = self._estimate_memory_usage(size)
            if estimated_memory > profile.available_ram_gb * 0.8 * 1024:
                print(f"Skipping context size {size}: requires too much memory.")
                continue

            latencies = []
            successes = 0
            memory_usages = []

            for _ in range(3):
                try:
                    start = time.time()
                    memory_before = self._get_memory_usage()

                    # In a real scenario, this would be an actual LLM call
                    # For now, simulate it
                    time.sleep(0.1 + (size / 100000.0)) # Simulate latency based on size
                    response_text = '{"key": "value"}' if random.random() > 0.1 else "invalid json"

                    latencies.append((time.time() - start) * 1000)
                    successes += 1
                    memory_after = self._get_memory_usage()
                    memory_usages.append(memory_after - memory_before)
                except Exception as e:
                    print(f"Error during context size benchmark for size {size}: {e}")

            if latencies:
                avg_latency = sum(latencies) / len(latencies)
                avg_memory_usage = sum(memory_usages) / len(memory_usages) if memory_usages else 0
                results.append(ContextTest(
                    num_ctx=size,
                    avg_latency_ms=avg_latency,
                    success_rate=successes / 3.0,
                    memory_usage_mb=avg_memory_usage,
                    quality_score=self._evaluate_quality(response_text)
                ))

        return results

    def _benchmark_chunk_sizes(
        self,
        model_name: str,
        profile: SystemProfile,
        test_sizes: List[int]
    ) -> List[ChunkTest]:
        """
        Test different chunk sizes for large file summarization.
        
        Args:
            model_name: The name of the model to benchmark.
            profile: The system profile for resource constraints.
            test_sizes: A list of chunk sizes to test.

        Returns:
            A list of ChunkTest results.
        """
        results = []
        
        for size in test_sizes:
            # This is a simplified placeholder
            avg_latency = 500 + (size / 2000)
            success_rate = 1.0
            memory_usage = 50 + (size / 20000)
            response_text = '{"summary": "This is a chunk summary."}'

            results.append(ChunkTest(
                chunk_size=size,
                avg_latency_ms=avg_latency,
                success_rate=success_rate,
                memory_usage_mb=memory_usage,
                quality_score=self._evaluate_quality(response_text)
            ))
        return results


    def _find_optimal_context(
        self,
        tests: List[ContextTest],
        profile: SystemProfile
    ) -> int:
        """
        Find optimal context size balancing speed, quality, and resources.

        Strategy:
        1. Filter out tests with low success rate (<90%)
        2. Find the largest context that doesn't exceed memory budget
        3. Prefer larger contexts if latency difference is < 20%
        """
        good_tests = [t for t in tests if t.success_rate >= 0.9]
        if not good_tests:
            return 8192  # Safe default

        memory_budget_mb = profile.available_ram_gb * 0.5 * 1024
        memory_ok_tests = [t for t in good_tests if t.memory_usage_mb < memory_budget_mb]

        if not memory_ok_tests:
            return min((t.num_ctx for t in good_tests), default=8192)

        sorted_tests = sorted(memory_ok_tests, key=lambda t: t.num_ctx, reverse=True)
        if len(sorted_tests) <= 1:
            return sorted_tests[0].num_ctx

        baseline_latency = sorted(sorted_tests, key=lambda t: t.num_ctx)[0].avg_latency_ms
        if baseline_latency == 0:
            return sorted_tests[0].num_ctx

        for test in sorted_tests:
            latency_increase = (test.avg_latency_ms - baseline_latency) / baseline_latency
            if latency_increase <= 0.20:
                return test.num_ctx

        return sorted_tests[-1].num_ctx

    def _find_optimal_chunk(
        self,
        tests: List[ChunkTest],
        profile: SystemProfile
    ) -> int:
        """
        Find optimal chunk size.
        Simplified for now, just picks the largest successful chunk size that fits in memory.
        """
        good_tests = [t for t in tests if t.success_rate >= 0.9]
        if not good_tests:
            return 100000

        memory_budget_mb = profile.available_ram_gb * 0.5 * 1024
        memory_ok_tests = [t for t in good_tests if t.memory_usage_mb < memory_budget_mb]

        if not memory_ok_tests:
            return max((t.chunk_size for t in good_tests), default=100000)
        
        return max(t.chunk_size for t in memory_ok_tests)


    def _calculate_optimal_content_length(self, optimal_num_ctx: int) -> int:
        """
        Calculate optimal max content length for a single prompt.
        Heuristic: Assumes content should take up about 75% of the context window.
        """
        return int(optimal_num_ctx * 0.75)

    def _find_optimal_temperature(self, model_name: str) -> float:
        """
        Determine optimal temperature for a given model.
        Returns a fixed low temperature for consistent JSON output.
        """
        return 0.1

    def _evaluate_quality(self, response_text: str) -> float:
        """
        Evaluates the quality of the LLM's response.
        Placeholder that gives a higher score if it looks like JSON.
        """
        if response_text and '{' in response_text and '}' in response_text:
            return 0.9 + random.uniform(-0.1, 0.1) # High score for JSON-like
        return 0.2 + random.uniform(-0.1, 0.1) # Low score otherwise

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
        return (num_ctx * 1.5) / (1024 * 1024) + 50 # Base 50MB overhead