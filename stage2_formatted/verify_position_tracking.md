**Tags:** #drone-tracking, #position-verification, #simulation, #api-integration, #time-series
**Created:** 2026-01-12
**Type:** code-notes

# verify_position_tracking

## Summary

```
Verifies drone position tracking by monitoring movement over time and validating transitions between positions.
```

## Details

> This script programmatically checks drone position tracking by:
> 1. Fetching real-time drone positions via an API endpoint (`/api/state`).
> 2. Recording position history for each drone in a structured dictionary.
> 3. Validating motion patterns by comparing timestamps and spatial changes.
> 4. Integrating with a local server (`http://localhost:5007`) to retrieve drone data, including trajectory logs (`/api/motion/{drone_name}`).
> 
> The `PositionTracker` class manages drone position data, initializes a base reference (origin at `[0, 0, 0]`), and logs trajectories for later analysis. It includes error handling for API failures and waits for the server to initialize before proceeding.

## Key Functions

### ``wait_for_server(max_wait=30)``

Polls the server endpoint (`/api/health`) until it responds with HTTP 200, defaulting to 30 seconds of timeout.

### ``get_current_drone_positions()``

Fetches live drone positions from `/api/state`, parsing JSON into a dictionary of drone names and their coordinates (converted to NumPy arrays) along with timestamps.

### ``get_motion_history(drone_name)``

Retrieves a drone’s recorded trajectory from `/api/motion/{drone_name}`, returning a list of position snapshots over time.

### ``track_positions_during_simulation(duration=60.0, sample_interval=1.0)``

Continuously samples drone positions for a specified duration (e.g., 60 seconds) at fixed intervals (e.g., 1 second), storing results in `position_history`.

## Usage

1. Initialize `PositionTracker` with the server URL (defaults to `http://localhost:5007`).
2. Call `wait_for_server()` to ensure the server is ready.
3. Use `get_current_drone_positions()` to fetch live positions.
4. Call `get_motion_history(drone_name)` to retrieve historical trajectory data.
5. For automated tracking, invoke `track_positions_during_simulation()` with desired duration and sampling rate.

## Dependencies

> `requests`
> `time`
> `json`
> `numpy`
> `typing`
> `datetime`
> `sys`

## Related

- [[drone_simulation_server]]
- [[api_specification]]

>[!INFO] Server Initialization
> The script assumes the target server (`BASE_URL`) is running and accessible. If the server fails to respond within `max_wait` seconds, the script exits with an error.

>[!WARNING] Rate Limiting
> Frequent API calls may trigger throttling. Implement retries or exponential backoff for production use.
