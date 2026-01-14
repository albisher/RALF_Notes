**Tags:** #map-generation, #procedural-generation, #game-world, #retries-and-validation
**Created:** 2026-01-13
**Type:** code-notes

# map_generator

## Summary

```
Orchestrates procedural map generation with retry logic for validation failures.
```

## Details

> The `MapGenerator` class serves as a central orchestrator for generating procedural maps, integrating components like Voronoi diagrams, heightmaps, biomes, and city placements. It handles resolution presets, parameter validation, and retry logic to ensure map integrity. The system uses a modular design, delegating specific tasks to submodules (e.g., `VoronoiGenerator`, `HeightmapGenerator`) while managing workflows like progress tracking and error recovery.
> 
> The `generate()` method initiates the process, while `_generate_single_attempt()` coordinates the internal workflow. Retry logic dynamically adjusts seeds and validates results, ensuring robustness against generation failures.

## Key Functions

### `generate()`

Orchestrates map generation with retry logic, validation checks, and progress callbacks.

### `_generate_single_attempt()`

Core internal method that delegates sub-tasks (e.g., Voronoi, heightmap, biome generation) while tracking progress.

### `resolution_presets`

Configures predefined map dimensions (cells, width, height) for different resolutions (low/medium/high/ultra).

## Usage

1. Initialize `MapGenerator()`.
2. Call `generate()` with parameters like `seed`, `resolution`, or custom dimensions.
3. Handle progress callbacks (e.g., for UI updates) and validation results.

## Dependencies

> ``.voronoi_generator``
> ``.heightmap_generator``
> ``.biome_calculator``
> ``.world_type_biome_calculator``
> ``.city_placer``
> ``.world_type_voronoi_generator``
> ``.world_type_heightmap_generator``
> ``.world_type_city_placer``
> ``logging``
> ``hashlib``

## Related

- [[Procedural Generation Workflow]]
- [[Validation Framework]]

>[!INFO] Retry Mechanism
> Uses SHA-256 hashing to modify seeds during retries, ensuring deterministic yet varied attempts for validation recovery.

>[!WARNING] Validation Failure
> If validation fails after `max_retries`, the method returns the map despite potential issues, prioritizing progress over strict correctness.
