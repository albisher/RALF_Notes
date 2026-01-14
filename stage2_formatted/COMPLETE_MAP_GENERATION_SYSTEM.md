**Tags:** #algorithm, #procedural-generation, #hash-based, #2D-visualization, #flask-backend, #vue-frontend, #modular-components, #voronoi-diagrams, #terrain-generation, #biome-classification
**Created:** 2026-01-13
**Type:** documentation

# COMPLETE_MAP_GENERATION_SYSTEM

## Summary

```
Generates interactive 2D maps from hash inputs using a multi-stage pipeline combining Python generators and Vue.js frontend components.
```

## Details

> The system converts user-provided hash inputs (e.g., `"ew|Planet"`) into a complete, interactive 2D map via a structured pipeline. It employs modular components (Flask backend and Vue.js frontend) to handle terrain generation, Voronoi cell structuring, heightmap assignment, and biome classification. The system supports both quick previews (fast, <0.1s) and full map generation (5–120s), with configurable world types and parameters. Key stages include hash processing, terrain/heightmap generation, and rendering via SVG polygons.

## Key Functions

### ``MapGeneratorPage.vue``

Orchestrates UI and orchestrates quick preview generation.

### ``WorldTypeTerrainGeneratorBox``

Generates base terrain patterns (2D array) using world type and hash.

### ``WorldTypeVoronoiGenerator``

Creates Voronoi cell structures for world layout.

### ``WorldTypeHeightmapGeneratorBox``

Assigns height values to cells based on terrain and sea level.

### ``WorldTypeBiomeCalculator``

Classifies regions into biomes (e.g., forest, desert).

### ``WorldMap2D.vue``

Renders interactive SVG-based 2D maps with cell polygons.

### ``MapGeneratorServiceBox``

Manages asynchronous map generation jobs.

### ``MapProcessBox``

Validates and processes final map data (e.g., adds metadata).

## Usage

1. **Quick Preview**: Input a hash + world type (e.g., `"ew|Planet"`), triggering a fast (<0.1s) preview via `MapGeneratorPage.vue`.
2. **Full Map**: Submit a hash + parameters, triggering async generation via `MapGeneratorServiceBox` and rendering via `WorldMap2D.vue`.
3. **Customization**: Modify world types (e.g., `"planet"`, `"galaxy"`) or adjust parameters (e.g., resolution, sea level) in frontend/backend boxes.

## Dependencies

> `Flask (backend)`
> `Vue.js (frontend)`
> `NumPy/Python libraries (Voronoi/heightmap algorithms)`
> `Azgaar-format (map serialization)`
> `SVG.js (rendering).`

## Related

- [[`Complete Generation Sequence Diagram`]]
- [[`Code Boxes Implementation Notes`]]
- [[`Backend API Specifications`]]

>[!INFO] **Hash Processing**
> The system uses SHA-256 to derive deterministic inputs from user-provided strings (e.g., `"ew|Planet"`), ensuring reproducibility across runs.

>[!WARNING] **Performance Tradeoff**
> Quick previews sacrifice detail (128x128 resolution) for speed, while full maps use higher resolutions (1000x600) but take longer (5–120s).
