**Tags:** #unit-test, #ai-integration, #flask-rest, #jwt-authentication, #database-testing
**Created:** 2026-01-13
**Type:** test-reference

# test_ai_endpoints

## Summary

```
Tests AI endpoints for a Flask application, validating health, model availability, rate limits, and text/world content generation.
```

## Details

> This test suite verifies the functionality of AI-related endpoints in a Flask application using SQLite in-memory database. It sets up a test user, world, and JWT token before running tests for endpoints like `/api/ai/health`, `/api/ai/models`, and `/api/ai/generate-text`. The tests cover authentication, input validation, error handling, and expected responses (e.g., 400 for missing prompts, 503 if Ollama is unavailable). The `setUp` initializes a test environment, while `tearDown` cleans up database resources.

## Key Functions

### ``AIEndpointsTestCase.setUp()``

Initializes test database, user, world, and JWT token.

### ``test_ai_health_endpoint()``

Validates `/api/ai/health` returns correct status and metadata.

### ``test_ai_models_endpoint()``

Checks `/api/ai/models` endpoint response structure.

### ``test_rate_limit_status_endpoint()``

Tests rate limit status endpoint validation.

### ``test_generation_history_endpoint()``

Ensures `/api/ai/generation-history` returns expected data.

### ``test_generate_text_missing_prompt()``

Confirms 400 error for empty prompt input.

### ``test_generate_text_with_prompt()``

Tests successful text generation with valid input (or 503 if Ollama unavailable).

### ``test_generate_world_content_missing_world_id()``

Validates 400 error for missing `world_id`.

### ``test_generate_world_content_missing_content_type()``

Ensures 400 error for missing `content_type`.

### ``test_generate_world_content_invalid_world()``

Checks 404 response for invalid `world_id`.

## Usage

Run the test suite via `unittest`:
```bash
python -m unittest test_ai_endpoints.py
```
Or execute directly:
```python
python test_ai_endpoints.py
```

## Dependencies

> `unittest`
> `Flask`
> `SQLAlchemy`
> `Flask-JWT-Extended`
> ``app` (Flask app instance)`
> ``db` (SQLAlchemy session)`
> ``models` (User`
> `World`
> `WorldElement)`
> ``auth` (test user creation)`
> ``ai_service` (HashGenerator`
> `AIService)`
> ``jwt` (token generation).`

## Related

- [[Flask-AI-App-Architecture]]
- [[World-Generation-Endpoints]]
- [[JWT-Authentication-Guide]]

>[!INFO] Test Environment Setup
> Uses SQLite in-memory database (`:memory:`) for isolation. The `setUp` method creates a test user and world, while `tearDown` resets the database to prevent test contamination.

>[!WARNING] Dependency on Ollama
> The `test_generate_text_with_prompt()` test may return a 503 error if Ollama (the AI backend) is unavailable, requiring manual inspection of the response structure.
