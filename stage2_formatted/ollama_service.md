**Tags:** #API-Integration, #Rate-Limiting, #LLM-Service, #Ollama, #Text-Generation
**Created:** 2026-01-13
**Type:** code-notes

# ollama_service

## Summary

```
Manages Ollama API interactions with text generation, model management, and health checks.
```

## Details

> This code defines an `OllamaServiceBox` class that acts as a wrapper for the Ollama API, handling text generation, model listing, and health checks. It includes rate limiting via `RateLimiterBox`, auto-detection of the Ollama server URL and best model, and structured request/response handling through `BoxInput`/`BoxOutput`. The class processes operations like text generation, model management, and system checks while enforcing rate limits and validating inputs.

## Key Functions

### ``execute``

Routes requests to appropriate sub-methods based on operation type.

### ``_generate_text``

Handles text generation with configurable parameters (temperature, max_tokens, system_prompt).

### ``_list_models``

Fetches and returns available models from the Ollama API.

### ``_check_health``

Verifies if the Ollama service is running and responsive.

### ``_set_default_model``

Updates the default model after validating its availability.

### ``_get_model_info``

Retrieves metadata for a specified model.

### ``_detect_best_model``

Auto-detects the best available model if none is provided.

### ``_detect_ollama_url``

Detects the Ollama server URL (defaults to `http://localhost:11434`).

### ``_make_request``

Internal helper to send HTTP requests to Ollama (not fully implemented in snippet).

## Usage

1. Initialize with `base_url` (optional) and `default_model` (optional).
2. Call `execute()` with a `BoxInput` containing an `operation` (e.g., `"generate_text"`).
3. For text generation, include `prompt`, `model`, and optional parameters (`temperature`, `max_tokens`, `system_prompt`).
4. Example:
   ```python
   input_data = BoxInput(data={"operation": "generate_text", "prompt": "Hello, world!"})
   output = ollama_service.execute(input_data)
   ```

## Dependencies

> `requests`
> `logging`
> ``..core.box_interface``
> ``BoxInput``
> ``BoxOutput``
> ``.rate_limiter.RateLimiterBox``

## Related

- [[Ollama API Documentation]]
- [[BoxInterface Design]]
- [[RateLimiterBox Implementation]]

>[!INFO] Auto-Detection
> If `default_model` is not provided, the service auto-detects the best available model from the API.

>[!WARNING] Rate Limiting
> Exceeding the rate limit (20 calls/60s) will return an error. Ensure proper throttling in client code.

>[!CAUTION] Error Handling
> All API calls include logging and graceful error handling, but network issues may still occur. Validate `success` flag in responses.
