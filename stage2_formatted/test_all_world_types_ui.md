**Tags:** #unit-test, #terrain-generation, #world-types, #procedural-generation, #numpy-analysis
**Created:** 2026-01-13
**Type:** code-test

# test_all_world_types_ui

## Summary

```
Script validates procedural terrain generation across diverse world types for uniqueness and correctness.
```

## Details

> This script tests a `WorldTypeTerrainGeneratorBox` component by generating terrain samples for predefined world types (e.g., "planet," "galaxy") and analyzing statistical properties (mean, standard deviation, min/max values). It verifies whether each world type produces distinct terrain distributions by comparing statistical metrics across runs. The test framework uses NumPy for numerical analysis and outputs success/failure metrics for each case.

## Key Functions

### `test_world_type(world_type, hash_desc)`

Executes terrain generation for a single world type and returns statistical metrics.

### `test_all_world_types_ui()`

Orchestrates the test suite, runs all predefined cases, and performs statistical differentiation analysis.

## Usage

1. Run the script directly to execute all predefined world type tests.
2. The script prints real-time test results and a final analysis of terrain uniqueness.
3. Output includes success/failure status, mean/std ranges, and statistical comparisons.

## Dependencies

> ``numpy``
> ``backend/boxes.generators.world_type_terrain_generator_box``
> ``backend/boxes.core.box_interface``

## Related

- [[boxes.generators]]
- [[boxes.core]]

>[!INFO] Important Note
> The script uses a predefined list of world types (`test_cases`) with descriptive hashes. These are hardcoded for testing but should ideally be configurable or derived dynamically from a world type registry.

>[!WARNING] Caution
> If terrain generation fails silently (e.g., due to missing dependencies or invalid inputs), the script will still proceed but mark the test as failed. Ensure the `WorldTypeTerrainGeneratorBox` is properly initialized and the backend environment is correctly set up.
