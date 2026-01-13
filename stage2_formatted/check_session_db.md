**Tags:** #database-check, #api-integration, #session-analysis, #motion-history
**Created:** 2026-01-13
**Type:** code-notes

# check_session_db

## Summary

```
Analyzes session data from a database via API to verify session details and track position changes.
```

## Details

> This script queries a local database (accessed via `http://localhost:5007`) to retrieve session details for a given `session_id`. It fetches session metadata, workflow state, and performance metrics, then prints structured output for verification. The script handles missing fields gracefully and logs base positions and metadata in JSON format if available. It also includes a placeholder for analyzing motion history (not fully implemented in this snippet).

## Key Functions

### `check_session_via_api(session_id`

str)**: Fetches session data from the database API, validates its presence, and prints formatted details including session ID, status, workflow state, timestamps, and optional metadata/performance metrics.

## Usage

1. Call `check_session_via_api(session_id)` with a valid session identifier.
2. The script prints session details in a readable format, including:
   - Basic session info (ID, status, duration).
   - Position and metadata (if stored).
   - Performance metrics (if available).
3. Useful for debugging or auditing session data consistency.

## Dependencies

> `requests`
> `numpy`
> `pathlib (built-in)`
> `sys`
> `json`

## Related

- [[none]]

>[!INFO] Important Note
> This script relies on an API endpoint (`/api/sessions/db/{session_id}`) hosted at `http://localhost:5007`. Ensure the server is running and accessible before execution.

>[!WARNING] Caution
> If the API returns a non-200 status code or times out, the script will log an error but continue execution. For production use, add retry logic or validation for critical fields.
