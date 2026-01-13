**Tags:** #drone-telemetry, #data-processing, #IoT, #sensor-data, #real-time, #autonomous-systems
**Created:** 2026-01-13
**Type:** code-notes

# base_station_box

## Summary

```
Processes and stores drone telemetry data for path tracking, crash detection, and LiDAR point accumulation.
```

## Details

> The `BaseStationBox` class handles telemetry reception from drones, storing raw data, tracking flight paths, accumulating LiDAR points, and logging crash events. It uses a timestamped buffer (`received_data`) to store processed telemetry, while `drone_path` records sequential positions. LiDAR points are merged into `discovered_points`, and object reflections are tracked in `object_reflections`. Crash detection checks for collision events or crash reports, logging them if a `LoggingBox` is provided.

## Key Functions

### ``receive_telemetry``

Parses and stores drone telemetry data (position, orientation, LiDAR points, etc.) into internal buffers.

### ``__init__``

Initializes buffers (`received_data`, `discovered_points`, etc.) and sets up logging infrastructure.

## Usage

1. Instantiate `BaseStationBox` (e.g., `box = BaseStationBox(logging_box=FrontendLogger())`).
2. Call `receive_telemetry(drone_data)` with a dictionary containing drone telemetry (e.g., `box.receive_telemetry({"position": [1, 2, 3], "lidar_points": [...]})`).
3. Retrieve processed data via instance attributes (e.g., `box.received_data`, `box.discovered_points`).

## Dependencies

> `numpy`
> `datetime`
> `json (implicitly via `datetime`)`
> `logging_box (optional external dependency).`

## Related

- [[drone_telemetry_processing_guide]]
- [[logging_system_architecture]]

>[!WARNING] Crash Handling
> The code attempts to append `crash_reports` but uses `self.crash_reports` (undefined). Fix by initializing `self.crash_reports = []` in `__init__`.

>[!INFO] Logging
> Logging is conditional on `self.logging_box`; ensure it implements a `log()` method for frontend integration.
