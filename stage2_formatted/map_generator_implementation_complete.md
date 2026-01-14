**Tags:** #Algorithmic-Generation, #Geospatial-Simulation, #Containerized-Services, #FastAPI, #Docker, #Biome-Modelling, #City-Placement, #Story-Integration, #High-Resolution-Maps
**Created:** 2026-01-13
**Type:** documentation-research

# map_generator_implementation_complete

## Summary

```
A complete implementation of a high-resolution map generator using Azgaar’s algorithms, integrated with a story/world system via containerized microservices.
```

## Details

> This implementation includes a modular engine for generating procedural maps via Voronoi diagrams, heightmaps, biome calculations, and city placement. The system is containerized for isolation, with a FastAPI service exposing REST endpoints for job management and results. It integrates with a frontend UI to allow interactive map generation, preview, and story system synchronization. The design emphasizes scalability, modularity, and real-time progress tracking.

## Key Functions

### `VoronoiGenerator`

Creates cell-based map structures from seed points.

### `HeightmapGenerator`

Implements neighbor propagation for natural terrain.

### `BiomeCalculator`

Assigns biome types based on elevation and climate data.

### `CityPlacer`

Places cities with terrain suitability scoring and population constraints.

### `MapGenerator`

Orchestrates the full workflow and outputs Azgaar-compatible map data.

### `JobManager`

Handles background job processing with progress callbacks.

### `FastAPI Service`

Exposes REST endpoints for map generation, status checks, and result retrieval.

### `Docker Container`

Isolates the service with resource limits and health checks.

### `UI Integration`

Vue-based components for map generation, preview, and story linking.

## Usage

1. **Deploy**: Run `docker-compose up map-generator` to start the service.
2. **Generate Maps**: Use the UI form to specify parameters (seed, resolution, etc.) and trigger generation.
3. **API Workflow**:
   - POST `/api/maps/generate` to start a job.
   - Poll `GET /api/maps/status/{job_id}` for progress.
   - Retrieve results via `GET /api/maps/result/{job_id}`.
4. **Cancel Jobs**: Use `POST /api/maps/cancel/{job_id}` to abort a job.

## Dependencies

> `fastapi`
> `uvicorn`
> `numpy`
> `scipy`
> `pydantic`
> `Redis (for job management)`
> `Docker`
> `Vue 3`
> `Material Design Icons.`

## Related

- [[World-System-Documentation]]
- [[Story-Integration-Guide]]
- [[Docker-Container-Configuration]]

>[!INFO] **Performance Considerations**
> High-resolution maps (100,000 cells) may take 120+ seconds. Optimize seed resolution or reduce cell count for faster iterations.

>[!WARNING] **Job Limits**
> Docker resource limits (2 CPU, 4GB RAM) may throttle large jobs. Adjust `MAP_GEN_MAX_CELLS` or use smaller resolutions for testing.
