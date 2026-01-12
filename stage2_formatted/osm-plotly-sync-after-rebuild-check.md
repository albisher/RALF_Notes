**Tags:** #bug, #api-failure, #gps-preset, #osm-integration, #cesium, #docker-rebuild, #network-issue, #overpass-api
**Created:** 2026-01-12
**Type:** code-notes

# 

## Summary

```
Post-Docker-rebuild UI audit reveals unresolved GPS preset and OSM building loading failures, with API fetch errors persisting despite viewer initialization.
```

## Details

> The rebuild of Docker containers (without cache) confirmed successful container startup, but UI components failed to load OSM data due to two critical issues: (1) GPS preset selection (e.g., "Home (Kuwait)") did not update coordinates, and (2) the Overpass API request failed intermittently, despite prior fallback mechanisms working. Cesium viewers initialized, but empty dark-blue viewports and console errors (`Failed to fetch buildings`) indicated API endpoint/network problems. The random location (`44.1253970, -146.97008`) persisted even after preset selection, blocking OSM building visualization.

## Key Functions

### `OSMIntegrationBox`

Handles OSM building loading via Overpass API, with fallback to Cesium Ion. Fails with persistent API errors post-rebuild.

### `GPS Preset Selection`

Vue component that updates coordinates but breaks after container rebuild.

### `Docker Compose`

Manages container lifecycle (`down`, `build --no-cache`, `up -d`) for UI testing.

## Usage

To reproduce:
1. Run `docker compose down && docker compose build --no-cache && docker compose up -d` in `simulation/docker/`.
2. Access `http://localhost:5007/` and verify:
   - GPS preset dropdown updates coordinates.
   - OSM buildings load in Cesium viewers (empty if API fails).

## Dependencies

> `- Docker Compose (`docker compose`)`
> `Socket.IO`
> `Cesium.js`
> `Overpass API`
> `Vue.js components.`

## Related

- [[docker-compose]]
- [[OSMIntegrationBox]]
- [[Overpass API documentation]]

>[!INFO] **API Endpoint Check**
> Verify Overpass API endpoint (`/api/osm/buildings?bbox=...`) is accessible and returns valid JSON. Network issues may cause intermittent failures.

>[!WARNING] **Preset Isolation**
> The GPS preset logic may be decoupled from the OSM integration box. Test coordinate updates independently to isolate the issue.
