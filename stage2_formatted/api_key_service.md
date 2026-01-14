**Tags:** #security, #api-integration, #configuration-management, #caching, #logging
**Created:** 2026-01-13
**Type:** documentation-research

# api_key_service

## Summary

```
Secure API key management system for backend AI services, retrieving keys from config systems with caching and validation.
```

## Details

> This module centralizes secure access to external API keys (e.g., Perplexity, OpenAI) via a caching layer and configuration system. It retrieves keys from environment variables or Docker secrets, avoids hardcoding, and provides validation and monitoring capabilities. The design ensures keys are never exposed in application code, with error handling and logging for debugging.
> 
> The service implements a singleton pattern via a global instance (`api_key_service`) and includes helper functions for common API key access. It supports dynamic cache clearing for testing or key updates and provides metadata about key availability without exposing secrets.

## Key Functions

### ``APIKeyService``

Core class managing API key retrieval, caching, and validation.

### ``_get_cached_key``

Internal method to fetch and cache API keys by service.

### ``get_perplexity_api_key()``

Convenience function to retrieve Perplexity API key.

### ``get_openai_api_key()``

Convenience function to retrieve OpenAI API key.

### ``validate_api_keys()``

Checks availability of all supported API keys.

### ``clear_cache()``

Resets cached keys to force fresh retrieval.

### ``get_api_key_info()``

Returns metadata (status, count) about API keys.

### ``SecureAIService``

Example class demonstrating secure API key usage in AI workflows.

## Usage

1. Initialize the service via `get_api_key_service()` (returns singleton instance).
2. Use helper functions (e.g., `get_perplexity_api_key()`) or the `APIKeyService` class directly.
3. Integrate with AI services (e.g., `SecureAIService`) to handle API calls securely.
4. Call `validate_api_keys()` to check key availability or `clear_cache()` for testing.

## Dependencies

> ``config` (custom module for `get_config()` and `get_api_key()`)`
> `Python’s `logging``
> ``typing` (for type hints).`

## Related

- [[Space Pearl Configuration System]]
- [[Backend AI Service Architecture]]

>[!INFO] Caching Behavior
> Keys are cached after first retrieval to improve performance, but cached values are invalidated on errors or cache clearing.

>[!WARNING] Hardcoded Placeholder
> The code includes a placeholder check (`"your-{service}-api-key-here"`), which should be replaced with actual validation logic for production use.

>[!INFO] Singleton Pattern
> The global instance (`api_key_service`) ensures a single point of control for all API key operations, reducing redundancy.
