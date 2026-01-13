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
        from rich.live import Live
        from ..tui import ProgressManager
        
        self.console.info(f"Starting optimization suite (Intensity: [bold magenta]{benchmark_config.intensity}[/bold magenta])")

        try:
            with ProgressManager(self.console) as progress:
                main_task = progress.add_task("[bold]Total Progress", total=4)
                
                # 1. Profile system
                progress.update(main_task, description="[bold blue]Step 1: Profiling System")
                system_profile: SystemProfile = self.system_profiler.profile()
                self.console.substep(f"CPU: {system_profile.cpu_cores} cores, RAM: {system_profile.available_ram_gb:.1f}GB available")
                progress.update(main_task, advance=1)
                
                model_name = self.config_manager.get("model_name", "ministral-3:3b")

                # 2. Benchmark model
                progress.update(main_task, description=f"[bold blue]Step 2: Benchmarking {model_name}")
                model_results: ModelBenchmarkResults = self.model_benchmarker.benchmark_model(
                    model_name, system_profile, benchmark_config, progress=progress, main_task_id=main_task
                )
                self.console.substep(f"Optimal Context: [highlight]{model_results.optimal_num_ctx}[/highlight], Chunk: [highlight]{model_results.optimal_chunk_size}[/highlight]")
                progress.update(main_task, advance=1)
                
                # 3. Find optimal latency
                progress.update(main_task, description="[bold blue]Step 3: Benchmarking Latency")
                latency_results: LatencyBenchmarkResults = self.latency_benchmarker.benchmark_latency(
                    model_name, model_results.optimal_num_ctx, benchmark_config
                )
                self.console.substep(f"Avg Latency: [highlight]{latency_results.avg_request_latency_ms:.1f}ms[/highlight]")
                progress.update(main_task, advance=1)

                # 4. Find optimal throughput
                progress.update(main_task, description="[bold blue]Step 4: Benchmarking Throughput")
                throughput_results: ThroughputBenchmarkResults = self.throughput_benchmarker.benchmark_throughput(
                    system_profile, latency_results, model_name, model_results.optimal_num_ctx, benchmark_config,
                    progress=progress, main_task_id=main_task
                )
                self.console.substep(f"Throughput: [highlight]{throughput_results.max_throughput_fps:.1f} files/s[/highlight]")
                progress.update(main_task, advance=1)

                # 5. Aggregate
                progress.update(main_task, description="[bold green]Finalizing results...")
                optimized_config: OptimizedConfig = self.optimized_config_builder.build(
                    system_profile,
                    model_results,
                    latency_results,
                    throughput_results
                )
                
                progress.complete(main_task)
            
            return optimized_config

        except Exception as e:
            self.console.error(f"A critical error occurred during benchmarking: {e}")
            import traceback
            traceback.print_exc()
            raise
