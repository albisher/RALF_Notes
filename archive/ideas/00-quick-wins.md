# Quick Wins - Immediate Actionable Changes

These are **5-minute changes** you can make right now to improve Ollama performance.

## Change 1: Add keep_alive to OPTIONS ⏱️ 1 minute

**File:** `config.py:19-22`

**Before:**
```python
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2
}
```

**After:**
```python
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2,
    "keep_alive": "30m"  # Keep model loaded for 30 minutes
}
```

**Impact:** Eliminates 5-10s model loading delay between files

---

## Change 2: Add Model Warmup Function ⏱️ 2 minutes

**File:** `main.py` (add after line 50)

```python
def warmup_model():
    """Pre-load model into VRAM to eliminate first-request delay"""
    try:
        logger.info(f"Warming up {MODEL_NAME}...")
        client.generate(
            model=MODEL_NAME,
            prompt="Initialize model",
            options={'num_predict': 1, 'keep_alive': '60m'}
        )
        logger.info(f"✓ {MODEL_NAME} loaded and ready")
    except Exception as e:
        logger.warning(f"Warmup failed (non-critical): {e}")
```

**Impact:** Eliminates 8-10s delay on first file

---

## Change 3: Call Warmup in main() ⏱️ 30 seconds

**File:** `main.py:617` (add after line 617)

**Before:**
```python
def main():
    # wait_until_start_time(PREFERRED_START_TIME)

    try:
        ensure_dir(TARGET_DIR)
```

**After:**
```python
def main():
    # wait_until_start_time(PREFERRED_START_TIME)

    warmup_model()  # ADD THIS LINE

    try:
        ensure_dir(TARGET_DIR)
```

**Impact:** Model ready before processing starts

---

## Change 4: Add Model Availability Check ⏱️ 2 minutes

**File:** `main.py` (add after line 50)

```python
def check_model_available():
    """Verify model exists in Ollama"""
    try:
        models = client.list()
        available = [m['name'] for m in models.get('models', [])]
        if MODEL_NAME not in available:
            logger.error(f"Model '{MODEL_NAME}' not found. Available: {available}")
            logger.error(f"Run: ollama pull {MODEL_NAME}")
            return False
        logger.info(f"✓ Model '{MODEL_NAME}' is available")
        return True
    except Exception as e:
        logger.error(f"Could not connect to Ollama: {e}")
        return False
```

**Impact:** Fail fast with helpful error instead of cryptic crash

---

## Change 5: Add Check to main() ⏱️ 30 seconds

**File:** `main.py:617` (update to)

```python
def main():
    # wait_until_start_time(PREFERRED_START_TIME)

    if not check_model_available():  # ADD THIS
        logger.error("Aborting: Model not available")
        return

    warmup_model()

    try:
        ensure_dir(TARGET_DIR)
```

**Impact:** Clear error messages for troubleshooting

---

## Complete Quickstart Implementation

Here's all 5 changes combined (copy-paste ready):

### Add to main.py (after line 50):

```python
def check_model_available():
    """Verify model exists in Ollama"""
    try:
        models = client.list()
        available = [m['name'] for m in models.get('models', [])]
        if MODEL_NAME not in available:
            logger.error(f"Model '{MODEL_NAME}' not found. Available: {available}")
            logger.error(f"Run: ollama pull {MODEL_NAME}")
            return False
        logger.info(f"✓ Model '{MODEL_NAME}' is available")
        return True
    except Exception as e:
        logger.error(f"Could not connect to Ollama: {e}")
        return False

def warmup_model():
    """Pre-load model into VRAM"""
    try:
        logger.info(f"Warming up {MODEL_NAME}...")
        client.generate(
            model=MODEL_NAME,
            prompt="init",
            options={'num_predict': 1, 'keep_alive': '60m'}
        )
        logger.info(f"✓ {MODEL_NAME} loaded and ready")
    except Exception as e:
        logger.warning(f"Warmup failed (non-critical): {e}")
```

### Update config.py (line 19-22):

```python
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2,
    "keep_alive": "30m"  # ADD THIS LINE
}
```

### Update main() (line 603):

```python
def main():
    # wait_until_start_time(PREFERRED_START_TIME)

    # ADD THESE 5 LINES
    if not check_model_available():
        logger.error("Aborting: Model not available")
        return

    warmup_model()

    # --- Pre-run check for TARGET_DIR ---
    try:
        ensure_dir(TARGET_DIR)
        # ... rest of function
```

---

## Expected Results

### Before Quick Wins:
```
File 1: Load model (8s) + Generate (12s) = 20s
File 2: Load model (8s) + Generate (12s) = 20s
File 3: Load model (8s) + Generate (12s) = 20s
Total: 60s for 3 files
```

### After Quick Wins:
```
Startup: Check model (0.5s) + Warmup (8s) = 8.5s
File 1: Generate (12s) = 12s
File 2: Generate (12s) = 12s
File 3: Generate (12s) = 12s
Total: 44.5s for 3 files (26% faster)
```

### For 100 files:
- **Before:** ~2000s (33 minutes)
- **After:** ~1208s (20 minutes)
- **Savings:** 13 minutes

---

## Testing

Run after changes:
```bash
python main.py
```

Expected output:
```
✓ Model 'ministral-3:3b' is available
Warming up ministral-3:3b...
✓ ministral-3:3b loaded and ready
Found 10 files to process.
[Processing begins immediately with no model load delay]
```

---

## Rollback

If issues occur, revert:
1. Remove `keep_alive` from OPTIONS
2. Remove `check_model_available()` function
3. Remove `warmup_model()` function
4. Remove calls from `main()`

---

## Next Steps

After these quick wins, consider:
- **Enhancement 1:** Parallel Section Generation (5-7x speedup)
- **Enhancement 7:** Response Caching (skip unchanged files)
- **Enhancement 2:** Model Auto-Detection (flexibility)
