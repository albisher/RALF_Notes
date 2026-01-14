**Tags:** #algorithm, #hash-based, #terrain-generation, #low-resolution, #world-type, #numerical-computation, #caching, #numpy, #box-system
**Created:** 2026-01-13
**Type:** code-notes

# world_type_terrain_generator_box

## Summary

```
Generates low-resolution terrain maps (64–256px) for different world types using hash-based algorithms.
```

## Details

> This module implements a **Box-based** terrain generator that produces simplified heightmaps (0.0–1.0) for various world types (e.g., planets, galaxies, clouds). It leverages a hash-based approach for deterministic, fast generation, with optional caching to avoid redundant computations. The system delegates terrain-specific logic (e.g., spiral arms for galaxies) to helper methods while defaulting to a generic planet-like pattern. Inputs include `world_hash`, `world_type`, and resolution dimensions, which are validated and cached for reuse.

## Key Functions

### ``execute(input_data)``

Orchestrates terrain generation, checks cache, and returns results as a `BoxOutput`. Handles errors gracefully.

### ``generate_terrain(world_hash, world_type, width, height)``

Dispatches generation to the appropriate sub-method based on `world_type`.

### ``_generate_galaxy_terrain()``

Creates spiral-arm patterns using hash-derived parameters (e.g., arm count, tightness).

### ``_generate_cloud_terrain()``

Simulates cloud-based terrain (placeholder logic).

### ``_generate_planet_terrain()``

Default planet-like noise-based terrain (simplified).

### ``_generate_station_asteroid()``

Specialized for small bodies (e.g., moons, ships).

### ``_generate_simple_terrain()``

Fallback for non-Numpy environments.

## Usage

1. Initialize `WorldTypeTerrainGeneratorBox()`.
2. Call `execute()` with a `BoxInput` containing:
   - `"operation": "generate_terrain"`
   - Required fields: `world_hash`, `world_type`, `width`, `height` (default: 128x128).
3. Retrieve the generated `terrain` (as a list for JSON serialization).

## Dependencies

> ``numpy` (optional`
> `fallback to string hashing)`
> ``hashlib``
> ``logging``
> ``Box``
> ``HashBasedHeightmapUtilsBox``
> ``HashGeneratorMasterBox`.`

## Related

- [[`HashBasedHeightmapUtilsBox`]]
- [[`HashGeneratorMasterBox`]]
- [[`core.box_interface`.]]

>[!INFO] Cache Behavior
> Uses an in-memory LRU cache (`_cache`) with a max size of 50 entries. Oldest entries are evicted when exceeding the limit.

>[!WARNING] Fallback Logic
> If `numpy` is unavailable, it switches to a simplified string-hashing approach, reducing precision for complex terrain types.
