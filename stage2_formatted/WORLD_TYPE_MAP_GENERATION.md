**Tags:** #world-generation, #deterministic-algorithm, #procedural-content, #oop-design, #hash-based-seeding
**Created:** 2026-01-13
**Type:** code-notes

# WORLD_TYPE_MAP_GENERATION

## Summary

```
Generates world maps with world-type-specific patterns using deterministic hash-based logic for procedural content generation.
```

## Details

> This system dynamically creates unique maps by applying world-type-specific algorithms (Voronoi cell patterns, heightmaps, biome assignments, and city placements) based on user-selected `world_type` and a provided hash. The architecture uses an object-oriented approach with a box pattern, where each component (e.g., Voronoi generator, heightmap generator) adapts its logic based on the world type while maintaining deterministic results via the hash. The frontend passes world context to an orchestrator (`MapGenerator`), which delegates generation to specialized services.

## Key Functions

### `WorldTypeVoronoiGenerator`

Generates cell patterns (e.g., spiral arms for Galaxy, cloud clusters for Cloud World) using the hash to determine distribution.

### `WorldTypeHeightmapGenerator`

Creates terrain shapes (e.g., energy gradients for Galaxy, cloud density for Cloud World) based on hash-derived elevation rules.

### `WorldTypeBiomeCalculator`

Assigns biomes/regions (e.g., nebula, star_cluster for Galaxy; cloud_platform, storm_cloud for Cloud World) using temperature/precipitation derived from heightmaps.

### `WorldTypeCityPlacer`

Places and names settlements (e.g., "Nebula Alpha" for Galaxy; "Sky City" for Cloud World) deterministically via hash-indexed logic.

### `MapGenerator`

Orchestrates the full workflow, passing world_type and hash to specialized generators.

### `Vue Integration`

Frontend component (`GenerateStage.vue`) forwards world context to the backend via a box system.

## Usage

1. User selects `world_type` (e.g., "Galaxy") and provides a hash/description.
2. Frontend (`GenerateStage.vue`) packages context into `params` and sends it to `MapGeneratorServiceBox`.
3. Backend processes `params` via `MapGenerator.generate()`, which routes to world-type-specific generators.
4. Each generator uses the hash to produce deterministic outputs (e.g., Voronoi cells, heightmaps, biomes, cities).
5. Results are returned to the frontend for rendering.

## Dependencies

> ``services/map-generator/engine/world_type_voronoi_generator.py``
> ``services/map-generator/engine/world_type_heightmap_generator.py``
> ``services/map-generator/engine/world_type_biome_calculator.py``
> ``services/map-generator/engine/world_type_city_placer.py``
> ``services/map-generator/api.py``
> ``MapGeneratorServiceBox` (Vue backend adapter).`

## Related

- [[`WORLD_TYPE_MAP_GENERATION_ARCHITECTURE`]]
- [[`PROCEDURAL_GENERATION_GUIDELINES`]]
- [[`HASH_BASED_SEEDING`.]]

>[!INFO] Deterministic Guarantee
> The same `world_type` + hash combination always produces identical maps, ensuring reproducibility for users.

>[!WARNING] Hash Sensitivity
> Minor hash changes (e.g., typos) may drastically alter map structure, so input validation is critical.
