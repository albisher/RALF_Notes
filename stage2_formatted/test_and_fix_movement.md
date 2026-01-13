**Tags:** #drone-movement, #simulation-test, #debugging, #api-integration
**Created:** 2026-01-13
**Type:** code-notes

# test_and_fix_movement

## Summary

```
Tests and validates drone movement in a simulated environment by spawning, commanding, and monitoring drones.
```

## Details

> This script automates a workflow to test drone movement:
> 1. Resets a simulation server, starts a 5-minute run, and spawns a scout drone at coordinates (0, 0, 5).
> 2. Sends a `move_to` command targeting (10, 10, 10) and logs the response.
> 3. Monitors drone position every second for 30 seconds, recording movement data and calculating Euclidean distance traveled.
> 4. Analyzes results to determine if the drone moved sufficiently (within 0.1m threshold) or if movement failed due to potential issues like weak forces, constraints, or command failures.
> 
> The script uses HTTP requests to interact with a local simulation server (`http://localhost:5007`) and logs debug information to the console.

## Key Functions

### `test_movement()`

Orchestrates the full drone movement test workflow, including reset, spawn, command, monitoring, and analysis.

### `API Calls`

Handles interactions with the simulation server via `requests.post`/`requests.get` for `/api/reset`, `/api/start`, `/api/spawn`, `/api/command`, and `/api/data`.

## Usage

1. Run the script directly (`python test_and_fix_movement.py`).
2. Ensure the simulation server (`http://localhost:5007`) is running and accessible.
3. Monitor console output for debug logs and results.
4. Use the script to identify and diagnose movement issues in drone simulations.

## Dependencies

> `requests`
> `time`
> `json`

## Related

- [[drone_simulation_server]]
- [[movement_debugging_guide]]

>[!INFO] Important Note
> The script assumes the simulation server logs debug information to the console. If the server does not provide real-time feedback, adjust the monitoring loop or add additional logging endpoints.


>[!WARNING] Caution
> If the drone does not move despite valid commands, verify:
> - Server-side `update()` method execution (e.g., missing or incorrect logic).
> - Force magnitudes applied to the drone (e.g., too low to overcome inertia).
> - Physical constraints (e.g., collision detection blocking movement).
