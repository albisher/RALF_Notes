**Tags:** #database, #api, #session_management, #verification, #python, #requests
**Created:** 2026-01-13
**Type:** code-notes

# create_and_verify_db_session

## Summary

```
Script to create and verify a database session via API, ensuring proper session storage and retrieval.
```

## Details

> This script automates the creation of a session using an API endpoint and verifies its persistence in a database. It uses the `requests` library to interact with a local server (`http://localhost:5007`) via two endpoints: `/api/sessions/create-demo` (for named sessions) or `/api/start` (for default sessions). After creation, it checks the database via `/api/sessions/db/{session_id}` to confirm the session exists and retrieves metadata like `session_id`, `status`, `workflow_state`, and simulation details. Error handling includes connection failures and general exceptions.

## Key Functions

### `create_session_via_api`

Initiates a new session via API with optional parameters (`session_name`, `num_buildings`). Returns the generated `session_id` if successful.

### `verify_session_in_db`

Validates the session’s presence in the database by querying the `/api/sessions/db/{session_id}` endpoint and prints detailed session metadata.

## Usage

1. Run the script to create a session (e.g., `python create_and_verify_db_session.py`).
2. Call `create_session_via_api()` with optional arguments (e.g., `create_session_via_api(session_name="test", num_buildings=3)`).
3. Call `verify_session_in_db()` with a session ID (e.g., `verify_session_in_db("abc123")`) to check persistence.

## Dependencies

> `requests`
> `pathlib (via `import requests` and `from pathlib import Path`)`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the server at `http://localhost:5007` is running and accessible. If not, it will log a connection error.

>[!WARNING] Caution
> Hardcoded `BASE_URL` (`http://localhost:5007`) may break if the server address changes. Consider using environment variables or a config file for flexibility. The script truncates `session_dir_path` in the provided snippet; ensure full path is used for completeness.
