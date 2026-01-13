**Tags:** #machine-learning, #simulation, #automation, #api-integration, #server-communication
**Created:** 2026-01-13
**Type:** code-notes

# run_ml_sessions

## Summary

```
Automates running 5 machine learning sessions to analyze learned patterns in a simulation environment.
```

## Details

> This script orchestrates five independent simulation sessions, each involving drone spawning, simulation execution, and cleanup. It interacts with a local server (`http://localhost:5007`) via REST APIs to manage sessions, drones, and simulation states. The workflow includes waiting for server readiness, spawning drones, starting simulations, and handling completion, while logging errors gracefully.

## Key Functions

### `wait_for_server(max_wait=30)`

Polls the server’s `/api/health` endpoint until it responds with `200`, indicating readiness.

### `stop_and_reset()`

Terminates any running simulation, resets the server state, and waits for cleanup.

### `spawn_session(num_buildings=3)`

Initiates a new simulation session with configurable building count via `/api/sessions/spawn`.

### `spawn_drones(scout_count=2, tanker_count=1)`

Dynamically spawns scout and tanker drones at predefined positions using `/api/spawn`.

### `start_simulation(duration=120)`

Launches a simulation for a specified duration via `/api/start`.

### `wait_for_completion(timeout=150)`

Monitors simulation progress via `/api/state` until completion or timeout.

## Usage

1. Ensure the server (`http://localhost:5007`) is running and accessible.
2. Call `wait_for_server()` to verify server readiness.
3. Execute `spawn_session()` and `spawn_drones()` to initialize the session.
4. Trigger `start_simulation()` to begin the run.
5. Use `wait_for_completion()` to handle session termination.
6. Cleanup with `stop_and_reset()` after each session.

## Dependencies

> `requests`
> `numpy`
> `pathlib`
> `typing`
> `time`
> `sys`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the server handles session IDs and drone states internally. If drones fail to spawn, retry logic is minimal (single `try-except` block); consider retry logic for production use.

>[!WARNING] Caution
> Timeout values (e.g., `max_wait=30`, `timeout=150`) are hardcoded. Adjust these dynamically for variable server/simulation speeds to avoid deadlocks or missed events.
