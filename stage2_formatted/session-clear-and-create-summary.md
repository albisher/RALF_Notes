**Tags:** #simulation, #session-management, #drone-control, #replay-data, #automation
**Created:** 2026-01-12
**Type:** code-notes

# simulation/scripts/clear_and_create_fresh_session.py

## Summary

```
Script automates session reset and replay data generation for drone simulations.
```

## Details

> This script handles the lifecycle of simulation sessions by stopping the current run, clearing existing sessions, and initializing a new session. It spawns a drone at a predefined origin (0, 0, 0) and generates motion history via repeated `/move_to` commands. The script captures session metadata (e.g., timestamp) and ensures data persistence by stopping the simulation explicitly. Motion history accumulates at 240Hz, requiring active simulation steps to populate replay data.

## Key Functions

### `Session Initialization`

Creates a new session with a fresh drone spawn at (0, 0, 0).

### `Motion History Generation`

Executes `/move_to` commands to populate motion history data.

### `Session Persistence`

Triggers `/api/stop` to save session data before returning the session ID.

### `Status Validation`

Checks simulation status (`/api/status`) to confirm active execution.

## Usage

Run via command line:
```bash
python3 simulation/scripts/clear_and_create_fresh_session.py
```
Ensure the simulation is running before execution. The script outputs the latest session ID (e.g., timestamp-based).

## Dependencies

> ``/api/stop``
> ``/api/status``
> ``/move_to` (API endpoints for simulation control)`
> ``drone-movement` logic (internal simulation framework).`

## Related

- [[drone-movement-rc-tracking-implementation]]
- [[hardcoded-0-0-5-investigation]]

>[!INFO] Motion History Requirement
> Motion history accumulates only if the simulation is actively stepping (240Hz). If no data is recorded, verify:
> - Simulation thread is running (`/api/status` shows `running: true`).
> - Drone commands are being processed (e.g., `/move_to` commands are valid).
>

>[!WARNING] Session ID Timestamps
> Session IDs are auto-generated timestamps (e.g., `YYYYMMDDHHMM`). Ensure the latest session is selected in the UI to load replay data.
