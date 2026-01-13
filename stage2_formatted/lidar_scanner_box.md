**Tags:** #simulation, #robotics, #sensor, #pybullet, #lidar, #point_cloud, #physics
**Created:** 2026-01-13
**Type:** code-notes

# lidar_scanner_box

## Summary

```
Configurable LiDAR scanner for PyBullet simulations, supporting real-world sensor presets and custom configurations.
```

## Details

> The `LiDARScannerBox` class implements a LiDAR sensor capable of ray casting to generate point cloud data. It uses PyBullet for physics simulations and supports predefined LiDAR models (e.g., Velodyne VLP-16, HDL-64) or custom configurations. The class initializes with configurable parameters like field-of-view (FOV), resolution, range limits, and noise, and returns a point cloud array, object reflections, and scan statistics. It relies on PyBullet for ray casting and physics interactions.

## Key Functions

### ``__init__``

Initializes the LiDAR scanner with physics client and sensor parameters (preset or custom).

### ``SENSOR_PRESETS``

Dictionary mapping sensor models to their configurations (channels, FOV, resolution, range).

## Usage

1. Instantiate with a PyBullet physics client and sensor configuration (e.g., `LiDARScannerBox(physics_client, sensor_model='VLP-16')`).
2. Call `scan()` (implicitly via physics interactions) to generate point cloud data.
3. Access outputs like `point_cloud`, `reflections`, or `scan_stats` after scanning.

## Dependencies

> `pybullet`
> `numpy`

## Related

- [[PyBullet Physics Client Documentation]]
- [[LiDAR Sensor Calibration Guide]]

>[!INFO] Sensor Presets
> The `SENSOR_PRESETS` dict defines real-world LiDAR specs. Override parameters via constructor args for flexibility.

>[!WARNING] Physics Dependency
> Requires a valid PyBullet client ID. Invalid IDs may cause crashes. Always validate `physics_client` before use.
