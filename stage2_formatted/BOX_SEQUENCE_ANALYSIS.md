**Tags:** #optimization, #box-sequence, #backend-frontend-integration, #asynchronous-processing, #parallelization, #caching, #terrain-generation
**Created:** 2026-01-13
**Type:** architecture

# BOX_SEQUENCE_ANALYSIS

## Summary

```
Analyzes and optimizes the box-based map generation workflow, highlighting bottlenecks and proposing parallelized, cached, and streamed improvements for faster and more efficient map creation.
```

## Details

> This document analyzes the current box sequence for map generation, detailing both frontend and backend flows. The current system relies on sequential box execution and polling, leading to latency and inefficiency. The backend uses a service-based async job system with heavy reliance on `WorldTypeTerrainGeneratorBox` and `WorldTypeHeightmapGeneratorBox`, which perform redundant steps like terrain generation followed by cell mapping. The analysis identifies performance bottlenecks, including polling delays, redundant computations, and lack of parallelization.

## Key Functions

### `generateMapParameters()`

Frontend function to collect map generation parameters.

### `generateMap()`

Initiates async job creation via `MapGeneratorServiceBox`.

### `startMapStatusPolling()`

Continuously checks job status via `MapGeneratorServiceBox.status()`.

### `fetchMapResult()`

Retrieves processed map data after job completion.

### `WorldTypeTerrainGeneratorBox.generate_terrain()`

Core backend function generating terrain arrays.

### `WorldTypeHeightmapGeneratorBox.generate_heightmap()`

Maps terrain to Voronoi cells and calculates heights.

### `HashGeneratorMasterBox`

Manages hash-based operations for seed generation and cell hashing.

### `HashBasedHeightmapUtilsBox`

Provides utility functions for cell hashing and height assignment.

### `MapProcessBox`

Converts raw map data into Azgaar format for display.

### `useMapGeneration.js`

Direct composable for quick map generation (alternative flow).

## Usage

1. **Current Workflow**: User triggers generation via frontend, which polls backend status until completion. Backend processes data in sequential steps.
2. **Optimized Workflow**: Proposed to use parallel execution, caching, and direct box calls for faster preview maps. Full maps still use async jobs but leverage optimizations like parallel cell hashing and intermediate caching.

## Dependencies

> `- Frontend: `GenerateStage.vue``
> ``MapPreview``
> ``MapGeneratorServiceBox`
- Backend: `world_type_heightmap_generator.py``
> ``HashBasedHeightmapUtilsBox``
> ``HashGeneratorMasterBox`
- External APIs: `/api/generation/maps``
> ``/api/map-generator/generate``
> ``/api/generation/terrain``
> ``/api/generation/heightmap``

## Related

- [[BOX_SEQUENCE_DESIGN]]
- [[MAP_GENERATION_API_DOCS]]
- [[BACKEND_SERVICE_OPTIMIZATIONS]]

>[!INFO] **Parallelization Opportunity**
> The `HashBasedHeightmapUtilsBox` and `WorldTypeHeightmapGeneratorBox` can run cell hashing and height calculations concurrently, reducing overall generation time by up to 30-50%.

>[!WARNING] **Caching Risks**
> Over-caching may lead to stale data if hash inputs change frequently. Ensure cache invalidation logic is robust for dynamic maps.

>[!INFO] **Streaming Consideration**
> Implementing streaming for terrain chunks could reduce memory usage and improve real-time UI updates, though this requires backend support for chunked responses.
