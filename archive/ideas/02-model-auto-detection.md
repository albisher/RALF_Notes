# Enhancement 2: Model Auto-Detection & Selection

## Priority: ⭐⭐⭐⭐ HIGH VALUE

## Problem
Currently, RALF Notes is hardcoded to a single model (`ministral-3:3b`) with a fixed context window (16K). This means:
- Can't leverage models with larger context windows (Llama 3.2 has 128K)
- No validation that the model exists in Ollama
- No adaptation to user's available models
- Manual config changes required to switch models

## Current Code Location
- `config.py:26` - Hardcoded `MODEL_NAME`
- `config.py:30` - Hardcoded `MAX_CTX`
- `main.py:50` - Client instantiation without validation

## Solution
Automatically detect available Ollama models and their capabilities, then configure accordingly.

## Implementation

### Step 1: Add model detection functions to main.py

```python
def get_available_models():
    """Fetch available Ollama models and their specs"""
    try:
        models_info = client.list()
        available = {}
        for model in models_info.get('models', []):
            available[model['name']] = {
                'size': model.get('size', 0),
                'family': model['name'].split(':')[0],
                'modified': model.get('modified_at', ''),
                'digest': model.get('digest', '')
            }
        return available
    except Exception as e:
        logger.warning(f"Could not fetch models from Ollama: {e}")
        return {}


def get_model_context_size(model_name):
    """Query Ollama for model's actual context window"""
    try:
        show_response = client.show(model_name)
        modelfile = show_response.get('modelfile', '')

        # Extract: PARAMETER num_ctx 128000
        import re
        match = re.search(r'num_ctx\s+(\d+)', modelfile)
        if match:
            ctx_size = int(match.group(1))
            logger.info(f"Detected {model_name} context: {ctx_size}")
            return ctx_size
    except Exception as e:
        logger.debug(f"Could not query {model_name} context size: {e}")

    # Fallback to known defaults
    KNOWN_CONTEXTS = {
        'llama3.2': 128000,
        'llama3.1': 128000,
        'llama3': 8192,
        'qwen2.5': 32768,
        'qwen2': 32768,
        'ministral': 128000,   # Native, but 16K practical on smaller hardware
        'mistral': 32768,
        'deepseek-coder': 16384,
        'codellama': 16384,
        'phi': 4096,
        'gemma': 8192,
    }

    for family, ctx in KNOWN_CONTEXTS.items():
        if family in model_name.lower():
            logger.info(f"Using known context for {model_name}: {ctx}")
            return ctx

    logger.warning(f"Unknown model {model_name}, using safe default 8192")
    return 8192  # Safe default


def validate_model_availability():
    """Verify configured model exists and is accessible"""
    available_models = get_available_models()

    if not available_models:
        logger.error("No Ollama models found! Is Ollama running?")
        logger.error(f"Attempting to connect to: {OLLAMA_HOST}")
        return False

    if MODEL_NAME not in available_models:
        logger.error(f"Model '{MODEL_NAME}' not found in Ollama")
        logger.error(f"Available models: {list(available_models.keys())}")
        logger.error(f"Please run: ollama pull {MODEL_NAME}")
        return False

    logger.info(f"✓ Model '{MODEL_NAME}' is available")
    model_info = available_models[MODEL_NAME]
    size_gb = model_info['size'] / (1024**3)
    logger.info(f"  Size: {size_gb:.2f} GB")
    logger.info(f"  Family: {model_info['family']}")

    return True


def get_optimal_context_size(model_name):
    """Get optimal context size based on model and hardware"""
    detected_ctx = get_model_context_size(model_name)

    # Practical limits based on hardware
    # M4 Mac Mini with 16GB RAM can handle ~32K effectively
    PRACTICAL_LIMITS = {
        'ministral-3:3b': 16384,    # Small model, but limited
        'llama3.2:3b': 32768,       # Larger context, still efficient
        'qwen2.5:7b': 32768,        # Larger model, cap at 32K
    }

    if model_name in PRACTICAL_LIMITS:
        practical = PRACTICAL_LIMITS[model_name]
        if detected_ctx > practical:
            logger.info(f"Capping {model_name} context from {detected_ctx} to {practical} for performance")
            return practical

    return detected_ctx
```

### Step 2: Update main() to validate and configure

```python
def main():
    # --- Model validation ---
    logger.info("="*60)
    logger.info("RALF Notes - Ollama Documentation Generator")
    logger.info("="*60)

    if not validate_model_availability():
        logger.error("Aborting: Model not available")
        return

    # Dynamically set context size
    global MAX_CTX
    MAX_CTX = get_optimal_context_size(MODEL_NAME)
    logger.info(f"Using context window: {MAX_CTX}")

    # Warm up model
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

    # Rest of existing main() logic...
    all_files = get_all_files(SOURCE_PATHS)
    logger.info(f"Found {len(all_files)} files to process.")
    # ... etc
```

### Step 3: Add warmup function

```python
def warmup_model():
    """Pre-load model into VRAM to eliminate first-request delay"""
    try:
        logger.info(f"Warming up {MODEL_NAME}...")
        client.generate(
            model=MODEL_NAME,
            prompt="Initialize",
            options={'num_predict': 1, 'keep_alive': '60m'}
        )
        logger.info(f"✓ {MODEL_NAME} loaded and ready")
    except Exception as e:
        logger.warning(f"Model warmup failed (non-critical): {e}")
```

### Step 4: Update config.py to be more flexible

```python
# --- Configuration ---
# Source directories to process
SOURCE_PATHS = ['/Users/amac/Documents/code/WindowCleanner/']

# Target directory for Obsidian notes
TARGET_DIR = '/Users/amac/Documents/code/Ralf_Notes/To_Obsidian/'

# Processing options
PREFERRED_START_TIME = "08:03"
OVERWRITE_EXISTING = False

# --- Ollama Configuration ---
OLLAMA_HOST = 'http://127.0.0.1:11434'
MODEL_NAME = 'ministral-3:3b'  # Will auto-detect capabilities

# Context settings (will be auto-adjusted based on model)
APPROX_LINES_FOR_FULL_CONTEXT = 500
TOKENS_PER_LINE_ESTIMATE = 15

# Initial options (MAX_CTX will be set dynamically)
OPTIONS = {
    "num_ctx": APPROX_LINES_FOR_FULL_CONTEXT * TOKENS_PER_LINE_ESTIMATE,
    "temperature": 0.2,
    "keep_alive": "30m"  # Keep model loaded
}

# Chunking (will be optimized based on detected context)
CHUNK_SIZE = 6000     # Default, will adjust if larger context available
MAX_CTX = 16384       # Will be overridden by auto-detection
```

## Expected Impact
- **Reliability:** Fails fast with helpful error messages if model missing
- **Flexibility:** Works with any Ollama model without code changes
- **Performance:** Automatically uses largest available context window
- **User Experience:** Clear feedback about model status and capabilities

## Configuration Options

Add to `config.py` for advanced users:

```python
# Advanced: Override auto-detection
AUTO_DETECT_CONTEXT = True  # Set False to use manual MAX_CTX

# Advanced: Preferred models (fallback chain)
PREFERRED_MODELS = [
    'qwen2.5:7b',      # Try quality model first
    'llama3.2:3b',     # Fall back to balanced
    'ministral-3:3b',  # Fall back to fast
]
```

## Testing Checklist
- [ ] Run with available model - should work normally
- [ ] Run with unavailable model - should fail with clear error
- [ ] Run with Ollama stopped - should fail with connection error
- [ ] Run with large context model (Llama 3.2) - should detect 128K
- [ ] Check logs for detected context size
- [ ] Verify warmup completes successfully

## Error Messages Examples

**Model not found:**
```
ERROR: Model 'ministral-3:3b' not found in Ollama
Available models: ['llama3.2:3b', 'qwen2.5:7b']
Please run: ollama pull ministral-3:3b
```

**Ollama not running:**
```
ERROR: No Ollama models found! Is Ollama running?
Attempting to connect to: http://127.0.0.1:11434
```

**Success:**
```
✓ Model 'ministral-3:3b' is available
  Size: 2.87 GB
  Family: ministral
Detected ministral-3:3b context: 128000
Capping ministral-3:3b context from 128000 to 16384 for performance
Using context window: 16384
Warming up ministral-3:3b...
✓ ministral-3:3b loaded and ready
```

## Notes
- Detection happens once at startup for efficiency
- Context size can be overridden in config if needed
- Warmup is optional (fails gracefully if it doesn't work)
- Model info is logged for debugging
