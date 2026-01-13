from typing import Dict, Any
from rich.console import Console

from ..config_manager import ConfigManager
from .models import BenchmarkConfig, OptimizedConfig, SystemProfile, ModelBenchmarkResults, LatencyBenchmarkResults, ThroughputBenchmarkResults
from .system_profiler import SystemProfiler
from .model_benchmarker import ModelBenchmarker
from .latency_benchmarker import LatencyBenchmarker
from .throughput_benchmarker import ThroughputBenchmarker
from .config_builder import OptimizedConfigBuilder

class BenchmarkOrchestrator:
    """
    Box: Benchmark Orchestrator

    Input: ConfigManager, BenchmarkConfig
    Output: OptimizedConfig
    Responsibility: Coordinate all benchmark tests and aggregate results
    """

    def __init__(
        self,
        config_manager: ConfigManager,
        system_profiler: SystemProfiler,
        model_benchmarker: ModelBenchmarker,
        latency_benchmarker: LatencyBenchmarker,
        throughput_benchmarker: ThroughputBenchmarker,
        optimized_config_builder: OptimizedConfigBuilder,
        console: Console
    ):
        self.config_manager = config_manager
        self.system_profiler = system_profiler
        self.model_benchmarker = model_benchmarker
        self.latency_benchmarker = latency_benchmarker
        self.throughput_benchmarker = throughput_benchmarker
        self.optimized_config_builder = optimized_config_builder
        self.console = console

    def run_full_benchmark(self, benchmark_config: BenchmarkConfig) -> OptimizedConfig:
        """
        Run complete benchmarking suite.
        """
        self.console.info(f"Running benchmarks with intensity: [bold magenta]{benchmark_config.intensity}[/bold magenta]")

        try:
            # 1. Profile system
            self.console.step("Profiling system resources", 1)
            system_profile: SystemProfile = self.system_profiler.profile()
            self.console.substep(f"CPU: {system_profile.cpu_cores} cores, RAM: {system_profile.available_ram_gb:.1f}GB available")
            
            model_name = self.config_manager.get("model_name", "ministral-3:3b")

            # 2. Benchmark model
            self.console.step(f"Benchmarking model '{model_name}'", 2)
            model_results: ModelBenchmarkResults = self.model_benchmarker.benchmark_model(
                model_name, system_profile, benchmark_config
            )
            self.console.substep(f"Optimal Context: [highlight]{model_results.optimal_num_ctx}[/highlight], Optimal Chunk: [highlight]{model_results.optimal_chunk_size}[/highlight]")

            # 3. Find optimal latency
            self.console.step("Benchmarking latency and retries", 3)
            latency_results: LatencyBenchmarkResults = self.latency_benchmarker.benchmark_latency(
                model_name, model_results.optimal_num_ctx, benchmark_config
            )
            self.console.substep(f"Avg Latency: [highlight]{latency_results.avg_request_latency_ms:.1f}ms[/highlight], Retries: [highlight]{latency_results.optimal_retry_attempts}[/highlight]")

            # 4. Find optimal throughput
            self.console.step("Benchmarking throughput and parallelism", 4)
            throughput_results: ThroughputBenchmarkResults = self.throughput_benchmarker.benchmark_throughput(
                system_profile, latency_results, model_name, model_results.optimal_num_ctx, benchmark_config
            )
            self.console.substep(f"Optimal Parallel: [highlight]{throughput_results.optimal_parallel_requests}[/highlight], Throughput: [highlight]{throughput_results.max_throughput_fps:.1f} files/s[/highlight]")

            # 5. Aggregate and build optimized config
            self.console.step("Finalizing optimized configuration", 5)
            optimized_config: OptimizedConfig = self.optimized_config_builder.build(
                system_profile,
                model_results,
                latency_results,
                throughput_results
            )
            
            self.console.success("Successfully built optimized configuration.")
            return optimized_config

        except Exception as e:
            self.console.error(f"A critical error occurred during benchmarking: {e}")
            import traceback
            traceback.print_exc()
            raise
