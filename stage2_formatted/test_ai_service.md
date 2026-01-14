**Tags:** #testing, #ai-integration, #hash-generation, #ollama-service, #rate-limiting
**Created:** 2026-01-13
**Type:** code-notes

# test_ai_service

## Summary

```
Script runs automated tests for an AI service, focusing on hash generation, Ollama integration, and rate limiting.
```

## Details

> This test script evaluates the functionality of an AI service by verifying its components: **HashGenerator** (consistency and uniqueness of hash generation), **OllamaService** (health checks, model listing, and rate limiting), and **AIService** (rate limit status, model availability, and world/content generation). The tests ensure deterministic behavior for hash generation across identical inputs and validate integration with the Ollama AI platform. The script runs sequentially, reporting pass/fail statuses for each test module.

## Key Functions

### `test_hash_generator`

Validates hash generation consistency and uniqueness for inputs like world names, user IDs, and related elements.

### `test_ollama_service`

Checks Ollama’s health, lists available models, and verifies rate limiting functionality.

### `test_ai_service`

Tests the main AI service’s rate limit status, model availability, and world/content generation (if Ollama is operational).

### `test_hash_consistency`

Ensures repeated identical inputs produce identical hashes and different inputs yield distinct hashes.

### `main`

Orchestrates all test functions, aggregates results, and exits with success/failure status.

## Usage

1. Run the script directly (`python test_ai_service.py`).
2. It executes predefined test functions in sequence, printing pass/fail results.
3. Exit code `0` indicates all tests passed; `1` indicates failures.

## Dependencies

> ``ai_service``
> ``HashGenerator``
> ``OllamaService` (imported from `ai_service` module)`
> `Python standard libraries (`sys``
> ``os`).`

## Related

- [[ai_service]]
- [[HashGenerator class]]
- [[OllamaService class]]

>[!INFO] Important Note
> The script dynamically appends the current script’s directory to `sys.path`, ensuring imports from `ai_service` resolve correctly regardless of working directory.


>[!WARNING] Caution
> Skipped content generation tests may fail if Ollama is unavailable, leading to partial test results. Always verify Ollama’s health before running these tests.
