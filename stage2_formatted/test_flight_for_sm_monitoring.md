**Tags:** #drone_simulation, #system_monitoring, #api_testing, #automated_testing
**Created:** 2026-01-13
**Type:** code-notes

# test_flight_for_sm_monitoring

## Summary

```
Script automates drone flight testing for system monitoring by setting GPS, starting simulation, spawning drones, and sending flight commands.
```

## Details

> This script orchestrates a drone flight test workflow for system monitoring by:
> 1. Configuring a GPS home location (Kuwait coordinates).
> 2. Initiating a simulation environment.
> 3. Spawning a drone at a predefined position.
> 4. Executing sequential flight commands (e.g., `move_to`) to simulate activity.
> 5. Validating API responses and handling errors gracefully.
> 
> The script uses `requests` to interact with a local API (`http://localhost:5007`) and includes delays (`time.sleep`) to ensure proper initialization and command processing.

## Key Functions

### `set_gps_location(lat, lon)`

Sets the drone’s GPS home position via a POST request to `/api/master-controls/gps`.

### `start_simulation()`

Triggers the simulation server with a POST request to `/api/start` and waits 3 seconds for initialization.

### `spawn_drone(drone_name, position)`

Deploys a drone (default: `Scout-001`) at a specified 3D coordinate using `/api/spawn`.

### `send_move_command(drone_name, target_position)`

Issues a `move_to` command to a drone via `/api/command` with JSON payload.

## Usage

1. Run the script to execute the full workflow:
   ```bash
   python3 test_flight_for_sm_monitoring.py
   ```
2. Customize drone name/position or add more commands (e.g., `rotate`, `land`) by modifying the `send_move_command` logic.
3. Monitor API responses for success/failure (e.g., HTTP 200/4xx).

## Dependencies

> `requests`
> `time`
> `json (Python standard libraries)`
> `external API at `http://localhost:5007`.`

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the API server (`http://localhost:5007`) is running and accessible. If not, replace `BASE_URL` or handle connection errors explicitly.

>[!WARNING] Caution
> Delays (`time.sleep`) are hardcoded for initialization. Adjust timing based on simulation/drone latency to avoid race conditions.
