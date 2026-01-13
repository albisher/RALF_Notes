**Tags:** #LiDAR, #3D_mapping, #drone_automation, #voxel_grid, #ray_casting, #simulation
**Created:** 2026-01-13
**Type:** documentation

# LIDAR_3D_MAPPING_EXPLANATION

## Summary

```
Explains the LiDAR 3D surface mapping pipeline for drone-based object detection and spatial data accumulation.
```

## Details

> This document outlines a multi-step process where a drone’s LiDAR system casts 1,920 rays per scan (16 vertical channels × 120 horizontal rays) to detect 3D surfaces. The raw hits are transmitted to a base station, which accumulates all points and object reflections. The final step involves voxelizing these points into a 3D grid (1cm resolution) to map surfaces and track object reflections.

## Key Functions

### `LiDARScannerBox`

Handles ray generation, batch casting, and object reflection detection via PyBullet.

### `Drone → Base Station Transmission`

Encapsulates scan results in telemetry for data aggregation.

### `BaseStationBox`

Accumulates all LiDAR points and object reflections from multiple drones.

### `AdvancedLiDARBox`

Converts raw point clouds into a voxelized 3D surface map with per-voxel metadata (position, count, last seen).

## Usage

1. Deploy `LiDARScannerBox` on drones to generate point clouds.
2. Use `Drone → Base Station` telemetry to transmit raw data.
3. Aggregate data in `BaseStationBox` for global accumulation.
4. Process data in `AdvancedLiDARBox` to create a voxelized 3D map.

## Dependencies

> `PyBullet`
> `NumPy`
> `drone simulation libraries (e.g.`
> ``simulation/swarm` modules).`

## Related

- [[lidar_scanner_box]]
- [[base_station_box]]
- [[advanced_lidar_box]]

>[!INFO] Important Note
> The voxel resolution (`map_resolution = 0.01m`) balances detail and computational efficiency. Lower values increase accuracy but memory usage.

>[!WARNING] Caution
> Ground-plane filtering (`hit_object_id != ground_plane_id`) must be precise to avoid misclassifying surfaces. Incorrect thresholds may introduce noise in voxelization.
