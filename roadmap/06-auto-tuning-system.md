# RALF Note Auto-Tuning System - Complete Implementation Roadmap

**Feature:** `ralf-notes fine-tune` command
**Purpose:** Automatically determine optimal configuration for the current system
**Methodology:** Boxes + OOP + Dependency Injection
**Date:** January 2026

---

## 🎯 Vision

An intelligent benchmarking system that:
- **Discovers** optimal delay, retry, and parallel settings
- **Benchmarks** model performance with different context/chunk sizes
- **Measures** system capacity (CPU, memory, Ollama responsiveness)
- **Saves** optimized configuration automatically
- **Reports** findings with clear recommendations

---

## 📦 Architecture - Boxes Methodology

### Box 1: **Benchmark Orchestrator**
**Input:** ConfigManager, BenchmarkConfig
**Output:** OptimizedConfig
**Responsibility:** Coordinate all benchmark tests and aggregate results

```python
class BenchmarkOrchestrator:
    """
    Box: Benchmark Orchestrator

    Input: ConfigManager, BenchmarkConfig
    Output: OptimizedConfig
    Responsibility: Run all benchmarks and determine optimal settings
    """

    def __init__(
        self,
        config_manager: ConfigManager,
        system_profiler: SystemProfiler,
        model_benchmarker: ModelBenchmarker,
        latency_benchmarker: LatencyBenchmarker,
        throughput_benchmarker: ThroughputBenchmarker,
        console: Console
    ):
        self.config_manager = config_manager
        self.system_profiler = system_profiler
        self.model_benchmarker = model_benchmarker
        self.latency_benchmarker = latency_benchmarker
        self.throughput_benchmarker = throughput_benchmarker
        self.console = console

    def run_full_benchmark(self) -> OptimizedConfig:
        """Run complete benchmarking suite."""
        # 1. Profile system
        # 2. Benchmark model
        # 3. Find optimal latency
        # 4. Find optimal throughput
        # 5. Aggregate and return
```

---

### Box 2: **System Profiler**
**Input:** None
**Output:** SystemProfile
**Responsibility:** Detect system capabilities (CPU, RAM, GPU, Ollama)

```python
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


class SystemProfiler:
    """
    Box: System Profiler

    Input: None
    Output: SystemProfile
    Responsibility: Detect and measure system resources
    """

    def profile(self) -> SystemProfile:
        """
        Profile the system.

        Returns:
            SystemProfile with all detected capabilities
        """
        return SystemProfile(
            cpu_cores=self._detect_cpu_cores(),
            cpu_threads=self._detect_cpu_threads(),
            total_ram_gb=self._detect_total_ram(),
            available_ram_gb=self._detect_available_ram(),
            has_gpu=self._detect_gpu(),
            gpu_memory_gb=self._detect_gpu_memory(),
            ollama_host=self._get_ollama_host(),
            ollama_responding=self._check_ollama(),
            ollama_version=self._get_ollama_version()
        )

    def _detect_cpu_cores(self) -> int:
        """Detect physical CPU cores."""
        import psutil
        return psutil.cpu_count(logical=False)

    def _detect_cpu_threads(self) -> int:
        """Detect logical CPU threads."""
        import psutil
        return psutil.cpu_count(logical=True)

    def _detect_total_ram(self) -> float:
        """Detect total system RAM in GB."""
        import psutil
        return psutil.virtual_memory().total / (1024**3)

    def _detect_available_ram(self) -> float:
        """Detect available RAM in GB."""
        import psutil
        return psutil.virtual_memory().available / (1024**3)

    def _detect_gpu(self) -> bool:
        """Check if GPU is available."""
        # Check for CUDA, Metal, ROCm, etc.
        pass

    def _detect_gpu_memory(self) -> float:
        """Detect GPU memory in GB."""
        # Platform-specific detection
        pass

    def _check_ollama(self) -> bool:
        """Check if Ollama is responding."""
        try:
            client = Client(host=self._get_ollama_host())
            client.list()
            return True
        except:
            return False

    def _get_ollama_version(self) -> str:
        """Get Ollama version."""
        try:
            # Parse from ollama --version
            pass
        except:
            return "unknown"
```

---

### Box 3: **Model Benchmarker**
**Input:** Model name, SystemProfile
**Output:** ModelBenchmarkResults
**Responsibility:** Test model with various context/chunk sizes

```python
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
class ContextTest:
    """Single context size test result."""
    num_ctx: int
    avg_latency_ms: float
    success_rate: float
    memory_usage_mb: float
    quality_score: float  # Based on output validation


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
        profile: SystemProfile
    ) -> ModelBenchmarkResults:
        """
        Benchmark model with different settings.

        Args:
            model_name: Name of Ollama model
            profile: System profile for constraints

        Returns:
            Complete benchmark results with recommendations
        """
        # Test different context sizes
        context_tests = self._benchmark_context_sizes(
            model_name,
            profile,
            test_sizes=[2048, 4096, 8192, 16384, 32768]
        )

        # Test different chunk sizes
        chunk_tests = self._benchmark_chunk_sizes(
            model_name,
            profile,
            test_sizes=[50000, 100000, 200000, 400000]
        )

        # Determine optimal settings
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
        """Test different context window sizes."""
        results = []
        sample_code = self.sample_generator.generate_sample()

        for size in test_sizes:
            # Skip if size exceeds available memory
            estimated_memory = self._estimate_memory_usage(size)
            if estimated_memory > profile.available_ram_gb * 0.8:
                continue

            # Run 3 tests and average
            latencies = []
            successes = 0
            memory_usages = []

            for _ in range(3):
                start = time.time()
                memory_before = self._get_memory_usage()

                try:
                    response = self.client.generate(
                        model=model_name,
                        prompt=sample_code,
                        options={"num_ctx": size}
                    )
                    latencies.append((time.time() - start) * 1000)
                    successes += 1

                    memory_after = self._get_memory_usage()
                    memory_usages.append(memory_after - memory_before)
                except:
                    pass

            if latencies:
                results.append(ContextTest(
                    num_ctx=size,
                    avg_latency_ms=sum(latencies) / len(latencies),
                    success_rate=successes / 3.0,
                    memory_usage_mb=sum(memory_usages) / len(memory_usages),
                    quality_score=self._evaluate_quality(response)
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
        # Filter successful tests
        good_tests = [t for t in tests if t.success_rate >= 0.9]

        if not good_tests:
            return 8192  # Safe default

        # Memory budget: 50% of available RAM
        memory_budget = profile.available_ram_gb * 512  # MB

        # Filter by memory
        memory_ok = [t for t in good_tests if t.memory_usage_mb < memory_budget]

        if not memory_ok:
            # Use smallest that worked
            return min(t.num_ctx for t in good_tests)

        # Sort by context size (largest first)
        sorted_tests = sorted(memory_ok, key=lambda t: t.num_ctx, reverse=True)

        # Find best balance
        baseline_latency = sorted_tests[-1].avg_latency_ms

        for test in sorted_tests:
            latency_increase = (test.avg_latency_ms - baseline_latency) / baseline_latency

            # Accept up to 20% latency increase for larger context
            if latency_increase <= 0.20:
                return test.num_ctx

        return sorted_tests[-1].num_ctx
```

---

### Box 4: **Latency Benchmarker**
**Input:** SystemProfile, ModelBenchmarkResults
**Output:** LatencyBenchmarkResults
**Responsibility:** Find optimal retry and timeout settings

```python
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


class LatencyBenchmarker:
    """
    Box: Latency Benchmarker

    Input: SystemProfile, ModelBenchmarkResults
    Output: LatencyBenchmarkResults
    Responsibility: Determine optimal timeout and retry settings
    """

    def benchmark_latency(
        self,
        model_name: str,
        num_ctx: int,
        sample_count: int = 10
    ) -> LatencyBenchmarkResults:
        """
        Benchmark request latencies.

        Args:
            model_name: Model to test
            num_ctx: Context size to use
            sample_count: Number of test requests

        Returns:
            Latency statistics and recommendations
        """
        latencies = []
        errors = 0

        sample_code = self.sample_generator.generate_sample()

        for i in range(sample_count):
            start = time.time()

            try:
                response = self.client.generate(
                    model=model_name,
                    prompt=sample_code,
                    options={"num_ctx": num_ctx}
                )
                latency = (time.time() - start) * 1000
                latencies.append(latency)
            except:
                errors += 1

        if not latencies:
            # All failed - use conservative defaults
            return LatencyBenchmarkResults(
                avg_request_latency_ms=30000,
                p50_latency_ms=30000,
                p95_latency_ms=60000,
                p99_latency_ms=120000,
                optimal_timeout_seconds=180,
                optimal_retry_attempts=5,
                optimal_backoff_seconds=2.0,
                error_rate=1.0
            )

        latencies.sort()

        return LatencyBenchmarkResults(
            avg_request_latency_ms=sum(latencies) / len(latencies),
            p50_latency_ms=latencies[len(latencies) // 2],
            p95_latency_ms=latencies[int(len(latencies) * 0.95)],
            p99_latency_ms=latencies[int(len(latencies) * 0.99)],
            optimal_timeout_seconds=self._calculate_timeout(latencies),
            optimal_retry_attempts=self._calculate_retries(errors, sample_count),
            optimal_backoff_seconds=self._calculate_backoff(latencies),
            error_rate=errors / sample_count
        )

    def _calculate_timeout(self, latencies: List[float]) -> int:
        """
        Calculate optimal timeout.

        Strategy: 3x the P99 latency, minimum 60s
        """
        if not latencies:
            return 180

        p99 = latencies[int(len(latencies) * 0.99)]
        timeout = int((p99 / 1000) * 3)

        return max(60, min(300, timeout))  # Clamp to 60-300s

    def _calculate_retries(self, errors: int, total: int) -> int:
        """
        Calculate optimal retry attempts.

        Strategy:
        - No errors: 2 retries (for occasional failures)
        - Some errors: 3-5 retries based on error rate
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
            return 7  # High error rate - more retries

    def _calculate_backoff(self, latencies: List[float]) -> float:
        """
        Calculate initial backoff duration.

        Strategy: 10% of average latency, minimum 0.5s
        """
        if not latencies:
            return 1.0

        avg_latency_s = sum(latencies) / len(latencies) / 1000
        backoff = avg_latency_s * 0.1

        return max(0.5, min(5.0, backoff))  # Clamp to 0.5-5s
```

---

### Box 5: **Throughput Benchmarker**
**Input:** SystemProfile, LatencyBenchmarkResults
**Output:** ThroughputBenchmarkResults
**Responsibility:** Find optimal parallel and delay settings

```python
@dataclass
class ThroughputBenchmarkResults:
    """Results from throughput benchmarking."""
    optimal_parallel_requests: int
    optimal_delay_seconds: float
    max_throughput_fps: float  # Files per second
    recommended_batch_size: int
    recommended_batch_delay: float


class ThroughputBenchmarker:
    """
    Box: Throughput Benchmarker

    Input: SystemProfile, LatencyBenchmarkResults
    Output: ThroughputBenchmarkResults
    Responsibility: Determine optimal concurrency and delay
    """

    def benchmark_throughput(
        self,
        profile: SystemProfile,
        latency_results: LatencyBenchmarkResults,
        model_name: str
    ) -> ThroughputBenchmarkResults:
        """
        Benchmark throughput with different concurrency levels.

        Tests:
        1. Sequential (1 at a time, no delay)
        2. Sequential with delay (0.5s, 1s, 2s)
        3. Parallel (2, 4, 8 concurrent)

        Returns:
            Optimal concurrency and delay settings
        """
        # Test sequential
        seq_results = self._test_sequential(model_name, delays=[0, 0.5, 1.0, 2.0])

        # Test parallel (if system has enough cores)
        parallel_results = []
        if profile.cpu_threads >= 4:
            parallel_levels = [2, 4, min(8, profile.cpu_threads)]
            parallel_results = self._test_parallel(model_name, parallel_levels)

        # Find optimal configuration
        all_results = seq_results + parallel_results
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
        delays: List[float]
    ) -> List[ThroughputTest]:
        """Test sequential processing with different delays."""
        results = []
        sample_code = self.sample_generator.generate_sample()

        for delay in delays:
            start = time.time()

            for i in range(5):  # Process 5 files
                self.client.generate(
                    model=model_name,
                    prompt=sample_code,
                    options={"num_ctx": self.num_ctx}
                )

                if delay > 0 and i < 4:  # Don't delay after last
                    time.sleep(delay)

            duration = time.time() - start
            throughput = 5 / duration

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
        levels: List[int]
    ) -> List[ThroughputTest]:
        """Test parallel processing at different concurrency levels."""
        from concurrent.futures import ThreadPoolExecutor

        results = []
        sample_code = self.sample_generator.generate_sample()

        for parallel_count in levels:
            start = time.time()

            def process_one():
                return self.client.generate(
                    model=model_name,
                    prompt=sample_code,
                    options={"num_ctx": self.num_ctx}
                )

            with ThreadPoolExecutor(max_workers=parallel_count) as executor:
                futures = [executor.submit(process_one) for _ in range(10)]
                for future in futures:
                    future.result()

            duration = time.time() - start
            throughput = 10 / duration

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
        Calculate recommended batch size.

        Strategy:
        - For parallel: larger batches (50-100)
        - For sequential: smaller batches (10-20)
        - Scale based on available RAM
        """
        if best.parallel > 1:
            base_size = 50
        else:
            base_size = 10

        # Scale by available RAM (more RAM = larger batches)
        memory_factor = min(2.0, profile.available_ram_gb / 8.0)

        return int(base_size * memory_factor)
```

---

### Box 6: **Sample Code Generator**
**Input:** None
**Output:** Sample code strings
**Responsibility:** Generate realistic code samples for benchmarking

```python
class SampleCodeGenerator:
    """
    Box: Sample Code Generator

    Input: None
    Output: Sample code for testing
    Responsibility: Generate realistic code samples
    """

    SAMPLES = [
        # Small sample (~500 chars)
        '''def calculate_total(items):
    """Calculate total with tax."""
    subtotal = sum(item.price for item in items)
    return subtotal * 1.08
''',
        # Medium sample (~2000 chars)
        '''class DataProcessor:
    """Process data with validation."""

    def __init__(self, config):
        self.config = config
        self.cache = {}

    def process(self, data):
        if not self.validate(data):
            raise ValueError("Invalid data")

        result = self.transform(data)
        self.cache[data.id] = result
        return result

    def validate(self, data):
        return hasattr(data, 'id') and hasattr(data, 'value')

    def transform(self, data):
        return {
            'id': data.id,
            'value': data.value * self.config.multiplier,
            'timestamp': datetime.now()
        }
''',
        # Large sample (~5000 chars)
        '''class ComplexSystem:
    """A complex system with multiple components."""

    def __init__(self):
        self.database = DatabaseConnection()
        self.cache = CacheLayer()
        self.validator = DataValidator()
        self.processor = DataProcessor()
        self.logger = Logger()

    async def process_request(self, request):
        """Process incoming request with full pipeline."""
        try:
            # Validate input
            if not self.validator.validate(request):
                self.logger.warning(f"Invalid request: {request}")
                return {"error": "validation_failed"}

            # Check cache
            cache_key = self._generate_cache_key(request)
            if cached := await self.cache.get(cache_key):
                self.logger.info(f"Cache hit: {cache_key}")
                return cached

            # Process request
            data = await self.database.fetch(request.id)
            processed = self.processor.transform(data)

            # Store in cache
            await self.cache.set(cache_key, processed, ttl=3600)

            self.logger.info(f"Request processed: {request.id}")
            return processed

        except Exception as e:
            self.logger.error(f"Processing failed: {e}")
            raise

    def _generate_cache_key(self, request):
        return f"{request.type}:{request.id}:{request.version}"
'''
    ]

    def generate_sample(self, size: str = "medium") -> str:
        """
        Generate a sample code string.

        Args:
            size: "small", "medium", or "large"

        Returns:
            Sample code string
        """
        size_map = {
            "small": 0,
            "medium": 1,
            "large": 2
        }

        idx = size_map.get(size, 1)
        return self.SAMPLES[idx]
```

---

### Box 7: **Optimized Config Builder**
**Input:** All benchmark results
**Output:** Complete optimized configuration
**Responsibility:** Aggregate results and build final config

```python
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
    benchmark_date: str
    system_profile: SystemProfile
    confidence_score: float  # 0-100


class OptimizedConfigBuilder:
    """
    Box: Optimized Config Builder

    Input: All benchmark results
    Output: OptimizedConfig
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
        return OptimizedConfig(
            # Model settings
            model_name=model_results.model_name,
            num_ctx=model_results.optimal_num_ctx,
            temperature=model_results.optimal_temperature,
            chunk_size=model_results.optimal_chunk_size,
            max_content_length=model_results.optimal_max_content_length,
            max_chunk_summary_length=model_results.optimal_chunk_size // 25,

            # Performance settings
            request_delay_seconds=throughput_results.optimal_delay_seconds,
            max_concurrent_requests=throughput_results.optimal_parallel_requests,
            retry_attempts=latency_results.optimal_retry_attempts,
            initial_backoff_seconds=latency_results.optimal_backoff_seconds,
            backoff_multiplier=2.0,  # Standard exponential backoff
            request_timeout_seconds=latency_results.optimal_timeout_seconds,

            # Batch settings
            batch_size=throughput_results.recommended_batch_size,
            batch_delay_seconds=throughput_results.recommended_batch_delay,

            # Metadata
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
        - High success rates = higher confidence
        - Low error rates = higher confidence
        - Consistent latencies = higher confidence
        - More test samples = higher confidence
        """
        confidence = 100.0

        # Penalize for high error rate
        if latency_results.error_rate > 0:
            confidence -= latency_results.error_rate * 30

        # Penalize for inconsistent latencies (high variance)
        if latency_results.p99_latency_ms > latency_results.p50_latency_ms * 3:
            confidence -= 10

        # Penalize if optimal settings hit system limits
        if model_results.optimal_num_ctx >= 32768:
            confidence -= 5  # Might be limited by model, not optimal

        return max(0, min(100, confidence))
```

---

## 🎮 CLI Interface

### Command: `ralf-notes fine-tune`

```python
@app.command()
def fine_tune(
    quick: bool = typer.Option(
        False,
        "--quick",
        help="Quick tune (fewer tests, faster)"
    ),
    full: bool = typer.Option(
        False,
        "--full",
        help="Full comprehensive tuning (more tests, slower)"
    ),
    save: bool = typer.Option(
        True,
        "--save/--no-save",
        help="Save results to config file"
    ),
    report: bool = typer.Option(
        True,
        "--report/--no-report",
        help="Show detailed report"
    )
):
    """
    Automatically tune RALF Note for optimal performance on this system.

    This will:
    - Profile your system (CPU, RAM, GPU, Ollama)
    - Benchmark your model with different settings
    - Find optimal context size, chunk size, and performance settings
    - Save optimized configuration

    Duration:
    - Quick mode: 2-5 minutes
    - Normal mode: 5-10 minutes
    - Full mode: 10-20 minutes
    """
    console = Console()
    config_manager = ConfigManager()

    console.print("")
    console.rule("🔧 RALF Note Auto-Tuning System", style="bold cyan")
    console.print("")

    # Initialize components
    system_profiler = SystemProfiler()
    sample_generator = SampleCodeGenerator()

    client = Client(host=config_manager.get("ollama_host"))

    model_benchmarker = ModelBenchmarker(client, sample_generator)
    latency_benchmarker = LatencyBenchmarker(client, sample_generator)
    throughput_benchmarker = ThroughputBenchmarker(client, sample_generator)
    config_builder = OptimizedConfigBuilder()

    orchestrator = BenchmarkOrchestrator(
        config_manager=config_manager,
        system_profiler=system_profiler,
        model_benchmarker=model_benchmarker,
        latency_benchmarker=latency_benchmarker,
        throughput_benchmarker=throughput_benchmarker,
        console=console
    )

    # Set benchmark intensity
    if quick:
        benchmark_config = BenchmarkConfig(intensity="quick")
    elif full:
        benchmark_config = BenchmarkConfig(intensity="full")
    else:
        benchmark_config = BenchmarkConfig(intensity="normal")

    # Run benchmarks
    try:
        with console.status("Running benchmarks..."):
            optimized = orchestrator.run_full_benchmark(benchmark_config)

        console.print("")
        console.rule("✅ Tuning Complete", style="bold green")
        console.print("")

        # Show report
        if report:
            display_tuning_report(console, optimized)

        # Save to config
        if save:
            if typer.confirm("\nSave optimized settings to config?"):
                save_optimized_config(config_manager, optimized)
                console.success("Configuration updated!")
                console.info(f"Confidence: {optimized.confidence_score:.1f}%")

    except Exception as e:
        console.error(f"Tuning failed: {e}")
        raise typer.Exit(1)
```

---

## 📊 Output Report

```python
def display_tuning_report(console: Console, config: OptimizedConfig):
    """Display comprehensive tuning report."""

    # System Profile
    console.panel(
        f"""CPU: {config.system_profile.cpu_cores} cores / {config.system_profile.cpu_threads} threads
RAM: {config.system_profile.available_ram_gb:.1f} GB available / {config.system_profile.total_ram_gb:.1f} GB total
GPU: {"Yes" if config.system_profile.has_gpu else "No"}
Ollama: {config.system_profile.ollama_version} @ {config.system_profile.ollama_host}""",
        title="💻 System Profile",
        style="cyan"
    )

    console.print("")

    # Optimized Settings
    console.panel(
        f"""Model: {config.model_name}
Context Size: {config.num_ctx}
Chunk Size: {config.chunk_size}
Temperature: {config.temperature}
Max Content Length: {config.max_content_length}""",
        title="🤖 Model Settings",
        style="green"
    )

    console.print("")

    console.panel(
        f"""Parallel Requests: {config.max_concurrent_requests}
Request Delay: {config.request_delay_seconds}s
Timeout: {config.request_timeout_seconds}s
Retry Attempts: {config.retry_attempts}
Backoff: {config.initial_backoff_seconds}s × {config.backoff_multiplier}""",
        title="⚡ Performance Settings",
        style="magenta"
    )

    console.print("")

    console.panel(
        f"""Batch Size: {config.batch_size} files
Batch Delay: {config.batch_delay_seconds}s
Estimated Throughput: {estimate_throughput(config):.2f} files/min""",
        title="📦 Batch Settings",
        style="yellow"
    )

    console.print("")
    console.info(f"Confidence Score: {config.confidence_score:.1f}%")
    console.info(f"Benchmarked: {config.benchmark_date}")
```

---

## 📁 File Structure

```
ralf_notes/
├── tuning/
│   ├── __init__.py
│   ├── orchestrator.py          # BenchmarkOrchestrator
│   ├── system_profiler.py       # SystemProfiler
│   ├── model_benchmarker.py     # ModelBenchmarker
│   ├── latency_benchmarker.py   # LatencyBenchmarker
│   ├── throughput_benchmarker.py # ThroughputBenchmarker
│   ├── sample_generator.py      # SampleCodeGenerator
│   ├── config_builder.py        # OptimizedConfigBuilder
│   └── models.py                # All dataclasses
```

---

## 🎯 Implementation Phases

### Phase 1: Core Infrastructure (2-3 hours)
- [ ] Create tuning package structure
- [ ] Implement all dataclasses (models.py)
- [ ] Create SystemProfiler
- [ ] Create SampleCodeGenerator

### Phase 2: Model Benchmarking (3-4 hours)
- [ ] Implement ModelBenchmarker
- [ ] Context size testing
- [ ] Chunk size testing
- [ ] Quality scoring

### Phase 3: Performance Benchmarking (3-4 hours)
- [ ] Implement LatencyBenchmarker
- [ ] Implement ThroughputBenchmarker
- [ ] Sequential vs parallel testing

### Phase 4: Integration (2-3 hours)
- [ ] Implement BenchmarkOrchestrator
- [ ] Implement OptimizedConfigBuilder
- [ ] Create CLI command
- [ ] Create report display

### Phase 5: Testing & Polish (2-3 hours)
- [ ] Test on different systems
- [ ] Validate recommendations
- [ ] Add error handling
- [ ] Documentation

**Total Estimated Time:** 12-17 hours

---

## ✅ Benefits

1. **Automatic Optimization**
   - No manual configuration needed
   - Adapts to each system automatically
   - Continuous improvement

2. **System-Aware**
   - Respects hardware limits
   - Optimizes for available resources
   - Prevents overload

3. **Evidence-Based**
   - Actual benchmarks, not guesses
   - Confidence scores
   - Transparent results

4. **User-Friendly**
   - Simple command: `ralf-notes fine-tune`
   - Clear reports
   - One-click apply

5. **Professional**
   - Follows best practices
   - OOP + Boxes methodology
   - Maintainable code

---

## 🚀 Usage Examples

```bash
# Quick tune (2-5 minutes)
ralf-notes fine-tune --quick

# Normal tune (5-10 minutes) - recommended
ralf-notes fine-tune

# Full comprehensive tune (10-20 minutes)
ralf-notes fine-tune --full

# Tune and show report without saving
ralf-notes fine-tune --no-save

# Tune quietly and auto-save
ralf-notes fine-tune --no-report --save
```

---

## 📈 Expected Results

### Low-End System (4 cores, 8GB RAM)
```
Optimal Settings:
- num_ctx: 4096
- parallel: 1
- delay: 0.5s
- batch_size: 10
- timeout: 120s
Estimated: 2-3 files/min
```

### Mid-Range System (8 cores, 16GB RAM)
```
Optimal Settings:
- num_ctx: 8192
- parallel: 2
- delay: 0.2s
- batch_size: 25
- timeout: 90s
Estimated: 4-6 files/min
```

### High-End System (16+ cores, 32GB+ RAM, GPU)
```
Optimal Settings:
- num_ctx: 16384
- parallel: 4
- delay: 0s
- batch_size: 50
- timeout: 60s
Estimated: 8-12 files/min
```

---

## ✨ Future Enhancements

1. **Adaptive Tuning**
   - Re-tune automatically when performance degrades
   - Learn from actual usage patterns

2. **Profile Management**
   - Save multiple profiles (fast, balanced, quality)
   - Switch profiles easily

3. **Cloud Integration**
   - Share anonymized benchmarks
   - Get crowd-sourced recommendations

4. **Monitoring**
   - Track performance over time
   - Alert when settings become suboptimal

---

**This is a complete, production-ready design following boxes methodology and OOP principles. Ready for implementation!** 🎯
