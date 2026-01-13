import time
import random
from typing import List, Optional, Any
from ollama import Client

from .models import LatencyBenchmarkResults, SystemProfile, ModelBenchmarkResults
from .sample_generator import SampleCodeGenerator

class LatencyBenchmarker:
    """
    Box: Latency Benchmarker

    Input: SystemProfile, ModelBenchmarkResults
    Output: LatencyBenchmarkResults
    Responsibility: Determine optimal timeout and retry settings
    """

    def __init__(
        self,
        ollama_client: Client,
        sample_generator: SampleCodeGenerator
    ):
        self.client = ollama_client
        self.sample_generator = sample_generator

    def benchmark_latency(
        self,
        model_name: str,
        num_ctx: int,
        benchmark_config: 'BenchmarkConfig',
        progress: Any = None,
        main_task_id: Any = None
    ) -> LatencyBenchmarkResults:
        """
        Benchmark request latencies.

        Args:
            model_name: Model to test
            num_ctx: Context size to use
            benchmark_config: The benchmark configuration object.
            progress: Progress manager
            main_task_id: Main task ID

        Returns:
            Latency statistics and recommendations
        """
        intensity_map = {
            "quick": 5,
            "normal": 10,
            "full": 20
        }
        sample_count = intensity_map.get(benchmark_config.intensity, 10)
        
        latencies = []
        errors = 0

        sample_code = self.sample_generator.generate_sample()

        for i in range(sample_count):
            if progress and main_task_id is not None:
                progress.update(main_task_id, description=f"[cyan]Latency Test: {i+1}/{sample_count}")
            start = time.time()

            try:
                # Dummy response for now
                # In a real scenario, this would be an actual LLM call
                # response = self.client.generate(
                #     model=model_name,
                #     prompt=sample_code,
                #     options={"num_ctx": num_ctx}
                # )
                # Simulate some latency and occasional errors
                simulated_latency = random.uniform(500, 2000) + (num_ctx / 100)
                time.sleep(simulated_latency / 1000.0) 
                
                if random.random() < 0.05: # 5% chance of simulated error
                    raise Exception("Simulated Ollama error")
                
                latencies.append(simulated_latency)
            except Exception:
                errors += 1
            finally:
                if progress and main_task_id is not None:
                    progress.update(main_task_id, advance=1)

        if not latencies:
            # All failed - use conservative defaults
            return LatencyBenchmarkResults(
                avg_request_latency_ms=30000.0,
                p50_latency_ms=30000.0,
                p95_latency_ms=60000.0,
                p99_latency_ms=120000.0,
                optimal_timeout_seconds=180,
                optimal_retry_attempts=5,
                optimal_backoff_seconds=2.0,
                error_rate=1.0
            )

        latencies.sort()

        avg_latency = sum(latencies) / len(latencies)
        p50 = latencies[len(latencies) // 2]
        # Ensure index is valid for p95 and p99
        p95 = latencies[int(len(latencies) * 0.95)] if len(latencies) > 19 else latencies[-1]
        p99 = latencies[int(len(latencies) * 0.99)] if len(latencies) > 99 else latencies[-1]


        return LatencyBenchmarkResults(
            avg_request_latency_ms=avg_latency,
            p50_latency_ms=p50,
            p95_latency_ms=p95,
            p99_latency_ms=p99,
            optimal_timeout_seconds=self._calculate_timeout(latencies),
            optimal_retry_attempts=self._calculate_retries(errors, sample_count),
            optimal_backoff_seconds=self._calculate_backoff(latencies),
            error_rate=errors / sample_count
        )

    def _calculate_timeout(self, latencies: List[float]) -> int:
        """
        Calculate optimal timeout.

        Strategy: 3x the P99 latency, minimum 60s, maximum 300s.
        """
        if not latencies:
            return 180

        # Ensure that p99 index is valid
        p99_index = int(len(latencies) * 0.99)
        p99 = latencies[p99_index] if p99_index < len(latencies) else latencies[-1]

        timeout = int((p99 / 1000) * 3)

        return max(60, min(300, timeout))  # Clamp to 60-300s

    def _calculate_retries(self, errors: int, total: int) -> int:
        """
        Calculate optimal retry attempts.

        Strategy:
        - No errors: 2 retries (for occasional failures)
        - Some errors: 3-5 retries based on error rate
        - High error rate: 7 retries (to increase success chance)
        """
        if total == 0:
            return 3

        error_rate = errors / total

        if error_rate == 0:
            return 2
        elif error_rate < 0.1:
            return 3
        elif error_rate < 0.3:
            return 5
        else:
            return 7

    def _calculate_backoff(self, latencies: List[float]) -> float:
        """
        Calculate initial backoff duration.

        Strategy: 10% of average latency, minimum 0.5s, maximum 5.0s.
        """
        if not latencies:
            return 1.0

        avg_latency_s = sum(latencies) / len(latencies) / 1000
        backoff = avg_latency_s * 0.1

        return max(0.5, min(5.0, backoff))  # Clamp to 0.5-5s
