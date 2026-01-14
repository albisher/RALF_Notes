**Tags:** #UI-Development, #Map-Generation, #Docker, #World-Building, #Game-Procedural-Generation
**Created:** 2026-01-13
**Type:** documentation

# map_generator_demo_ready

## Summary

```
Documentation for a **Map Generator Demo System**, detailing UI readiness, service status, and procedural generation workflow for world-building.
```

## Details

> This file outlines the status of a **Map Generator** demo, combining a fully functional UI (`http://localhost:5174/#maps`) and a service under construction (`http://localhost:5002`). The UI allows users to configure map parameters (e.g., resolution, biome settings) and preview results, while the service handles backend generation. The demo includes a multi-stage process (Voronoi, heightmap, biomes, cities, assembly) with progress tracking and estimated timelines. The system generates structured JSON outputs compatible with existing tools, such as city placement and biome distribution.

## Key Functions

### `Map Generator Form`

User input for map parameters (name, resolution, biome preferences).

### `Progress Tracking`

Real-time stage updates (voronoi → assembly) and percentage completion.

### `Map Preview`

Visual representation of generated cells, biomes, and cities.

### `Service Health Check`

`GET /health` endpoint for Docker container status.

### `World Assembly`

Final JSON export for integration into game/world systems.

## Usage

1. **UI Access**: Navigate to `http://localhost:5174/#maps` to fill the form.
2. **Service Access**: After build completion, check `http://localhost:5002` for `/health` status.
3. **Generate**: Click "Generate Map" to queue a job; progress updates appear dynamically.
4. **Export**: Use the preview to export JSON or save to the world system.

## Dependencies

> `Docker`
> `Node.js (for UI)`
> `Docker Compose (for service container)`
> `Azgaar procedural generation libraries (backend).`

## Related

- [[Map Generator Service Code]]
- [[Azgaar Procedural Generation Docs]]
- [[Docker Compose Configuration]]

>[!INFO] Important Note
> The **Map Generator Service** is still building initially (first run takes ~2-3 minutes). Monitor `docker-compose ps map-generator` for progress.

>[!WARNING] Caution
> For "Low" resolution, expect ~5 seconds to generate 10K cells. Higher resolutions increase time significantly. Adjust settings to balance quality and performance.
