**Tags:** #time-series-data, #drone-tracking, #verification-script, #api-integration, #simulation
**Created:** 2026-01-12
**Type:** code-notes

# verify_time_based_data

## Summary

```
Script verifies drone data consistency over time by tracking positions, logs, and communication.
```

## Details

> This script interacts with a local server (running on `localhost:5007`) to validate that drone-related data (positions, logs, and motion history) accurately reflect changes over time. It uses HTTP requests to fetch real-time and historical data, then organizes it into time-based snapshots. The `TimeBasedDataTracker` class handles session management, server readiness checks, and data retrieval from the simulation API.
> 
> The script’s workflow involves:
> 1. Waiting for the server to initialize.
> 2. Fetching current drone states, communication logs, and motion histories.
> 3. Storing these snapshots in a structured list (`time_samples`) for later analysis.
> 4. Validating that data evolves predictably over time (e.g., drone positions update sequentially).

## Key Functions

### ``wait_for_server(max_wait)``

Polls the server’s `/api/health` endpoint until it responds with HTTP 200, then returns `True` if successful.

### ``get_current_state()``

Retrieves the latest simulation state (e.g., drone coordinates, battery levels) via `/api/state`.

### ``get_communication_log()``

Fetches drone-to-drone or human-machine communication logs from `/api/communication`.

### ``get_motion_history(drone_name)``

Extracts a drone’s trajectory history (e.g., position updates) from `/api/motion/{drone_name}`.

### ``get_all_drone_motion_histories()``

Aggregates motion histories for all drones by querying the current state’s `drones` list.

## Usage

1. Initialize `TimeBasedDataTracker` with the server’s base URL (defaults to `http://localhost:5007`).
2. Call `wait_for_server()` to ensure the server is ready.
3. Use helper methods to fetch data (e.g., `get_current_state()`, `get_communication_log()`).
4. Store results in `time_samples` for post-processing (e.g., plotting time-series trends).

## Dependencies

> `requests`
> `time`
> `json`
> `numpy`
> `typing`
> `datetime`
> `collections.defaultdict`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the server’s API endpoints (`/api/health`, `/api/state`, etc.) return JSON data with predictable structures (e.g., `communication_log` under a `communication_log` key). Validate these keys explicitly if the server’s API changes.

>[!WARNING] Caution
> Timeout errors (e.g., `requests.get` failures) are caught silently but logged. For production use, add retry logic or exponential backoff to handle transient failures gracefully.
