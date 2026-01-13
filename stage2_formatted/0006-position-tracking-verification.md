**Tags:** #drone-tracking, #simulation-verification, #position-validation, #real-time-data, #automated-testing
**Created:** 2026-01-13
**Type:** code-notes

# 0006-position-tracking-verification

## Summary

```
Script verifies drone position tracking accuracy, movement validation, and travel path confirmation in a simulated environment.
```

## Details

> The script `verify_position_tracking.py` programmatically checks if drones move between predefined positions over time. It spawns drones at a base location, records their positions in real-time for a configurable duration (default 60s), and analyzes whether positions change significantly (>0.1m). The script relies on a simulation server to spawn drones, reset states, and track movements, but currently fails due to drones remaining stationary. Key logic includes sampling positions every second, calculating total distance traveled, and verifying travel from base to target buildings.

## Key Functions

### ``verify_position_tracking.py``

Main script orchestrating session setup, drone spawning, real-time tracking, and movement analysis.

### ``spawn_drones()``

Configurable function to initialize scout drones at base positions.

### ``start_simulation()``

Initiates simulation with a set duration, enabling real-time position sampling.

### ``track_positions()``

Collects drone positions every second, storing them with timestamps.

### ``analyze_movement()``

Evaluates if positions changed significantly, checks total distance traveled, and validates travel paths.

## Usage

Run from the `simulation` directory:
```bash
cd simulation
python3 verify_position_tracking.py
```
Configure via command-line args (e.g., `--buildings 3`, `--sim_time 30`) or modify script parameters directly.

## Dependencies

> ``simulation-server``
> ``drone-api``
> ``time-series-storage` (external libraries/modules for session management`
> `drone control`
> `and data storage).`

## Related

- [[simulation-server-docs]]
- [[drone-api-reference]]
- [[position-tracking-protocol]]

>[!INFO] Important Note
> The script relies on the simulation server to enforce drone movement logic. If drones are statically positioned, the `analyze_movement()` function will fail to detect changes, even if the server logic is correct.

>[!WARNING] Caution
> Current implementation defaults to 60s tracking. Reduce `sim_time` if drones move too quickly or too slowly to avoid premature termination. Ensure building positions are preloaded in replay data to avoid fallback metrics.
