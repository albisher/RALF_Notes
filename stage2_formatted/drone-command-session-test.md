**Tags:** #test, #drone-automation, #session-management, #command-verification, #api-integration, #simulation
**Created:** 2026-01-13
**Type:** test-reference

# drone-command-session-test

## Summary

```
Comprehensive drone command session test suite verifying session creation, drone spawning, and command-response workflows.
```

## Details

> This test validates the full command flow in a drone simulation system, including session initialization, drone spawning, and execution of `move_to`/`hover` commands. It verifies command queuing, drone response handling, and movement validation through multiple API endpoints. The test employs retry logic for state checks and handles visualization delays gracefully.

## Key Functions

### ``test_drone_command_session.py``

Main test script orchestrating session lifecycle and command execution.

### ``/api/health``

Server health check endpoint.

### ``/api/reset``

Clears simulation state before testing.

### ``/api/start``

Initiates a new session.

### ``/api/spawn``

Creates drone instances for testing.

### ``/api/command``

Sends commands (e.g., `move_to`, `hover`) to drones.

### ``/api/master/commands``

Inspects command queue status.

### ``/api/communication``

Logs drone interaction data.

## Usage

Execute via:
```bash
cd simulation
python test_drone_command_session.py
```
Results are saved to `simulation_output/hmrs_live_verification/drone_command_session_test.json`.

## Dependencies

> ``requests` (for HTTP API calls)`
> ``json` (for output storage)`
> ``time` (for delays)`
> ``os` (for path handling).`

## Related

- [[test_drone_command_session]]
- [[drone-automation-api-docs]]
- [[session-management-workflow]]

>[!INFO] Important Note
> Test uses retry logic (up to 3 attempts) for critical state checks (e.g., session activation, drone spawning) to handle transient failures.
>

>[!WARNING] Caution
> Visualization lag may cause delays in drone movement verification. The test considers command queue status as a valid success indicator if drone fails to respond visually.
