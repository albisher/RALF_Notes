**Tags:** #map-generation, #json-processing, #hash-to-visual, #azgaar-format, #procedural-worldbuilding
**Created:** 2026-01-13
**Type:** code-notes

# GENERATE_MAP_JSON_FROM_HASH

## Summary

```
Generates a structured map JSON file from textual hash inputs, enabling procedural world creation with two-stage processing.
```

## Details

> This script implements a two-phase workflow: first, it converts textual descriptions (e.g., "galaxy map") into procedural parameters (e.g., Voronoi cell resolution, biome distribution), then it generates a full map in Azgaar’s proprietary JSON format. The first stage is instantaneous, while the second stage (Voronoi-based rendering) is computationally intensive, requiring time proportional to map complexity (cells count). The output matches `quraan_map.json`, supporting direct integration into Azgaar’s map viewer.

## Key Functions

### ``Generators/Maps/maps.py``

Instantly converts hash inputs into map parameters (e.g., `seed`, `resolution`, biome rules).

### ``services/map-generator/engine/map_generator.py``

Core procedural engine that constructs Voronoi cells, heightmaps, and biomes.

### ``ui-beta/scripts/generate_map_json_from_hash.py``

Orchestrates the full pipeline (API or direct mode) and outputs the final JSON.

### ``ui-beta/maps/quraan_map.json``

Reference template for the generated output format.

## Usage

1. **Command-line**: Run via API (recommended) or direct mode with `--direct` flag.
   Example:
   ```bash
   python3 ui-beta/scripts/generate_map_json_from_hash.py "cloud platforms" "cloud_world" "Mystical cloud world" ui-beta/maps/cloud_map.json --api-url http://localhost:5002
   ```
2. **Programmatic**: Use `Generators/Maps.maps` for parameter generation and `services.map-generator.engine` for direct rendering.

## Dependencies

> ``requests``
> ``numpy``
> ``scipy``
> ``Azgaar procedural engine` (internal service)`
> ``ui-beta` package.`

## Related

- [[quraan_map]]
- [[api]]
- [[maps]]

>[!INFO] Important Note
> The script splits work into two phases: **instant parameterization** (hash → rules) and **time-consuming rendering** (Voronoi cells, biomes). Always validate the `job_id` status if using API mode to avoid idle waits.

>[!WARNING] Caution
> Direct mode (`--direct`) requires `scipy` and `numpy` and runs in-process. For large maps (>60K cells), consider API mode to avoid memory overload in containers.
