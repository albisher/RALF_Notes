from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# Implied by fine_tune command
@dataclass
class BenchmarkConfig:
    intensity: str = "normal" # "quick", "normal", "full"
    request_timeout_seconds: int = 300
    max_attempts: int = 3

@dataclass
class SystemProfile:
    """System capabilities and resources."""
    cpu_cores: int
    cpu_threads: int
    total_ram_gb: float
    available_ram_gb: float
    has_gpu: bool
    gpu_memory_gb: float
    ollama_host: str
    ollama_responding: bool
    ollama_version: str

@dataclass
class ContextTest:
    """Single context size test result."""
    num_ctx: int
    avg_latency_ms: float
    success_rate: float
    memory_usage_mb: float
    quality_score: float # Based on output validation

@dataclass
class ChunkTest:
    """Single chunk size test result."""
    chunk_size: int
    avg_latency_ms: float
    success_rate: float
    memory_usage_mb: float
    quality_score: float

@dataclass
class ModelBenchmarkResults:
    """Results from model benchmarking."""
    model_name: str
    optimal_num_ctx: int
    optimal_chunk_size: int
    optimal_max_content_length: int
    optimal_temperature: float
    context_tests: List[ContextTest]
    chunk_tests: List[ChunkTest]

@dataclass
class LatencyBenchmarkResults:
    """Results from latency benchmarking."""
    avg_request_latency_ms: float
    p50_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    optimal_timeout_seconds: int
    optimal_retry_attempts: int
    optimal_backoff_seconds: float
    error_rate: float

# Implied by ThroughputBenchmarker's _test_sequential and _test_parallel methods
@dataclass
class ThroughputTest:
    parallel: int
    delay: float
    throughput_fps: float
    total_time: float

@dataclass
class ThroughputBenchmarkResults:
    """Results from throughput benchmarking."""
    optimal_parallel_requests: int
    optimal_delay_seconds: float
    max_throughput_fps: float  # Files per second
    recommended_batch_size: int
    recommended_batch_delay: float


@dataclass
class OptimizedConfig:
    """Complete optimized configuration."""
    # Model settings
    model_name: str
    num_ctx: int
    temperature: float
    chunk_size: int
    max_content_length: int
    max_chunk_summary_length: int

    # Performance settings
    request_delay_seconds: float
    max_concurrent_requests: int
    retry_attempts: int
    initial_backoff_seconds: float
    backoff_multiplier: float
    request_timeout_seconds: int

    # Batch settings
    batch_size: int
    batch_delay_seconds: float

    # Metadata
    system_profile: SystemProfile
    confidence_score: float # 0-100
    benchmark_date: str = field(default_factory=lambda: datetime.now().isoformat())
