**Tags:** #exploration, #pybullet, #drones, #simulation, #ground_truth, #docker, #drone_autonomy
**Created:** 2026-01-13
**Type:** code-notes

# simple_exploration_test

## Summary

```
Test script for drone exploration in a 3D simulation environment using PyBullet, logging ground truth and telemetry data.
```

## Details

> This script simulates a drone exploring a 3D environment, spawning random objects and logging their positions and sizes via a `GroundTruthLogger`. The `BaseStation` class captures drone telemetry (e.g., position) and records discoveries. The simulation runs in a Docker container with PyBullet, requiring external dependencies like `pybullet` and `numpy`. The script logs data to JSON files for analysis, with ground truth data hidden from the command-and-control system.

## Key Functions

### `GroundTruthLogger.log_object`

Records metadata (shape, position, size) of spawned objects in a hidden log.

### `BaseStation.receive_telemetry`

Processes drone telemetry data (e.g., position) and stores it for later analysis.

### `GroundTruthLogger._save`

Writes logged object data to a JSON file in the scenarios directory.

## Usage

1. Run in Docker: `docker compose -f simulation/docker/docker-compose.yml run --rm simulator python /app/scenarios/simple_exploration_test.py`.
2. The script spawns objects, logs ground truth, and records drone telemetry.
3. Logs are saved to `ground_truth_log.json` and `base_station_log.json` in the scenarios directory.

## Dependencies

> `pybullet`
> `pybullet_data`
> `numpy`
> `docker-compose (for Docker execution)`

## Related

- [[docker-compose]]
- [[drone_autonomy_architecture]]

>[!INFO] Important Note
> The `GroundTruthLogger` prints hidden object data to the console for testing purposes, but this data is not accessible to the command-and-control system (C&C). The script assumes a drone (`drone_data`) is passed to `receive_telemetry`; ensure this is implemented in the full workflow.

>[!WARNING] Caution
> If PyBullet is not installed, the script exits with an error. Ensure the Docker container includes `pybullet` and `pybullet_data` in its `docker-compose.yml` file. The script also requires `numpy` for numerical operations.
