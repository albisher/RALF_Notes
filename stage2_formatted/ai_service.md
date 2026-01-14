**Tags:** #AI_API_Integration, #Rate_Limiting, #Hashing_Utilities, #External_API_Client, #Authentication_Management
**Created:** 2026-01-13
**Type:** code-notes

# ai_service

## Summary

```
Manages AI API interactions with rate limiting, hashing utilities, and external API clients (Perplexity/OpenAI/Ollama).
```

## Details

> This file implements an `ExternalAIService` class for interacting with external AI APIs (Perplexity, OpenAI) and a basic `OllamaService` stub. It includes:
> - **Rate limiting** via `RateLimiter` to enforce API call quotas (e.g., 20 calls/minute).
> - **Hashing utilities** (`HashGenerator`) for generating consistent hashes (e.g., for world elements or seeds).
> - **API key management** via `APIKeyService` for secure credential handling.
> - **HTTP request handling** with retry logic and error logging for Perplexity/OpenAI endpoints.
> - **Partial Ollama integration** (initially incomplete, with `base_url` parameter).
> 
> The `ExternalAIService` enforces rate limits before making API calls, validates API keys, and logs failures. The `HashGenerator` provides methods for generating deterministic hashes (e.g., for world names, elements, or seeds).

## Key Functions

### ``RateLimiter.is_allowed()``

Checks if an API call is allowed based on call history and time window.

### ``HashGenerator.generate_hash()``

Creates SHA-256 hashes from input data (e.g., `world_name + user_id`).

### ``ExternalAIService.generate_text_with_perplexity()``

Calls Perplexity API with rate-limiting and error handling.

### ``ExternalAIService.get_api_key_status()``

Retrieves status of configured API keys.

### ``OllamaService.__init__()``

Initializes Ollama client (placeholder for future implementation).

## Usage

1. Initialize `ExternalAIService` to manage API calls.
2. Use `generate_text_with_perplexity()`/`generate_text_with_openai()` for text generation.
3. Validate keys with `validate_api_keys()` or check status with `get_api_key_status()`.
4. Extend `OllamaService` with a fully implemented `base_url` and endpoint logic.

## Dependencies

> ``requests``
> ``hashlib``
> ``json``
> ``time``
> ``logging``
> ``config``
> ``api_key_service``

## Related

- [[`config]]
- [[`api_key_service]]

>[!INFO] Rate Limiting
> The `RateLimiter` enforces a 20-calls-per-minute limit. Exceeding this raises an exception.

>[!WARNING] API Key Security
> API keys are fetched from `APIKeyService` but are not encrypted in transit. Ensure secure storage (e.g., environment variables) for production use.

>[!WARNING] Ollama Incomplete
> The `OllamaService` class lacks a fully implemented `base_url` parameter and endpoint logic; extend it with proper configuration.
