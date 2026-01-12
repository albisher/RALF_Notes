# Enhancement 3: Smart Model Routing by Task

## Priority: ⭐⭐⭐⭐ MEDIUM-HIGH VALUE

## Problem
Not all documentation sections need the same level of AI capability:
- Simple tasks (tags, type classification) can use fast, small models
- Complex tasks (detailed analysis, dependency graphs) benefit from larger models
- Currently uses the same model for everything, wasting time or quality

## Use Cases
- **Fast model** for tags, type → 2-3s per section
- **Quality model** for details, security analysis → 10-15s per section
- **Balanced model** for summaries, usage examples → 5-8s per section

## Current Code Location
- `config.py:26` - Single `MODEL_NAME`
- `main.py:95-126` - `safe_generate()` uses hardcoded model

## Solution
Route different tasks to different models based on complexity and quality requirements.

## Implementation

### Step 1: Define model strategy in config.py

```python
# --- Model Routing Strategy ---
# Assign different models to different task types for optimal speed/quality balance

MODEL_STRATEGY = {
    'fast': {
        'model': 'ministral-3:3b',
        'tasks': ['TYPE_PROMPT', 'TAGS_PROMPT'],
        'temperature': 0.3,
        'description': 'Quick classification tasks'
    },
    'quality': {
        'model': 'qwen2.5:7b',
        'tasks': ['DETAILS_PROMPT', 'DEPENDENCY_GRAPH_PROMPT', 'SECURITY_RISKS_PROMPT'],
        'temperature': 0.1,
        'description': 'Deep analysis requiring reasoning'
    },
    'balanced': {
        'model': 'llama3.2:3b',
        'tasks': ['SUMMARY_PROMPT', 'KEY_FUNCTIONS_PROMPT', 'USAGE_PROMPT', 'RELATED_PROMPT'],
        'temperature': 0.2,
        'description': 'Standard documentation tasks'
    }
}

# Fallback model if task not mapped
DEFAULT_MODEL = MODEL_NAME

# Enable/disable routing (set False to use single model)
ENABLE_MODEL_ROUTING = True
```

### Step 2: Add routing logic to main.py

```python
def get_model_for_task(task_type):
    """
    Route task to optimal model based on strategy.
    Returns (model_name, temperature)
    """
    if not ENABLE_MODEL_ROUTING:
        return MODEL_NAME, 0.2

    for strategy_name, config in MODEL_STRATEGY.items():
        if task_type in config['tasks']:
            model = config['model']
            temp = config['temperature']
            logger.debug(f"{task_type} → {model} (strategy: {strategy_name})")
            return model, temp

    # Fallback to default
    logger.debug(f"{task_type} → {DEFAULT_MODEL} (default)")
    return DEFAULT_MODEL, 0.2


def validate_routing_models():
    """Check that all models in routing strategy are available"""
    if not ENABLE_MODEL_ROUTING:
        return True

    available_models = get_available_models()
    required_models = set()

    for strategy_name, config in MODEL_STRATEGY.items():
        required_models.add(config['model'])

    missing_models = []
    for model in required_models:
        if model not in available_models:
            missing_models.append(model)

    if missing_models:
        logger.warning("Model routing enabled but some models are missing:")
        for model in missing_models:
            logger.warning(f"  - {model} (run: ollama pull {model})")
        logger.warning("Falling back to single model mode")
        return False

    logger.info("Model routing enabled:")
    for strategy_name, config in MODEL_STRATEGY.items():
        logger.info(f"  {strategy_name}: {config['model']} for {len(config['tasks'])} tasks")

    return True
```

### Step 3: Update safe_generate() to accept model parameter

```python
def safe_generate(client, model=None, system=None, prompt=None, options=None, stream=True, prompt_type="UNKNOWN"):
    """
    Generate with retries and streaming support.
    If model is None, will auto-route based on prompt_type.
    """
    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Auto-route model if not specified
    if model is None:
        model, temperature = get_model_for_task(prompt_type)
        # Update options with task-specific temperature
        if options:
            options = {**options, 'temperature': temperature}
        else:
            options = {'temperature': temperature}

    logger.info(f"PROMPT SENT [{prompt_type}] using {model}")
    logger.info(f"--- PROMPT SENT [{prompt_type}] [{timestamp_str}] ---\nMODEL: {model}\nSYSTEM: {system}\nPROMPT: {prompt}\n", extra={'detailed': True})

    for attempt in range(3):
        try:
            kwargs = {"model": model, "prompt": prompt}  # Use routed model
            if system: kwargs["system"] = system
            if options: kwargs["options"] = options
            kwargs["stream"] = stream

            if stream:
                stream_resp = client.generate(**kwargs)
                response = "".join(chunk['response'] for chunk in stream_resp)
                logger.info(f"RESPONSE RECEIVED [{prompt_type}] from {model}")
                logger.info(f"--- RESPONSE RECEIVED [{prompt_type}] [{timestamp_str}] ---\n{response}\n", extra={'detailed': True})
                return response
            else:
                response = client.generate(**kwargs)['response']
                logger.info(f"RESPONSE RECEIVED [{prompt_type}] from {model}")
                logger.info(f"--- RESPONSE RECEIVED [{prompt_type}] [{timestamp_str}] ---\n{response}\n", extra={'detailed': True})
                return response
        except (ResponseError, Exception) as e:
            logger.warning(f"Attempt {attempt+1} failed with {model}: {e}")
            if attempt == 2:
                logger.error(f"All retries failed for {prompt_type}: {e}")
                raise
            time.sleep(2 ** attempt)
    return None
```

### Step 4: Update main() to validate routing

```python
def main():
    logger.info("="*60)
    logger.info("RALF Notes - Ollama Documentation Generator")
    logger.info("="*60)

    # Validate base model
    if not validate_model_availability():
        logger.error("Aborting: Model not available")
        return

    # Validate routing models
    global ENABLE_MODEL_ROUTING
    if not validate_routing_models():
        ENABLE_MODEL_ROUTING = False  # Disable if models missing

    # Warm up all models
    warmup_models()

    # Rest of processing...
```

### Step 5: Update warmup to handle multiple models

```python
def warmup_models():
    """Pre-load all models used in routing strategy"""
    models_to_warmup = set([MODEL_NAME])

    if ENABLE_MODEL_ROUTING:
        for config in MODEL_STRATEGY.values():
            models_to_warmup.add(config['model'])

    for model in models_to_warmup:
        try:
            logger.info(f"Warming up {model}...")
            client.generate(
                model=model,
                prompt="init",
                options={'num_predict': 1, 'keep_alive': '60m'}
            )
            logger.info(f"✓ {model} ready")
        except Exception as e:
            logger.warning(f"Could not warm up {model}: {e}")
```

## Expected Impact

### Performance Comparison (estimated)
**Current (single model):**
- All 8 sections with `qwen2.5:7b`: ~80-100s per file

**With routing:**
- 2 fast sections (`ministral-3:3b`): ~5s
- 3 balanced sections (`llama3.2:3b`): ~20s
- 3 quality sections (`qwen2.5:7b`): ~35s
- **Total: ~60s per file (40% faster)**

### Quality Improvement
- Complex sections (security, dependencies) get better analysis
- Simple sections (tags, type) complete faster
- Overall quality-per-second increases

## Configuration Examples

### Speed-focused (all fast models)
```python
MODEL_STRATEGY = {
    'fast': {
        'model': 'ministral-3:3b',
        'tasks': ['TYPE_PROMPT', 'TAGS_PROMPT', 'SUMMARY_PROMPT', 'KEY_FUNCTIONS_PROMPT'],
        'temperature': 0.3,
    },
    'balanced': {
        'model': 'llama3.2:3b',
        'tasks': ['DETAILS_PROMPT', 'USAGE_PROMPT', 'RELATED_PROMPT',
                  'DEPENDENCY_GRAPH_PROMPT', 'SECURITY_RISKS_PROMPT'],
        'temperature': 0.2,
    }
}
```

### Quality-focused (use best model for most tasks)
```python
MODEL_STRATEGY = {
    'fast': {
        'model': 'ministral-3:3b',
        'tasks': ['TYPE_PROMPT', 'TAGS_PROMPT'],
        'temperature': 0.3,
    },
    'quality': {
        'model': 'qwen2.5:14b',  # Larger model
        'tasks': ['SUMMARY_PROMPT', 'DETAILS_PROMPT', 'KEY_FUNCTIONS_PROMPT',
                  'USAGE_PROMPT', 'RELATED_PROMPT', 'DEPENDENCY_GRAPH_PROMPT',
                  'SECURITY_RISKS_PROMPT'],
        'temperature': 0.1,
    }
}
```

### Single-model mode (disable routing)
```python
ENABLE_MODEL_ROUTING = False  # Use MODEL_NAME for everything
```

## Testing Checklist
- [ ] Verify all models in strategy are available
- [ ] Check logs show correct model routing per section
- [ ] Measure timing improvement vs. single model
- [ ] Validate output quality for each section type
- [ ] Test fallback when routing model unavailable
- [ ] Test with ENABLE_MODEL_ROUTING = False

## Notes
- Requires multiple models to be pulled: `ollama pull <model>`
- Memory usage: ~3-7GB per model loaded simultaneously
- Models stay loaded for 60m due to `keep_alive`
- Can mix and match any Ollama models
- Temperature per task can be tuned independently
