from datetime import datetime
from typing import List

from .models import OptimizedConfig, SystemProfile, ModelBenchmarkResults, LatencyBenchmarkResults, ThroughputBenchmarkResults

class OptimizedConfigBuilder:
    """
    Box: Optimized Config Builder

    Input: All benchmark results
    Output: Complete optimized configuration
    Responsibility: Build final configuration from benchmarks
    """

    def build(
        self,
        system_profile: SystemProfile,
        model_results: ModelBenchmarkResults,
        latency_results: LatencyBenchmarkResults,
        throughput_results: ThroughputBenchmarkResults
    ) -> OptimizedConfig:
        """
        Build optimized configuration.

        Args:
            system_profile: System capabilities
            model_results: Model benchmark results
            latency_results: Latency benchmark results
            throughput_results: Throughput benchmark results

        Returns:
            Complete optimized configuration
        """
        max_chunk_summary_length = model_results.optimal_chunk_size // 25 if model_results.optimal_chunk_size else 1000

        return OptimizedConfig(
            model_name=model_results.model_name,
            num_ctx=model_results.optimal_num_ctx,
            temperature=model_results.optimal_temperature,
            chunk_size=model_results.optimal_chunk_size,
            max_content_length=model_results.optimal_max_content_length,
            max_chunk_summary_length=max_chunk_summary_length,
            request_delay_seconds=throughput_results.optimal_delay_seconds,
            max_concurrent_requests=throughput_results.optimal_parallel_requests,
            retry_attempts=latency_results.optimal_retry_attempts,
            initial_backoff_seconds=latency_results.optimal_backoff_seconds,
            backoff_multiplier=2.0,
            request_timeout_seconds=latency_results.optimal_timeout_seconds,
            batch_size=throughput_results.recommended_batch_size,
            batch_delay_seconds=throughput_results.recommended_batch_delay,
            benchmark_date=datetime.now().isoformat(),
            system_profile=system_profile,
            confidence_score=self._calculate_confidence(
                system_profile,
                model_results,
                latency_results,
                throughput_results
            )
        )

    def _calculate_confidence(
        self,
        system_profile: SystemProfile,
        model_results: ModelBenchmarkResults,
        latency_results: LatencyBenchmarkResults,
        throughput_results: ThroughputBenchmarkResults
    ) -> float:
        """
        Calculate confidence score (0-100).

        Factors:
        - High success rates from model tests
        - Low error rates from latency tests
        - Consistent latencies (low variance)
        - Whether optimal settings hit predefined limits
        """
        confidence = 100.0

        if latency_results.error_rate > 0:
            confidence -= latency_results.error_rate * 30

        if latency_results.p99_latency_ms > latency_results.p50_latency_ms * 3:
            confidence -= 10

        if model_results.optimal_num_ctx >= 32768:
            confidence -= 5

        return max(0, min(100, confidence))
