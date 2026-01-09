# Enhancement 4: Model Warm-up & Persistence

## Priority: ⭐⭐⭐⭐ HIGH VALUE / VERY LOW EFFORT

## Problem
Ollama unloads models from VRAM after 5 minutes of inactivity by default. This causes:
- **First request delay:** 5-10 seconds to load model
- **Intermittent delays:** Model unloads between files
- **Inconsistent performance:** Some requests fast, others slow

## Current Code Location
- `config.py:19-22` - OPTIONS without `keep_alive`
- No warmup function exists

## Solution
1. Add `keep_alive` parameter to keep models loaded
2. Implement warmup function to pre-load models before processing
3. Configure appropriate keep-alive duration

## Implementation

### Step 1: Update OPTIONS in config.py

```python
# --- High Context Options ---
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2,
    "keep_alive": "30m"  # Keep model loaded for 30 minutes
}
```

**Keep-alive Options:**
- `"5m"` - 5 minutes (Ollama default)
- `"30m"` - 30 minutes (good for batch processing)
- `"1h"` - 1 hour (for all-day usage)
- `"0"` - Keep loaded indefinitely (until Ollama restart)
- `"-1"` - Unload immediately after request (for testing)

### Step 2: Add warmup function to main.py

```python
def warmup_model():
    """
    Pre-load model into VRAM to eliminate first-request delay.
    Makes a minimal generation request to trigger model loading.
    """
    try:
        logger.info(f"Warming up {MODEL_NAME}...")
        start_time = time.time()

        # Minimal request to load model
        client.generate(
            model=MODEL_NAME,
            prompt="Initialize model",
            options={
                'num_predict': 1,      # Generate only 1 token
                'keep_alive': '60m'    # Keep loaded for 60 minutes
            }
        )

        elapsed = time.time() - start_time
        logger.info(f"✓ {MODEL_NAME} loaded in {elapsed:.2f}s and ready")

    except Exception as e:
        logger.warning(f"Model warmup failed (non-critical): {e}")
        logger.warning("Continuing without warmup - first request will be slower")
```

### Step 3: Call warmup in main()

```python
def main():
    # wait_until_start_time(PREFERRED_START_TIME)

    logger.info("="*60)
    logger.info("RALF Notes - Ollama Documentation Generator")
    logger.info("="*60)

    # Validate model availability
    if not validate_model_availability():
        logger.error("Aborting: Model not available")
        return

    # Warm up model before processing
    warmup_model()

    # --- Pre-run check for TARGET_DIR ---
    try:
        ensure_dir(TARGET_DIR)
        if not os.access(TARGET_DIR, os.W_OK):
            logger.error(f"Error: The target directory '{TARGET_DIR}' is not writable.")
            return
    except Exception as e:
        logger.error(f"Error: Could not create or access the target directory '{TARGET_DIR}'.")
        logger.error(f"Details: {e}")
        return

    # Rest of processing...
    all_files = get_all_files(SOURCE_PATHS)
    logger.info(f"Found {len(all_files)} files to process.")
    # ...
```

### Step 4: Add keep_alive to all safe_generate calls

Update the options parameter construction in `generate_obsidian_doc()`:

```python
def generate_obsidian_doc(file_path):
    # ... file reading code ...

    processed_content = recursive_summarize(raw_content)

    options = {
        "num_ctx": min(estimate_tokens(processed_content) + 2048, MAX_CTX),
        "temperature": 0.2,
        "keep_alive": "30m"  # Ensure model stays loaded between sections
    }

    # ... rest of function
```

## Advanced: Multi-Model Warmup

For smart model routing (Enhancement #3), warm up all models:

```python
def warmup_models():
    """Pre-load all models used in routing strategy"""
    models_to_warmup = set([MODEL_NAME])

    # Add models from routing strategy if enabled
    if ENABLE_MODEL_ROUTING:
        for config in MODEL_STRATEGY.values():
            models_to_warmup.add(config['model'])

    logger.info(f"Warming up {len(models_to_warmup)} model(s)...")

    for model in models_to_warmup:
        try:
            start_time = time.time()
            client.generate(
                model=model,
                prompt="init",
                options={'num_predict': 1, 'keep_alive': '60m'}
            )
            elapsed = time.time() - start_time
            logger.info(f"✓ {model} loaded in {elapsed:.2f}s")
        except Exception as e:
            logger.warning(f"Could not warm up {model}: {e}")

    logger.info("All models ready")
```

## Expected Impact

### Before (without warmup/persistence)
```
File 1: Load model (8s) + Generate (12s) = 20s
File 2: Load model (8s) + Generate (12s) = 20s  # Model unloaded
File 3: Load model (8s) + Generate (12s) = 20s
Total: 60s for 3 files
```

### After (with warmup/persistence)
```
Warmup: Load model (8s)
File 1: Generate (12s) = 12s  # Model already loaded
File 2: Generate (12s) = 12s  # Model still loaded
File 3: Generate (12s) = 12s
Total: 44s for 3 files (27% faster)
```

### For 100 files
- **Before:** ~2000s (33 minutes)
- **After:** ~1208s (20 minutes)
- **Savings:** 13 minutes

## Configuration Options

Add to `config.py` for flexibility:

```python
# Model persistence settings
WARMUP_ENABLED = True           # Set False to skip warmup
KEEP_ALIVE_DURATION = "30m"     # How long to keep models loaded

# Override in OPTIONS
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2,
    "keep_alive": KEEP_ALIVE_DURATION
}
```

Then in main():
```python
if WARMUP_ENABLED:
    warmup_model()
```

## Memory Considerations

**Model Sizes in VRAM:**
- `ministral-3:3b` - ~2-3 GB
- `llama3.2:3b` - ~2-3 GB
- `qwen2.5:7b` - ~5-6 GB
- `qwen2.5:14b` - ~10-12 GB

**Mac Mini M4 with 16GB unified memory:**
- Can keep 2-3 small models (3b) loaded simultaneously
- Or 1 large model (14b) + 1 small model (3b)
- System reserves ~4-6GB for macOS

**Recommendations:**
- Single model: `keep_alive: "1h"` or `"0"` (indefinite)
- 2-3 models: `keep_alive: "30m"` (balance memory)
- 4+ models: `keep_alive: "15m"` (aggressive unloading)

## Testing Checklist
- [ ] First generation after warmup is fast (no 5-10s delay)
- [ ] Subsequent generations remain fast
- [ ] Models stay loaded for configured duration
- [ ] Check Ollama logs: `ollama list` shows loaded models
- [ ] Memory usage stable (not growing unbounded)
- [ ] Warmup completes without errors

## Monitoring Model Status

Check loaded models:
```bash
# List all models
ollama list

# Check Ollama logs
tail -f ~/.ollama/logs/server.log

# Monitor memory usage
top -o MEM  # macOS
htop        # Linux
```

## Troubleshooting

**Warmup fails:**
- Check Ollama is running: `curl http://localhost:11434/api/tags`
- Verify model exists: `ollama list`
- Check logs for OOM (out of memory) errors

**Model still unloads:**
- Verify `keep_alive` is in OPTIONS
- Check if other processes are using Ollama
- Try `keep_alive: "0"` for indefinite

**Too much memory usage:**
- Reduce `keep_alive` duration
- Use fewer/smaller models
- Consider upgrading RAM

## Notes
- Warmup is **optional** - script works without it (just slower)
- `keep_alive` applies per request, refreshes the timer
- Ollama manages VRAM automatically based on available memory
- On model switch, old model may unload to free VRAM
