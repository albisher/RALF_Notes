**Tags:** #API-Integration, #LLM-Service, #OpenRouter, #Google-Gemini, #Rate-Limiting
**Created:** 2026-01-13
**Type:** code-notes

# gemini_service

## Summary

```
Handles text generation via Google Gemini API (or OpenRouter fallback) with rate-limiting and configurable parameters.
```

## Details

> This service box manages interactions with the Google Gemini API, supporting both direct API access and OpenRouter as an alternative. It enforces rate limits via a `RateLimiterBox` and processes text generation requests with configurable parameters (temperature, max tokens). The `_generate_text` method dynamically routes requests to either OpenRouter or Google’s direct API based on user input, while handling errors gracefully via structured `BoxOutput` responses.

## Key Functions

### ``execute``

Orchestrates the high-level workflow, routing requests to `_generate_text` for text generation or returning errors for unsupported operations.

### ``_generate_text``

Core logic for generating text via Gemini API, handling both OpenRouter and direct API formats, rate limits, and API key validation.

### ``RateLimiterBox``

Manages API call quotas (20 calls/minute) to prevent throttling.

## Usage

1. Initialize with an optional API key and OpenRouter preference:
   ```python
   gemini_box = GeminiServiceBox(api_key="your_key", use_openrouter=True)
   ```
2. Call `execute` with a `BoxInput` containing `operation`, `prompt`, and optional parameters:
   ```python
   input_data = BoxInput(data={"operation": "generate_text", "prompt": "Hello"})
   output = gemini_box.execute(input_data)
   ```
3. Handle responses via `BoxOutput.success` and `BoxOutput.data`.

## Dependencies

> ``requests``
> ``logging``
> ``..core.box_interface``
> ``.rate_limiter``

## Related

- [[Gemini API Docs]]
- [[OpenRouter Documentation]]
- [[Rate Limiting Guide]]

>[!INFO] Rate Limiting
> The `RateLimiterBox` enforces a 20-calls-per-minute limit. Exceeding this will return a `success=False` response with an error message.

>[!WARNING] API Key Dependency
> If `api_key` is not provided, the service defaults to OpenRouter. Direct Google API access requires a valid Google Cloud API key. Insecure keys may expose credentials.
