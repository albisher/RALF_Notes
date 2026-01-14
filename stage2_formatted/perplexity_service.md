**Tags:** #API-Integration, #Text-Generation, #Rate-Limiting, #Async-Processing, #LLM-Services
**Created:** 2026-01-13
**Type:** code-notes

# perplexity_service

## Summary

```
Handles Perplexity AI API interactions for text generation with rate-limiting and error handling.
```

## Details

> This service class (`PerplexityServiceBox`) acts as a wrapper around the Perplexity API, enabling controlled text generation via a structured input/output interface. It enforces rate limits (20 calls/minute) via a `RateLimiterBox` dependency and validates API credentials dynamically. The core logic (`_generate_text`) constructs a POST request to Perplexity’s chat endpoint, passing configurable parameters (model, temperature, token limit) while respecting the user-provided `api_key` or falling back to an instance-level key.

## Key Functions

### ``execute()``

Dispatches requests based on operation type (e.g., `"generate_text"`), routing calls to `_generate_text` or returning errors for unsupported operations.

### ``_generate_text()``

Core method that:

### ``RateLimiterBox``

Manages call throttling (20 calls/60s) to prevent API abuse.

## Usage

1. Initialize with an optional `api_key`:
   ```python
   service = PerplexityServiceBox(api_key="YOUR_KEY")
   ```
2. Call `execute()` with a `BoxInput` containing:
   ```python
   input_data = BoxInput(
       data={"operation": "generate_text", "prompt": "Ask me about AI"},
       context={"api_key": "fallback_key"}  # Optional
   )
   result = service.execute(input_data)
   ```
3. Handle `BoxOutput` (success/error) to extract `generated_text` or errors.

## Dependencies

> ``requests``
> ``logging``
> ``..core.box_interface``
> ``.rate_limiter``

## Related

- [[Perplexity API Docs]]
- [[RateLimiterBox Implementation]]

>[!INFO] Important Note
> The `api_key` can be overridden per-request via `data["api_key"]` or `context["api_key"]` to avoid hardcoding in the instance.
>

>[!WARNING] Caution
> Rate limits are enforced globally; exceeding them returns a `success=False` response. Always handle errors gracefully (e.g., retry logic).
