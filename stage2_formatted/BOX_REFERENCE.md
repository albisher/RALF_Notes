**Tags:** #map-generation, #backend-frontend-integration, #procedural-generation, #box-pattern, #asynchronous-jobs
**Created:** 2026-01-13
**Type:** documentation

# BOX_REFERENCE

## Summary

```
Detailed reference for JavaScript/Python box components used in procedural world map generation, covering terrain, heightmap, and async job management.
```

## Details

> This document outlines frontend and backend box implementations for a modular map generation system. Frontend boxes (`WorldTypeTerrainGeneratorBox`, `WorldTypeHeightmapGeneratorBox`) serve as HTTP wrappers around backend generators, while backend boxes (`WorldTypeTerrainGeneratorBox`, `WorldTypeHeightmapGeneratorBox`) implement core procedural logic using hash-based algorithms. The `MapGeneratorServiceBox` manages asynchronous job workflows via REST endpoints, enabling decoupled frontend/backend interactions.
> 
> Key workflows include:
> 1. **Terrain Generation**: Converts world parameters into 2D height arrays via hash-based noise functions.
> 2. **Heightmap Assignment**: Maps terrain values to Voronoi cells using seed-based algorithms.
> 3. **Job Orchestration**: Frontend initiates async generation jobs, backend processes them, and returns results via status checks.

## Key Functions

### ``WorldTypeTerrainGeneratorBox` (frontend/backend)`

Generates 2D terrain arrays using hash-based procedural generation.

### ``WorldTypeHeightmapGeneratorBox` (frontend/backend)`

Creates height value dictionaries for Voronoi cells with configurable sea levels.

### ``MapGeneratorServiceBox``

Manages async map generation workflows with `generate()`, `status()`, and `result()` endpoints.

### ``GenerationAPIBox``

Flask blueprint hosting `/api/generation/terrain` and `/api/generation/cells` endpoints.

## Usage

1. **Frontend Usage**:
   - Initialize `apiClient` for HTTP requests.
   - Call `WorldTypeTerrainGeneratorBox.generate_terrain()` with `world_hash`, `world_type`, and dimensions.
   - Use `MapGeneratorServiceBox` for async jobs via `generate()` → `status()` → `result()`.

2. **Backend Setup**:
   - Register `GenerationAPIBox` in Flask app.
   - Initialize `WorldTypeTerrainGeneratorBox`/`WorldTypeHeightmapGeneratorBox` with dependencies.
   - Configure `/api/generation/terrain` and `/api/generation/cells` endpoints to route to respective box methods.

## Dependencies

> `Frontend:
- `apiClient` (HTTP client library)
- JavaScript/TypeScript runtime

Backend:
- `Box` base class (backend framework)
- `HashBasedHeightmapUtilsBox``
> ``HashGeneratorMasterBox` (hash utilities)
- `WorldTypeVoronoiGenerator` (Voronoi cell generation)
- Flask/Flask-RESTful (for API endpoints)
- NumPy (for array operations)`

## Related

- [[BOX_PATTERN_DOCUMENTATION]]
- [[MAP_GENERATION_ARCHITECTURE]]
- [[PROCEDURAL_GEN_BACKEND_MODULES]]

>[!INFO] Important Note
> The `MapGeneratorServiceBox` uses async operations, so frontend must handle job IDs for status checks. Backend boxes rely on `HashGeneratorMasterBox` for deterministic seed-based generation.


>[!WARNING] Caution
> Default dimensions (128x128) may be insufficient for large worlds. Explicitly pass `width`/`height` to avoid unexpected results. Heightmap generation assumes Voronoi cells are pre-defined in `inputData.cells`.
