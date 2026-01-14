**Tags:** #heightmap-generation, #world-generation, #procedural-terrain, #deterministic-randomness, #box-based-algorithms
**Created:** 2026-01-13
**Type:** code-notes

# world_type_heightmap_generator

## Summary

```
Generates world-specific heightmaps using deterministic methods with fallback to simpler algorithms when box-based generation fails.
```

## Details

> This script implements a **world-type-aware heightmap generator**, dynamically adapting terrain patterns (e.g., mountains, plateaus) based on input parameters like `world_type` (e.g., "fantasy_planet," "asteroid"). It prioritizes a **box-based backend** for efficiency and determinism but falls back to a hash-based algorithm if unavailable. The generator processes Voronoi cells, applies world-specific logic (e.g., sea-level adjustments), and returns a dictionary mapping cell indices to height values. Key features include:
> - **Categorization**: Automatically classifies worlds (e.g., "cloud_world" vs. "moon") via keyword checks in `world_type` or `world_description`.
> - **Hybrid Approach**: Combines a fast, deterministic box-based method with a fallback to simpler randomness (e.g., Gaussian peaks) when needed.
> - **Deterministic Seeding**: Uses MD5 hashing to ensure reproducibility across runs.

## Key Functions

### ``WorldTypeHeightmapGenerator``

Core class initializing the generator with a seed and world type. Handles categorization and delegates generation to specialized methods.

### ``_categorize_world``

Classifies the world into predefined categories (e.g., "space_station") based on input strings.

### ``generate_heightmap``

Orchestrates the generation process, first attempting the box-based method, then falling back to world-specific subroutines.

### ``_generate_planet_heightmap``

Default method for "fantasy_planet" worlds, using a research-based hash-based algorithm (or fallback to simple peaks).

### ``_generate_galaxy_heightmap``

Specialized for "galaxy" worlds (e.g., star systems), likely involving noise-based or fractal patterns.

### ``_generate_station_heightmap``

Simplified for "space_station" (e.g., craters, flat surfaces).

### ``_generate_asteroid_heightmap``

Generates jagged, irregular heights for asteroids.

### ``_generate_moon_heightmap``

Applies smooth, cratered terrain logic.

### ``_generate_cloud_world_heightmap``

Handles floating terrain (e.g., clouds) with minimal elevation changes.

## Usage

1. **Initialize**: Create an instance with `WorldTypeHeightmapGenerator(seed="my_seed", world_type="fantasy_planet")`.
2. **Generate**: Call `generate_heightmap(cells=[...], sea_level=0.2)` with a list of Voronoi cells and optional `sea_level` adjustment.
3. **Fallback Handling**: If the box-based method fails, the script logs a warning and uses a simpler algorithm (e.g., Gaussian peaks).

## Dependencies

> ``numpy``
> ``hashlib``
> ``random``
> ``sys``
> ``os``
> ``logging``
> ``boxes.generators.world_type_heightmap_generator_box``
> ``boxes.core.box_interface``
> ``.terrain_formation` (local module).`

## Related

- [[World Generation Engine]]
- [[Procedural Terrain Research Notes]]
- [[Box-Based Algorithms]]

>[!INFO] Deterministic Seeding
> The script uses MD5 hashing to convert the input `seed` into a deterministic 32-bit integer, ensuring identical results across runs with the same seed. This is critical for reproducibility in game/environment generation.

>[!WARNING] Box Dependency
> If the box-based backend (`WorldTypeHeightmapGeneratorBox`) is unavailable, the script falls back to a slower, less optimized method. Test thoroughly in production to avoid inconsistencies.
