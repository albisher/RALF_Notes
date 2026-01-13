**Tags:** #simulation, #test-drone, #pybullet, #exploration, #3d-objects, #waypoints, #lidar, #telemetry, #command-control
**Created:** 2026-01-13
**Type:** code-notes

# SIMPLE_TEST_READY

## Summary

```
A modular drone exploration test script using PyBullet, featuring hidden 3D objects, predefined waypoints, and real-time telemetry logging.
```

## Details

> This script implements a **drone exploration scenario** where a simulated drone navigates predefined waypoints while avoiding hidden 3D objects (cubes, spheres, cylinders). The simulation uses PyBullet for physics, with ground truth data logged separately. The drone’s LiDAR scans at each waypoint, and telemetry is streamed to a base station. The test includes a structured log system for validation, ensuring safe operation in a 15-45m area.

## Key Functions

### ``simulate_exploration()``

Orchestrates the entire mission, including object spawning, drone waypoint navigation, and LiDAR scanning.

### ``spawn_random_objects()``

Generates 5 hidden 3D objects with randomized positions and sizes.

### ``define_waypoints()``

Configures 6 predefined waypoints for drone navigation, including a return-to-base endpoint.

### ``log_ground_truth()``

Records object positions and metadata in a JSON log file.

### ``process_telemetry()``

Captures drone position, orientation, and LiDAR data for real-time monitoring.

## Usage

1. Install dependencies (`pip install pybullet numpy`).
2. Navigate to the `simulation/scripts/scenarios` directory.
3. Execute the script (`python simple_exploration_test.py`).
4. Observe the console output and PyBullet window for real-time simulation.

## Dependencies

> `PyBullet`
> `NumPy`
> `JSON libraries (standard Python packages).`

## Related

- [[README]]
- [[PyBullet documentation]]

>[!INFO] Important Note
> The drone spawns at `(0, 0, 5)` to avoid immediate collisions with objects, which are hidden from the command & control system. Ground truth logs (`ground_truth_log.json`) contain object positions, ensuring validation against hidden objects.


>[!WARNING] Caution
> The simulation area (15-45m) is intentionally large to prevent collisions, but ensure the drone’s LiDAR range (5.21m–32.45m) aligns with expected sensor capabilities. Overlapping scans may cause redundant data but do not affect mission integrity.
