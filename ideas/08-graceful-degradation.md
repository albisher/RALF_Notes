# Enhancement 8: Graceful Degradation & Fallback Chain

## Priority: ⭐⭐⭐ MEDIUM VALUE

## Problem
Single model failure stops entire pipeline:
- Model crashes or errors out
- Ollama service interruption
- Model too large for available VRAM
- Network issues (remote Ollama)

## Current Code Location
`main.py:95-126` - `safe_generate()` retries same model 3 times

## Solution
Implement fallback chain to try alternative models when primary fails.

## Implementation

### Step 1: Define fallback chain in config.py

```python
# Fallback chain configuration
# Models will be tried in order until one succeeds

FALLBACK_CHAIN = [
    'qwen2.5:7b',      # Primary: Quality model
    'llama3.2:3b',     # Fallback 1: Balanced
    'ministral-3:3b',  # Fallback 2: Fast/reliable
]

# Fallback behavior
FALLBACK_ENABLED = True
FALLBACK_MAX_ATTEMPTS_PER_MODEL = 2  # Retries per model in chain
```

### Step 2: Implement fallback logic in main.py

```python
def safe_generate_with_fallback(client, system=None, prompt=None, options=None, stream=True, prompt_type="UNKNOWN"):
    """
    Generate with fallback chain support.
    Tries models in FALLBACK_CHAIN order until one succeeds.
    """
    if not FALLBACK_ENABLED:
        # Use original logic without fallback
        return safe_generate(client, model=MODEL_NAME, system=system, prompt=prompt,
                           options=options, stream=stream, prompt_type=prompt_type)

    models_to_try = FALLBACK_CHAIN.copy()

    # Ensure primary model is first
    if MODEL_NAME not in models_to_try:
        models_to_try.insert(0, MODEL_NAME)

    last_error = None

    for model_index, model in enumerate(models_to_try):
        logger.info(f"Trying model {model_index + 1}/{len(models_to_try)}: {model}")

        for attempt in range(FALLBACK_MAX_ATTEMPTS_PER_MODEL):
            try:
                timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logger.info(f"PROMPT SENT [{prompt_type}] to {model} (attempt {attempt + 1})")

                kwargs = {"model": model, "prompt": prompt}
                if system: kwargs["system"] = system
                if options: kwargs["options"] = options
                kwargs["stream"] = stream

                if stream:
                    stream_resp = client.generate(**kwargs)
                    response = "".join(chunk['response'] for chunk in stream_resp)
                    logger.info(f"✓ RESPONSE RECEIVED from {model}")
                    return response
                else:
                    response = client.generate(**kwargs)['response']
                    logger.info(f"✓ RESPONSE RECEIVED from {model}")
                    return response

            except ResponseError as e:
                last_error = e
                logger.warning(f"Model {model} attempt {attempt + 1} failed: {e}")
                time.sleep(2 ** attempt)  # Exponential backoff

            except Exception as e:
                last_error = e
                logger.warning(f"Unexpected error with {model}: {e}")
                break  # Don't retry on unexpected errors

        logger.warning(f"Model {model} exhausted all {FALLBACK_MAX_ATTEMPTS_PER_MODEL} attempts")

    # All models in chain failed
    logger.error(f"All models in fallback chain failed for {prompt_type}")
    raise Exception(f"Fallback chain exhausted: {last_error}")


def safe_generate(client, model=None, system=None, prompt=None, options=None, stream=True, prompt_type="UNKNOWN"):
    """
    Original safe_generate for backward compatibility.
    Now delegates to fallback version.
    """
    return safe_generate_with_fallback(
        client,
        system=system,
        prompt=prompt,
        options=options,
        stream=stream,
        prompt_type=prompt_type
    )
```

### Step 3: Validate fallback chain on startup

```python
def validate_fallback_chain():
    """
    Check that at least one model in fallback chain is available.
    """
    if not FALLBACK_ENABLED:
        return True

    available_models = get_available_models()
    available_in_chain = [m for m in FALLBACK_CHAIN if m in available_models]

    if not available_in_chain:
        logger.error("Fallback chain enabled but NO models available!")
        logger.error(f"  Fallback chain: {FALLBACK_CHAIN}")
        logger.error(f"  Available models: {list(available_models.keys())}")
        return False

    logger.info(f"Fallback chain: {len(available_in_chain)}/{len(FALLBACK_CHAIN)} models available")
    for model in available_in_chain:
        logger.info(f"  ✓ {model}")

    return True


def main():
    logger.info("="*60)
    logger.info("RALF Notes - Ollama Documentation Generator")
    logger.info("="*60)

    # Validate primary model
    if not validate_model_availability():
        logger.error("Primary model not available")

        # Check if fallback available
        if FALLBACK_ENABLED and validate_fallback_chain():
            logger.warning("Continuing with fallback models...")
        else:
            logger.error("Aborting: No models available")
            return

    # Validate fallback chain
    if not validate_fallback_chain():
        logger.warning("Fallback chain validation failed, disabling fallback")
        global FALLBACK_ENABLED
        FALLBACK_ENABLED = False

    # ... rest of main ...
```

## Advanced: Per-Section Fallback Strategy

Different sections can use different fallback chains:

### config.py:
```python
# Section-specific fallback chains
SECTION_FALLBACK_CHAINS = {
    'SUMMARY_PROMPT': ['qwen2.5:7b', 'llama3.2:3b'],
    'DETAILS_PROMPT': ['qwen2.5:7b', 'llama3.2:3b'],
    'TAGS_PROMPT': ['ministral-3:3b', 'llama3.2:3b'],  # Fast models fine
    'TYPE_PROMPT': ['ministral-3:3b', 'llama3.2:3b'],
    'DEPENDENCY_GRAPH_PROMPT': ['qwen2.5:7b', 'deepseek-coder-v2:16b'],  # Prefer code models
    'SECURITY_RISKS_PROMPT': ['qwen2.5:7b', 'llama3.2:3b'],
}

# Default fallback if section not specified
DEFAULT_FALLBACK_CHAIN = FALLBACK_CHAIN
```

### main.py:
```python
def get_fallback_chain_for_section(prompt_type):
    """Get appropriate fallback chain for section"""
    return SECTION_FALLBACK_CHAINS.get(prompt_type, DEFAULT_FALLBACK_CHAIN)

def safe_generate_with_fallback(client, system=None, prompt=None, options=None, stream=True, prompt_type="UNKNOWN"):
    """Generate with section-specific fallback chain"""
    fallback_chain = get_fallback_chain_for_section(prompt_type)

    # ... rest of fallback logic using fallback_chain ...
```

## Expected Impact

### Reliability Improvement
**Before:**
- Single model failure = entire pipeline fails
- Must manually switch models and restart

**After:**
- Automatic failover to backup models
- Processing continues despite model issues
- Degraded quality better than no output

### Real-World Scenario
```
Processing 100 files:
- File 1-50: qwen2.5:7b works perfectly
- File 51: qwen2.5:7b crashes (VRAM issue)
  → Fallback to llama3.2:3b ✓
- File 52-100: llama3.2:3b completes successfully
Result: 100/100 files processed (vs. 50/100 without fallback)
```

## Configuration Examples

### Conservative (prefer reliability):
```python
FALLBACK_CHAIN = [
    'ministral-3:3b',   # Most reliable, smallest
    'llama3.2:3b',      # Backup
]
FALLBACK_MAX_ATTEMPTS_PER_MODEL = 3
```

### Aggressive (prefer quality):
```python
FALLBACK_CHAIN = [
    'qwen2.5:14b',      # Largest/best
    'qwen2.5:7b',       # Medium
    'llama3.2:3b',      # Small backup
    'ministral-3:3b',   # Emergency fallback
]
FALLBACK_MAX_ATTEMPTS_PER_MODEL = 1  # Don't waste time retrying
```

### Disabled:
```python
FALLBACK_ENABLED = False  # Use only MODEL_NAME
```

## Error Handling Strategy

```python
# Error classification for better fallback decisions
def classify_error(error):
    """Classify error type to decide retry vs. fallback"""
    error_str = str(error).lower()

    if 'out of memory' in error_str or 'oom' in error_str:
        return 'memory'  # Try smaller model

    if 'timeout' in error_str or 'connection' in error_str:
        return 'network'  # Retry same model

    if 'not found' in error_str or 'unavailable' in error_str:
        return 'unavailable'  # Try different model

    return 'unknown'  # Generic retry


def should_retry_same_model(error):
    """Determine if error is transient (retry) or permanent (fallback)"""
    error_type = classify_error(error)

    if error_type == 'network':
        return True  # Transient, retry

    if error_type in ['memory', 'unavailable']:
        return False  # Permanent, fallback

    return True  # Default: retry
```

## Monitoring & Logging

Track fallback usage:

```python
FALLBACK_STATS = {
    'total_requests': 0,
    'primary_success': 0,
    'fallback_used': 0,
    'fallback_by_model': {}
}

def log_fallback_stats():
    """Log fallback statistics"""
    if FALLBACK_STATS['total_requests'] == 0:
        return

    logger.info("="*60)
    logger.info("Fallback Statistics")
    logger.info("="*60)
    logger.info(f"Total requests: {FALLBACK_STATS['total_requests']}")
    logger.info(f"Primary success: {FALLBACK_STATS['primary_success']}")
    logger.info(f"Fallback used: {FALLBACK_STATS['fallback_used']}")

    if FALLBACK_STATS['fallback_by_model']:
        logger.info("Fallback by model:")
        for model, count in FALLBACK_STATS['fallback_by_model'].items():
            logger.info(f"  {model}: {count}")
```

## Testing Checklist
- [ ] Simulate primary model failure
- [ ] Verify automatic fallback to secondary
- [ ] Test with all models unavailable
- [ ] Test per-section fallback chains
- [ ] Monitor fallback statistics
- [ ] Verify graceful error messages

## Notes
- Fallback increases reliability but may reduce quality
- Smaller fallback models are faster but less capable
- Monitor fallback usage to identify issues with primary model
- Disable for consistent quality requirements
