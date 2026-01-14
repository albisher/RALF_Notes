**Tags:** #docker, #map-viewer, #nginx, #static-files, #web-development, #frontend, #ui-design, #coordinate-system, #json-data
**Created:** 2026-01-13
**Type:** documentation

# MAP_VIEWER_SETUP

## Summary

```
Documentation for Docker-based setup and testing of map viewer applications, detailing file structures, services, and recommended configurations.
```

## Details

> This document outlines the Docker-based deployment of map viewer applications, replacing a deprecated local server setup. The setup includes a **static file server** and **Nginx proxy**, both managed via Docker Compose. The map viewer files are organized into `/app/` and `/ui-explorations/`, with multiple HTML pages supporting interactive features like zooming, panning, and coordinate editing. The current production version (`map-viewer-overlay.html`) features integrated controls and dynamic UI elements. Supporting files include JavaScript, CSS, and JSON data for map rendering.

## Key Functions

### ``static-files` service`

Hosts map viewer files (`/app/` and `/ui-explorations/`) via Nginx proxy.

### ``proxy` service`

Routes requests to the static file server, exposing `/app/` and `/ui-explorations/` at `http://localhost:8888`.

### ``map.js``

External JavaScript for `map.html` (672 lines), managing map interactions.

### ``map.css``

Stylesheet for `map.html`, defining visual styling.

### ``map.json``

Raw map data for `map_visualization.html`.

### ``processed_map.json``

Processed map data for `map.html` and `map_visualization_processed.html`.

### ``map.html``

Editable map center coordinates via input fields.

### ``map_visualization.html``

Read-only map with coordinate spans.

### ``map_visualization_processed.html``

Editable map with processed data.

### ``map-viewer-overlay.html``

Current production version with integrated controls (icons, collapsible panels).

## Usage

1. **Deploy**:
   - Run `docker-compose up -d` to start services.
   - Access map viewers at `http://localhost:8888` (e.g., `app/map.html`).
2. **Manage**:
   - Use `docker-compose ps static-files` to check service status.
   - Use `docker-compose logs static-files` to inspect errors.
   - Use `curl` to test HTTP responses (e.g., `curl -s -o /dev/null -w "%{http_code}" http://localhost:8888/app/map.html`).
3. **Stop**:
   - `docker-compose down` to halt all services.
   - `docker-compose restart static-files` to restart the static file server.

## Dependencies

> `Docker`
> `Docker Compose`
> `Nginx (for proxy routing)`
> `and external libraries for map rendering (e.g.`
> `Leaflet or similar).`

## Related

- [[README]]
- [[map-viewer]]

>[!INFO] Important Note
> The **current production version** (`map-viewer-overlay.html`) is recommended for all iterations due to its integrated controls and dynamic UI. Ensure `processed_map.json` is correctly served at `/app/processed_map.json`.


>[!WARNING] Caution
> Avoid using the deprecated local server (port 8001) to prevent port conflicts. Always use Docker at `http://localhost:8888`. Logs for debugging can be accessed via `docker-compose logs -f static-files`.
