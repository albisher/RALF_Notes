**Tags:** #lidar, #3d_mapping, #real_time_processing, #surface_reconstruction, #obstacle_detection, #voxelization
**Created:** 2026-01-13
**Type:** code-notes

# advanced_lidar_box

## Summary

```
Advanced LiDAR box for real-time 3D mapping, obstacle classification, and surface degradation analysis.
```

## Details

> This class extends `LiDARProcessorBox` to handle real-time 3D surface mapping using LiDAR point clouds. It processes input data into a voxelized 3D map (`surface_map`), tracks obstacle types (`obstacle_map`), and generates a degradation heatmap (`degradation_map`). The system uses configurable resolution parameters (e.g., 1cm) for spatial precision and rounds point coordinates to map voxel boundaries. The `update_surface_map` method populates the voxel grid with point cloud data, incrementing counts for repeated voxels and tracking metadata like last seen position.

## Key Functions

### ``update_surface_map``

Processes incoming point clouds into voxelized 3D map entries, returning statistics (new/total points) and map bounds.

### ``__init__``

Initializes the box with configurable parameters (e.g., `num_channels`, `map_resolution`) and preallocates data structures (`surface_map`, `obstacle_map`, `degradation_map`).

## Usage

1. Instantiate `AdvancedLiDARBox` with desired parameters (e.g., `map_resolution=0.01` for 1cm).
2. Call `update_surface_map(point_cloud, position)` with raw LiDAR data and drone position.
3. Access results via `self.surface_map`, `self.obstacle_map`, or `self.degradation_map`.

## Dependencies

> `numpy`
> ``.lidar_processor_box` (parent class)`

## Related

- [[lidar_processor_box]]
- [[surface_reconstruction_guide]]

>[!INFO] Voxelization Note
> Voxel coordinates are rounded to the nearest integer multiple of `map_resolution`, ensuring uniform grid alignment. Overlapping points increment voxel counts, enabling density-based surface reconstruction.

>[!WARNING] Edge Case Handling
> Empty point clouds return minimal metadata; ensure `point_cloud` is non-empty for meaningful updates.
