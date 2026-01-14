**Tags:** #procedural-generation, #world-building, #databases, #backend-integration, #frontend-framework, #3d-visualization, #2d-visualization, #d3js, #threejs, #vuejs, #docker, #postgresql, #jsonb
**Created:** 2026-01-13
**Type:** code-notes

# EXISTING_CODE_ANALYSIS

## Summary

```
Analyzes existing procedural generation and visualization systems for a space-themed world-building application, detailing implemented components and pending integrations.
```

## Details

> This code file documents a **Space Pearl World-Building Web Application**, featuring a **procedural generation system** and **interactive visualizations** (2D/3D maps) with extensive world data. The system uses **SHA-256 hashing** for deterministic generation, **JSONB** for metadata storage, and **D3.js/Three.js** for rendering. The **Generators** directory includes plant, building, robot, and character generation modules with biome-specific adaptations. The **app/** directory contains **D3.js-based 2D maps** and **Three.js 3D globes**, both ready for Vue integration. Rich world data (biomes, characters, robots) is stored in the **Documentation/** directory. Data processing scripts validate and analyze map coordinates and JSON structures. **Pending tasks** focus on backend (PostgreSQL + SQLAlchemy, JWT auth), frontend (Vue 3, RTL support), and deployment (Docker, Nginx, monitoring).

## Key Functions

### ``Generators/Plants/plants.py``

Generates plant attributes (20+ categories) using salt-based selection.

### ``Generators/Buildings/buildings.py``

Creates buildings with materials, styles, and pod architecture via deterministic hashing.

### ``app/map.js``

Renders interactive 2D maps with D3.js, including zoom/pan controls and biome color mapping.

### ``app/globe.js``

Visualizes 3D globes with Three.js, supporting terrain extrusion, orbit controls, and biome visualization.

### ``app/process_map_data.py``

Validates and preprocesses map JSON data for backend integration.

### ``Documentation/WorldInformation/``

Stores static world data (biomes, characters, robots) in text files.

## Usage

1. **Generators**: Seed with a salt (e.g., `SHA-256("seed")`) to generate consistent content.
2. **Visualizations**: Load `map.json`/`processed_map.json` and `globe.js` data into Vue components.
3. **Data Processing**: Run scripts (`process_map_data.py`) to validate/transform JSON before backend storage.
4. **Backend**: Convert generators to Flask endpoints (e.g., `/generate/plant`) and integrate with PostgreSQL.
5. **Frontend**: Replace D3.js/Three.js with Vue components (e.g., `<MapComponent />` for 2D maps).

## Dependencies

> `D3.js`
> `Three.js`
> `Vue.js (for frontend integration)`
> `PostgreSQL`
> `SQLAlchemy`
> `Python libraries (e.g.`
> ``hashlib``
> ``json`)`
> `Flask (for backend API)`
> `Docker`
> `Nginx`
> `Prometheus.`

## Related

- [[Space Pearl World-Building API Design]]
- [[PostgreSQL JSONB Migration Guide]]
- [[Vue 3 Integration Template]]
- [[Three]]
- [[Dockerized Flask Backend]]

>[!INFO] **Deterministic Generation**
> Use `SHA-256("seed")` in `Generators/` to ensure reproducible content. Biomes adapt attributes based on salt input.

>[!WARNING] **Data Size Limits**
> `map.json` (4.5MB) may exceed frontend limits; split into chunks or use API endpoints for large datasets.

>[!INFO] **Vue Integration Critical**
> Existing D3.js/Three.js code must be refactored into Vue components (e.g., `MapComponent`) to avoid conflicts.

>[!WARNING] **PostgreSQL JSONB**
> Ensure schema supports nested JSON (e.g., `JSONB` fields) for world data migration. Validate with `validate_map_json.py`.
