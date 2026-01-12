**Tags:** #javascript, #cesium, #gps, #map-updates, #preset-selection, #2d-view, #osm-integration, #frontend-logic, #event-handling, #data-flow
**Created:** 2026-01-12
**Type:** code-notes

# app-data.js

## Summary

```
Updates the 2D Cesium top-view when a GPS preset is selected, ensuring compatibility across different layout modes.
```

## Details

> This fix ensures the `onMiniMapLoaded()` method in `app-data.js` dynamically updates the Cesium 2D top-view container when a GPS preset (Random, Home, or PAAET) is chosen. The logic now checks for OSM integration, non-quad layout modes, and triggers updates to the Cesium viewer by fetching new coordinates and loading OSM data. Previously, this functionality was only functional in quad-view mode (Plotly-based), but the fix extends it to other modes (2D-only, 3D-only, OSM) by initializing and updating the Cesium 2D top-view container.

## Key Functions

### `onMiniMapLoaded()`

Handles the event when the OSM mini-map loads, updating the 2D Cesium view if conditions are met.

### `initCesium2DTopViewer()`

Initializes the Cesium 2D top-view container if it doesn’t exist.

### `update2DTopView()`

Updates the Cesium 2D top-view with new GPS coordinates and elevation settings.

### `loadOSMBuildings()`

Loads OSM buildings for the new location with specified altitude, pitch, and radius.

## Usage

1. Select a GPS preset (Random, Home, or PAAET) from the dropdown.
2. The `onMiniMapLoaded()` method checks if OSM is enabled and the layout mode is not quad.
3. If conditions are met, it initializes/updates the Cesium 2D top-view with the new coordinates and loads OSM buildings.

## Dependencies

> ``Cesium``
> ``Plotly` (for quad view)`
> ``osmIntegrationBox` (external OSM integration module)`
> ``masterControls` (coordinates data)`
> ``mapData` (latitude/longitude storage).`

## Related

- [[app-data]]
- [[GPS-Preset-Selection-Workflow]]
- [[OSM-Integration-Guide]]

>[!INFO] Important Note
> The fix ensures backward compatibility by preserving existing quad-view behavior while adding support for Cesium 2D top-view updates in other layout modes. Always await initialization and updates to handle asynchronous operations safely.


>[!WARNING] Caution
> If `osmIntegrationBox` or Cesium containers fail to load, the update logic will fall back to error handling. Ensure OSM integration is properly initialized before triggering this method.
