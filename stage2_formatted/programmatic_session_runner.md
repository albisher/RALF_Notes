**Tags:** #automation, #simulation, #ml, #api-integration, #session-management
**Created:** 2026-01-13
**Type:** code-notes

# programmatic_session_runner

## Summary

```
Automates simulation session management for ML learning, dirty glass detection, and cleaning missions.
```

## Details

> This script programmatically manages simulation sessions by spawning, starting, and monitoring them. It handles session lifecycle (spawning with configurable building counts, starting with adjustable duration, and waiting for completion with configurable timeouts and check intervals). The class logs success/failure via console output and tracks sessions in internal lists (`sessions`, `successful_sessions`, `failed_sessions`).

## Key Functions

### ``__init__(self, base_url`

str = "http://localhost:5007")`**: Initializes the runner with a simulation API endpoint and session tracking lists.

### ``spawn_session(self, num_buildings`

int = 5) -> Optional[str]`**: Initiates a new session with the specified number of buildings, returns the session ID on success.

### ``start_session(self, duration`

float = 300.0) -> bool`**: Starts an existing session with a configurable duration, returns a boolean success status.

### ``wait_for_completion(self, timeout`

float = 600.0, check_interval: float = 5.0) -> bool`**: Polls the session status until completion or timeout, with adjustable polling frequency.

## Usage

1. Instantiate `ProgrammaticSessionRunner` with the simulation API base URL.
2. Call `spawn_session()` to create sessions (e.g., `runner.spawn_session(num_buildings=5)`).
3. Call `start_session()` to begin execution (e.g., `runner.start_session(duration=60)`).
4. Call `wait_for_completion()` to monitor session completion (e.g., `runner.wait_for_completion(timeout=120)`).

## Dependencies

> `requests`
> `time`
> `json`
> `datetime`
> `sys`

## Related

- [[none]]

>[!INFO] Important Note
> Session IDs are returned only on successful spawns; handle `None` returns gracefully.

>[!WARNING] Caution
> Timeout values in `wait_for_completion()` must be sufficiently large to avoid premature termination. Defaults (600s timeout, 5s interval) may need adjustment for long-running sessions.
