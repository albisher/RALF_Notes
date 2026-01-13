**Tags:** #drone-simulation, #session-management, #replayable-testing, #api-integration, #automation
**Created:** 2026-01-13
**Type:** code-notes

# create_replayable_session

## Summary

```
Script automates creation of a drone simulation session with replayable motion history.
```

## Details

> This script orchestrates a drone simulation workflow: it stops an existing simulation (with retry logic), creates a new demo session, starts the simulation, and verifies readiness. It uses REST API calls to a local drone simulation server (localhost:5007) to handle session lifecycle management. The script includes retry mechanisms for transient failures and waits for simulation initialization before proceeding.

## Key Functions

### `Session Creation`

Creates a demo session with configurable parameters (e.g., "ReplayTest" name, 3 buildings).

### `Simulation Control`

Handles start/stop/reset operations with retry logic.

### `Status Verification`

Checks simulation state via API endpoints.

### `Motion History Capture`

Implicitly enables replayable session by leveraging demo session creation.

## Usage

1. Run as Python script (`python create_replayable_session.py`)
2. Automates full session lifecycle:
   - Stops existing simulation (with retries)
   - Creates demo session
   - Starts simulation
   - Verifies readiness
3. Outputs success/failure status for each step

## Dependencies

> `requests`
> `time`
> `json`

## Related

- [[DroneSimulationAPIReference]]
- [[SessionManagementWorkflow]]

>[!INFO] Important Note
> The script assumes the simulation server is running at `http://localhost:5007`. If the server is elsewhere, update `BASE_URL` accordingly.

>[!WARNING] Caution
> Retry logic may cause delays. For production use, consider adding exponential backoff for the retry mechanism. The 5-second wait after starting may be insufficient for some simulations.
