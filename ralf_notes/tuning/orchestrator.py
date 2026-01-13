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
        from ..tui import ProgressManager
        
        try:
            # Calculate total steps
            model_name = self.config_manager.get("model_name", "ministral-3:3b")
            
            # Setup intensity parameters to calculate total
            if benchmark_config.intensity == "quick":
                ctx_sizes, chunk_sizes = 2, 1
                latency_samples = 5
                throughput_seq, throughput_par = 2, 2
                req_per_test = 2
            elif benchmark_config.intensity == "full":
                ctx_sizes, chunk_sizes = 7, 6
                latency_samples = 20
                throughput_seq, throughput_par = 4, 4
                req_per_test = 5
            else: # normal
                ctx_sizes, chunk_sizes = 3, 2
                latency_samples = 10
                throughput_seq, throughput_par = 3, 2
                req_per_test = 3
            
            attempts = benchmark_config.max_attempts
            total_steps = (
                1 + # Step 1: Profile
                (ctx_sizes * attempts) + # Step 2: Model (Context)
                (chunk_sizes * attempts) + # Step 2: Model (Chunk)
                latency_samples + # Step 3: Latency
                (throughput_seq * req_per_test) + # Step 4: Throughput (Seq)
                (throughput_par * req_per_test * 2) # Step 4: Throughput (Par)
            )

            with ProgressManager(self.console) as progress:
                main_task = progress.add_task("[bold]Optimization Progress", total=total_steps)
                
                # 1. Profile system
                progress.update(main_task, description="[bold blue]Profiling System")
                system_profile: SystemProfile = self.system_profiler.profile()
                progress.update(main_task, advance=1)
                
                # 2. Benchmark model (Advances internally)
                model_results: ModelBenchmarkResults = self.model_benchmarker.benchmark_model(
                    model_name, system_profile, benchmark_config, progress=progress, main_task_id=main_task
                )
                
                # 3. Find optimal latency (Advances internally)
                progress.update(main_task, description="[bold blue]Benchmarking Latency")
                latency_results: LatencyBenchmarkResults = self.latency_benchmarker.benchmark_latency(
                    model_name, model_results.optimal_num_ctx, benchmark_config, progress=progress, main_task_id=main_task
                )

                # 4. Find optimal throughput (Advances internally)
                throughput_results: ThroughputBenchmarkResults = self.throughput_benchmarker.benchmark_throughput(
                    system_profile, latency_results, model_name, model_results.optimal_num_ctx, benchmark_config,
                    progress=progress, main_task_id=main_task
                )

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