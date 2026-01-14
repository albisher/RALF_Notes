**Tags:** #test, #world-generation, #hash-based-heightmap, #procedural-generation, #unit-testing
**Created:** 2026-01-13
**Type:** code-test

# test_map_generation_all_types

## Summary

```
Tests hash-based heightmap generation across multiple world types for procedural map creation.
```

## Details

> This script validates the new hash-based heightmap generation system by testing it against predefined world types (planet, galaxy, cloud-world, etc.). It creates test Voronoi cells, applies the generator for each world type, and evaluates success/failure based on heightmap generation. The test outputs statistics (average/min/max heights) and saves results to JSON for analysis.

## Key Functions

### `create_test_cells(num_cells)`

Generates distributed Voronoi cells for testing.

### `test_world_type(world_type, world_hash, cells)`

Executes heightmap generation for a specific world type with given inputs.

### `main()`

Orchestrates testing across all world types, collects results, and reports success/failure metrics.

## Usage

1. Run script directly (`python test_map_generation_all_types.py`).
2. Script automatically:
   - Creates test cells.
   - Tests each world type with predefined hash and description.
   - Prints success/failure stats and saves results to `screenshots/map_generation_tests/test_results.json`.

## Dependencies

> ``sys``
> ``os``
> ``json``
> ``pathlib``
> ``backend` (local module)`
> ``boxes.generators.world_type_heightmap_generator_box``
> ``boxes.core.box_interface``

## Related

- [[generators (Core procedural generation logic)
test_map_generation_basic (Basic heightmap tests)]]

>[!INFO] Test Structure
> Each world type is tested with identical cells but unique `world_hash` to simulate distinct environments. The script validates heightmap generation consistency across types.

>[!WARNING] Error Handling
> Failed tests log errors but continue execution—results are still saved to preserve data integrity.
