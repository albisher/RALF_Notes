**Tags:** #test, #api-integration, #drone-simulation, #logging, #automation
**Created:** 2026-01-13
**Type:** code-notes

# test_command_logging

## Summary

```
Test script validates command logging for drone simulation API by verifying session setup, GPS positioning, drone spawning, and command execution.
```

## Details

> This script automates a sequence of operations to test a drone simulation API’s logging capabilities:
> 1. Checks API health before proceeding.
> 2. Initiates a new simulation session.
> 3. Configures drone GPS coordinates to a predefined "Home" location (Kuwait).
> 4. Spawns a drone at the set coordinates with customizable name/type.
> 5. Logs each step for verification of correct command execution and response handling.
> 
> The script uses `requests` to interact with a local API (`http://localhost:5007`) and prints status updates with visual markers (✅/❌) for debugging.

## Key Functions

### `check_api_health()`

Verifies API availability via `/api/health` endpoint.

### `start_new_session()`

Initiates a new simulation session via `/api/start`.

### `set_position_to_home()`

Sets drone GPS coordinates to Kuwait’s Home coordinates.

### `spawn_drone()`

Creates a drone with customizable attributes (name, type, initial position).

## Usage

1. Run the script directly (`python test_command_logging.py`).
2. Ensure the target API (`http://localhost:5007`) is running.
3. Modify `BASE_URL` if needed for testing against a different endpoint.
4. Customize drone parameters (e.g., `drone_name`, `drone_type`) in `spawn_drone()`.

## Dependencies

> `requests`
> `time`
> `json`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the API returns JSON responses with keys like `session_id` or `drone_id`. If the API uses different field names, adjust parsing logic accordingly.

>[!WARNING] Caution
> Timeout settings (e.g., `timeout=10`) may need adjustment for high-latency networks or slow APIs. Exceeding timeouts can cause `requests` to fail silently.
