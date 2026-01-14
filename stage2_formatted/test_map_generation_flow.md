**Tags:** #test, #map_generation, #terrain_generation, #heightmap_generation, #world_types, #unit_test
**Created:** 2026-01-13
**Type:** code-test

# test_map_generation_flow

## Summary

```
Tests the complete workflow of terrain and heightmap generation for different world types in a procedural generation system.
```

## Details

> This script validates the functionality of terrain and heightmap generation modules within a world-building system. It verifies:
> 1. **Terrain generation** for a specified world type (e.g., "planet") with configurable dimensions.
> 2. **Heightmap generation** using predefined grid cells and a sea-level threshold.
> 3. **Cross-world type compatibility** by testing multiple predefined world types (planet, galaxy, cloud world).
> 
> The tests output success/failure statuses, sample data, and error messages for debugging.

## Key Functions

### `test_terrain_generation()`

Validates terrain generation logic with a given world hash and dimensions.

### `test_heightmap_generation()`

Tests heightmap generation using a 10x10 grid of cells and a sea-level parameter.

### `test_different_world_types()`

Compares terrain generation across multiple world types (planet, galaxy, cloud world).

### `main()`

Orchestrates all tests, aggregates results, and provides a summary of pass/fail statuses.

## Usage

1. Run the script directly (`python test_map_generation_flow.py`).
2. The script automatically imports required modules from the `backend` directory.
3. Outputs test progress, results, and a summary of pass/fail statuses.

## Dependencies

> ``backend/boxes.generators.world_type_terrain_generator_box``
> ``backend/boxes.generators.world_type_heightmap_generator_box``
> ``backend/boxes.core.box_interface``
> `Python standard libraries (`sys``
> ``json`).`

## Related

- [[boxes.generators]]
- [[boxes.generators]]
- [[boxes.core]]

>[!INFO] Important Note
> This script relies on the `BoxInput` and `BoxResult` interfaces defined in `backend/boxes.core.box_interface` to pass data to generator boxes. Ensure these interfaces are correctly implemented for the tests to run as expected.

>[!WARNING] Caution
> If the `world_hash` or `world_type` parameters are not recognized by the generator boxes, the tests may fail silently with invalid terrain/heightmap results. Always check error messages for mismatches.
