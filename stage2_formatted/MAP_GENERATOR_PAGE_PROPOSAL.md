**Tags:** #architecture, #optimization, #proposal, #map-generation, #asynchronous-processing, #ui-design, #backend-frontend-integration
**Created:** 2026-01-13
**Type:** architecture-proposal

# MAP_GENERATOR_PAGE_PROPOSAL

## Summary

```
Proposes a dedicated `/map-generator` page to streamline and optimize map generation workflows with real-time preview and parallel processing.
```

## Details

> This proposal introduces a dedicated page (`/map-generator`) to replace scattered map generation and viewing functionalities, addressing performance bottlenecks and user experience gaps. The solution leverages parallel execution, caching, and modular box-based architecture to drastically reduce generation times (e.g., quick preview now under 0.1s). The design splits large monolithic boxes into smaller, single-responsibility components (e.g., `CellMappingBox`, `HeightVariationBox`) for better maintainability and reusability. The UI integrates a real-time 2D viewer (`WorldMap2D`) and supports streaming updates, while backend caching invalidates results on hash changes. The phased implementation ensures backward compatibility while optimizing performance through lazy loading and Web Workers.

## Key Functions

### `WorldTypeHeightmapGeneratorBox`

Orchestrates terrain and heightmap generation (refactored into smaller boxes).

### `CellMappingBox`

Maps 2D terrain coordinates to Voronoi cells for biome/city placement.

### `HashGeneratorMasterBox`

Generates base hash inputs for terrain and heightmap generation.

### `WorldMap2D`

Integrated 2D viewer displaying generated maps in real-time.

### `MapGeneratorPage.vue`

Frontend page handling user input, selection, and preview rendering.

### `TerrainCacheBox`

Backend cache for terrain data (keyed by world parameters).

### `HeightmapCacheBox`

Backend cache for heightmap data (keyed by hash and world type).

## Usage

1. Navigate to `/map-generator` in the UI.
2. Input a hash (e.g., "rocky planet with mountains") and select a **World Type** (e.g., "Planet").
3. Choose a **Map Type** (Quick Preview, Full Map, or Custom).
4. Click **Generate**—the map renders instantly (or progressively) in the 2D viewer.
5. Adjust inputs dynamically to see real-time updates.
6. Switch to **Full Map** to generate biomes/cities (takes <5s).
7. Save the map to a world for later use.

## Dependencies

> ``backend/boxes/generators``
> ``backend/boxes/cache``
> ``ui-beta/src/boxes/generators``
> ``ui-beta/src/pages``
> ``ui-beta/src/composables``
> ``WorldMap2D` (2D viewer component)`
> ``HashBasedHeightmapUtilsBox` (parallel hash utilities).`

## Related

- [[Map_Generator_Architecture_Diagram]]
- [[Backend_UI_Integration_Guide]]
- [[Performance_Optimization_Notes]]

>[!INFO] **Parallel Execution**
> Parallelizing cell hash operations (e.g., `HashBasedHeightmapUtilsBox`) across all cells reduces latency by distributing workloads across CPU cores.

>[!WARNING] **Cache Invalidation**
> Ensure `TerrainCacheBox` and `HeightmapCacheBox` invalidate cached data when the user modifies the input hash to avoid stale results.

>[!INFO] **Lazy Loading**
> Implement lazy loading for visible cells only to balance performance and memory usage during full-map generation.

>[!WARNING] **Web Workers**
> Offload heavy computations (e.g., Voronoi generation) to Web Workers to prevent UI freezing during long operations.
