# Design Document: `fine-tune` Command Enhancements

This document outlines the research and design for optimizing the `fine-tune` command as requested.

---

## 1. Optimizing `--quick`, `normal`, and `--full` Modes

The goal is to make a meaningful trade-off between speed and accuracy for each tuning mode. This will be controlled by a `BenchmarkConfig` object passed through the orchestrator to each benchmarker.

### Proposed Changes:

#### `ralf_notes/cli.py` (`fine_tune` command)
The `fine-tune` command will create a `BenchmarkConfig` based on the user's flag.

```python
# Inside the fine_tune command
if quick:
    benchmark_config = BenchmarkConfig(intensity="quick")
elif full:
    benchmark_config = BenchmarkConfig(intensity="full")
else:
    benchmark_config = BenchmarkConfig(intensity="normal") # Default

# Pass this config to the orchestrator
optimized = orchestrator.run_full_benchmark(benchmark_config)
```

#### Benchmark Implementations (`ModelBenchmarker`, `LatencyBenchmarker`, etc.)
Each benchmarker will adjust its behavior based on the `intensity` in the `BenchmarkConfig`.

**Example: `LatencyBenchmarker`**
```python
# In LatencyBenchmarker.benchmark_latency
intensity_map = {
    "quick": 5,
    "normal": 10,
    "full": 20
}
sample_count = intensity_map.get(benchmark_config.intensity, 10)

for i in range(sample_count):
    # ... run test
```

**Example: `ModelBenchmarker`**
```python
# In ModelBenchmarker.benchmark_model
if benchmark_config.intensity == "quick":
    test_sizes = [4096, 8192]
elif benchmark_config.intensity == "full":
    test_sizes = [2048, 4096, 6144, 8192, 12288, 16384, 32768]
else: # normal
    test_sizes = [4096, 8192, 16384]

context_tests = self._benchmark_context_sizes(
    model_name,
    profile,
    test_sizes=test_sizes
)
```

This design allows for a clear and controllable difference between the tuning modes, giving the user a real choice between a quick check and a deep, comprehensive analysis.

---

## 2. Enhancing Result Display

The current table display is good, but it can be made more informative.

### Proposed Enhancements:

#### a. Show "Before" and "After" Comparison
When displaying the final report, we can show the original configuration value next to the new, optimized value. This gives the user immediate feedback on what has changed.

**Example `display_tuning_report` modification:**
```python
# In display_tuning_report, before generating the panel
old_config = config_manager.config

# In the panel content
f"""Model: [dim]{old_config.get('model_name')}[/dim] -> [bold]{config.model_name}[/bold]
Context Size: [dim]{old_config.get('num_ctx')}[/dim] -> [bold]{config.num_ctx}[/bold]
..."""
```

#### b. Explain the Confidence Score
Add a small note to the report explaining what the confidence score means.

**Example:**
```
ℹ️  Confidence Score: 85.0%
   (This score reflects the consistency of benchmark results and whether settings hit system limits.)
```

#### c. Save Report to File
Add a `--save-report` flag to the `fine-tune` command. If used, the final report would be saved as a formatted Markdown file (e.g., `ralf-tuning-report-YYYY-MM-DD.md`) in the current directory.

---

## 3. Default System Settings

The application needs a sensible default configuration for users who have not yet run the `fine-tune` command.

### Current Approach:
The default settings are defined in `ralf_notes/config_manager.py` inside the `DEFAULT_CONFIG` dictionary.

```python
class ConfigManager:
    DEFAULT_CONFIG = {
        "source_paths": [],
        "target_dir": "./to_obsidian",
        "model_name": "ministral-3:3b",
        "ollama_host": "http://127.0.0.1:11434",
        "temperature": 0.1,
        "num_ctx": 10000,
        "chunk_size": 100000
    }
```

### Rationale for Defaults:
- **`model_name: "ministral-3:3b"`:** This is a good default as it's a small, fast, and popular model that is likely to work on a wide range of systems.
- **`num_ctx: 10000`:** This is a reasonably large context size that modern models can handle, but it's not so large that it will cause memory issues on lower-end systems.
- **`temperature: 0.1`:** A low temperature is crucial for ensuring consistent, predictable JSON output from the model.
- **Other values (`chunk_size`, etc.):** These are chosen as safe, middle-of-the-road values that provide a good balance between performance and resource usage.

The purpose of these defaults is **"it just works"** out of the box for the average user. The `fine-tune` command then allows users to move from these "good enough" defaults to settings that are **optimal** for their specific hardware and model.

---

## 4. Persisting and Using Optimized Settings

This is a critical part of the `fine-tune` feature and is already implemented correctly. Here is a breakdown of how it works:

### a. Persisting the Settings
1.  After the benchmarks are complete, the `fine-tune` command in `cli.py` has the results in an `OptimizedConfig` object.
2.  If the user confirms `y` to save (or if `--save` is used without `--no-report`), the `save_optimized_config` function is called.
3.  This function iterates through the fields of the `OptimizedConfig` object and calls `config_manager.set("key", value)` for each one. This updates the configuration in memory.
4.  Finally, `config_manager.save()` is called. This method writes the entire in-memory configuration dictionary to the `~/.ralf-notes/config.json` file on the user's disk, overwriting the old settings with the new, optimized ones.

### b. Using the Settings
1.  When any command that needs configuration (like `ralf-notes generate`) is run, the first thing it does is create an instance of the `ConfigManager` class.
2.  The `ConfigManager.__init__` method immediately loads the `~/.ralf-notes/config.json` file into its internal `self.config` dictionary.
3.  When the application needs a setting, it calls `config_manager.get("setting_name")`. This retrieves the value from the dictionary that was just loaded from the file.

This ensures that once the `fine-tune` command saves the new settings, **every subsequent run of any `ralf-notes` command will automatically use the optimized configuration**. The user does not need to do anything extra; the optimized settings become the new default.
