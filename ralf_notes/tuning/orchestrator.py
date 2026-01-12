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

        Args:
            benchmark_config: Configuration for the benchmark intensity.

        Returns:
            An OptimizedConfig object with the best found settings.
        
        Raises:
            Exception: If any of the benchmark stages fail critically.
        """
        self.console.print(f"Running benchmarks with intensity: [bold magenta]{benchmark_config.intensity}[/bold magenta]")

        try:
            # 1. Profile system
            self.console.print("1. Profiling system resources...")
            system_profile: SystemProfile = self.system_profiler.profile()
            self.console.print(f"   [green]✓[/green] CPU Cores: {system_profile.cpu_cores}, RAM: {system_profile.available_ram_gb:.1f}GB available")
            
            model_name = self.config_manager.get("model_name", "ministral-3:3b")

            # 2. Benchmark model
            self.console.print(f"\n2. Benchmarking model '{model_name}'...")
            model_results: ModelBenchmarkResults = self.model_benchmarker.benchmark_model(
                model_name, system_profile, benchmark_config
            )
            self.console.print(f"   [green]✓[/green] Optimal Context: {model_results.optimal_num_ctx}, Optimal Chunk: {model_results.optimal_chunk_size}")

            # 3. Find optimal latency
            self.console.print("\n3. Benchmarking latency and retries...")
            latency_results: LatencyBenchmarkResults = self.latency_benchmarker.benchmark_latency(
                model_name, model_results.optimal_num_ctx, benchmark_config
            )
            self.console.print(f"   [green]✓[/green] Avg Latency: {latency_results.avg_request_latency_ms:.1f}ms, Retries: {latency_results.optimal_retry_attempts}")

            # 4. Find optimal throughput
            self.console.print("\n4. Benchmarking throughput and parallelism...")
            throughput_results: ThroughputBenchmarkResults = self.throughput_benchmarker.benchmark_throughput(
                system_profile, latency_results, model_name, model_results.optimal_num_ctx, benchmark_config
            )
            self.console.print(f"   [green]✓[/green] Optimal Parallel: {throughput_results.optimal_parallel_requests}, Throughput: {throughput_results.max_throughput_fps:.1f} files/s")

            # 5. Aggregate and build optimized config
            self.console.print("\n5. Aggregating results and building optimized configuration...")
            optimized_config: OptimizedConfig = self.optimized_config_builder.build(
                system_profile,
                model_results,
                latency_results,
                throughput_results
            )
            
            self.console.print("   [green]✓[/green] Successfully built optimized configuration.")
            self.console.print(f"\n   Tuning complete. Confidence Score: [bold green]{optimized_config.confidence_score:.1f}%[/bold green]")
            return optimized_config

        except Exception as e:
            self.console.error(f"A critical error occurred during benchmarking: {e}")
            import traceback
            traceback.print_exc()
            raise
