**Tags:** #testing, #drone_simulation, #rc_control, #api_integration, #session_management
**Created:** 2026-01-13
**Type:** code-notes

# test_drone_movement_with_rc_tracking

## Summary

```
Test script for drone movement simulation with remote control (RC) command tracking and session management.
```

## Details

> This script automates a drone movement test by clearing existing sessions, restarting a simulation in GUI mode, and executing predefined drone movement commands. It tracks RC commands and motor rotations with timestamps via an API, ensuring real-time visibility and logging of drone actions. The test sequence includes moving the drone from (0,0,0) to (10,10,10) and back, while logging all interactions with the simulation server.

## Key Functions

### `clear_all_sessions()`

Prints a placeholder message for clearing sessions from a database (conceptual placeholder; actual implementation uses an API).

### `clear_sessions_via_api(base_url)`

Fetches existing sessions from an API endpoint (`http://localhost:5007/api/sessions`), logs them, and notes that the new session will overwrite them.

### `restart_simulation(base_url)`

Initiates a simulation restart via API (`http://localhost:5007/api/restart`), configures it for GUI mode (visible simulation), and returns the generated session ID.

## Usage

1. Run the script to:
   - Clear existing sessions (via API).
   - Restart the simulation in GUI mode.
   - Execute drone movement commands (e.g., `move_to`).
2. The script logs session IDs, RC commands, and motor rotations with timestamps.
3. Ensure the simulation server (`http://localhost:5007`) is running before execution.

## Dependencies

> `requests`
> `json`
> `pathlib (standard Python libraries)`
> `external simulation server at `http://localhost:5007` (requires `python simulation/hmrs_simulation_live.py` to run).`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the simulation server is running at `http://localhost:5007`. If not, it will fail with a connection error. Ensure the server is started with `python simulation/hmrs_simulation_live.py` before running this test.

>[!WARNING] Caution
> The script does not delete sessions directly—it logs them and notes that the new session will overwrite existing ones. If multiple sessions are critical, manual cleanup may be required.
