**Tags:** #LiDAR_processing, #building_analysis, #drone_mapping, #3D_modeling, #data_structures, #scout_drone
**Created:** 2026-01-13
**Type:** code-notes

# building_mapper

## Summary

```
Processes LiDAR data to generate building models with coordinates, shapes, and metadata for Scout drone inspections.
```

## Details

> The `building_mapper` module implements a system to extract and store building information from LiDAR point clouds. It uses a `BuildingModel` dataclass to organize data like coordinates, shape, windows, cracks, and metadata. The `BuildingMapper` class manages storage, retrieval, and processing of building data, initializing with a storage path and loading existing models. The core function `create_building_from_lidar` processes raw LiDAR data to generate a structured building model without requiring CAD inputs.

## Key Functions

### `BuildingModel`

Stores all metadata for a building, including coordinates, shape, windows, cracks, and mapping errors.

### `BuildingMapper`

Manages the lifecycle of building models—initialization, storage, and loading from LiDAR data.

### `create_building_from_lidar`

Processes LiDAR point clouds into a `BuildingModel` instance (incomplete snippet shown; likely includes shape extraction logic).

## Usage

1. Initialize `BuildingMapper` with a storage directory.
2. Use `create_building_from_lidar` to process LiDAR data into a `BuildingModel`.
3. Retrieve or save models via `self.buildings` dictionary or file storage.

## Dependencies

> `numpy`
> `typing`
> `json`
> `os`
> `datetime`
> `dataclasses`

## Related

- [[buildings]]
- [[LiDAR_processing_guide]]

>[!INFO] In-Memory Cache
> The `buildings` dictionary caches models in memory; use `_load_buildings()` to load from disk before processing.

>[!WARNING] LiDAR Input Validation
> Ensure `lidar_point_cloud` is a valid Nx3 NumPy array; invalid inputs may cause crashes.
