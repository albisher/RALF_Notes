**Tags:** #asynchronous-processing, #deterministic-generation, #hash-based-parameterization, #map-generation, #two-stage-process, #backend-frontend-architecture, #fastapi-flask-integration, #geospatial-data-generation
**Created:** 2026-01-13
**Type:** code-architecture

# MAP_GENERATION_LOGIC

## Summary

```
Designs a two-phase map generation system using hash-based parameters for instant preview and procedural generation for detailed maps.
```

## Details

> This system implements a **two-stage map generation workflow** where a hash-based parameter generator (`maps.py`) produces deterministic map metadata instantly, while a procedural engine (`map_generator.py`) renders the full map asynchronously. The frontend interacts with a backend API to trigger parameter generation, which is immediately returned, followed by a background job for actual map rendering. The architecture leverages deterministic hashing for consistency and modular design for scalability, with time-based resolution affecting generation duration.

## Key Functions

### ``generate_map_description``

Converts input (text/hash) into map metadata (name, coordinates, biome settings).

### ``hash_input``

Converts text to SHA256 hash for deterministic parameter selection.

### ``MapGenerator``

Procedural engine generating Voronoi cells, heightmaps, biomes, and city placements.

### ``/api/generation/maps` (Flask)`

Instant parameter generation endpoint.

### ``/api/maps/generate` (FastAPI)`

Background job for full map rendering.

## Usage

1. **Frontend**: Sends hash/world data to `/api/generation/maps` → receives parameters.
2. **Backend**: Triggers `/api/maps/generate` with parameters → returns job ID.
3. **Background**: `MapGenerator` processes job asynchronously → returns map data on completion.

## Dependencies

> ``Generators.Maps.maps``
> ``services.map-generator.engine.map_generator``
> `Flask`
> `FastAPI`
> `PyTorch (for Voronoi generation)`
> `Azgaar format library.`

## Related

- [[Space Pearl Map Generation API Docs]]
- [[Space Pearl UI Integration Guide]]
- [[Deterministic Procedural Generation Patterns]]

>[!INFO] **Deterministic Hashing**
> Hash-based parameter selection ensures identical maps for identical inputs, critical for replayability and consistency across sessions.

>[!WARNING] **Background Job Risk**
> Asynchronous rendering may fail if the job queue is overloaded; implement retry logic for failed jobs.

>[!INFO] **Resolution Impact**
> Higher resolutions (e.g., "ultra") significantly increase generation time; preload lower-res maps for quick previews.
