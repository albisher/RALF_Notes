**Tags:** #pytest, #http-endpoints, #session-management, #testing, #api-testing
**Created:** 2026-01-12
**Type:** test-reference

# test_session_endpoints

## Summary

```
Script validates session-related API endpoints for correctness and functionality.
```

## Details

> This script uses the `requests` library to test HTTP endpoints for session management functionality. It constructs requests for common operations like listing sessions, selecting sessions, replaying sessions, and querying the database session list. Each test checks the HTTP status code and optionally parses the JSON response. The script handles exceptions gracefully and provides detailed feedback for each test case.

## Key Functions

### `test_endpoint`

Executes HTTP requests (GET/POST) against a specified URL, validates the status code, and logs response details.

### `main`

Orchestrates the execution of predefined session endpoint tests, printing results in a structured format.

## Usage

1. Run the script directly (`python test_session_endpoints.py`).
2. It will test:
   - GET `/api/sessions` (list sessions)
   - POST `/api/sessions/<session_id>/select` (select session)
   - GET `/api/sessions/<session_id>/replay` (replay session)
   - GET `/api/sessions/db/list` (database session list)
3. Output includes success/failure indicators, status codes, and truncated response bodies.

## Dependencies

> `requests`
> `json (built-in)`
> `sys (built-in)`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses `http://localhost:5007` as the base URL. Ensure the target server is running and accessible at this endpoint before execution.

>[!WARNING] Caution
> Truncated response bodies (e.g., `...`) may hide critical errors. For debugging, increase the `response.text[:200]` limit or inspect raw responses manually.
