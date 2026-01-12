**Tags:** #ui-testing, #session-management, #api-integration, #database-verification
**Created:** 2026-01-12
**Type:** code-notes

# verify_session_ui_complete

## Summary

```
Verifies UI completeness for session playback by testing session saving, loading, and drone movement visualization.
```

## Details

> This script performs automated UI verification for session playback functionality, including checks for session persistence in a database, API loadability, and availability of motion history data for drone movements. It uses HTTP requests to validate session data integrity and replay capabilities. The script prints detailed statuses for each test, including HTTP responses, session metadata, and drone movement history.

## Key Functions

### `test_session_saved(session_id)`

Validates if a session exists in the database via an API endpoint.

### `test_session_loadable(session_id)`

Checks if the session can be loaded via a POST request to the API and verifies the presence of replay data (motion history).

### `print_section(title)`

Helper function to format and print section headers for test output.

## Usage

1. Run the script directly to execute predefined tests for `TEST_SESSION`.
2. Override `TEST_SESSION` variable to test a different session ID.
3. Execute individual test functions manually if needed (e.g., `test_session_saved()`).
4. Ensure the backend server (`BASE_URL`) is running and accessible.

## Dependencies

> `requests`
> `json`
> `pathlib (built-in)`
> `sys (built-in)`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses `requests` to interact with a local API (`http://localhost:5007`). Ensure the server is running and accessible before execution.

>[!WARNING] Caution
> Timeout settings (10 seconds) may fail if the server is unresponsive. Increase `timeout` if needed, but avoid excessively long waits to prevent hanging.
