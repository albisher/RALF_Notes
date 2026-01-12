**Tags:** #crosshair-fix, #3d-view, #osm-integration, #gps-coordinates, #layout-mode, #javascript, #map-view
**Created:** 2026-01-12
**Type:** code-notes

# center-crosshair-all-views-fix

## Summary

```
Fixed crosshair centering across all map views (2D, 3D, OSM) to ensure consistent display regardless of initialization or GPS updates.
```

## Details

> This fix ensures the green crosshair is always rendered in all map views (OSM, 3D isometric, and 2D) by guaranteeing its addition during initialization, layout mode changes, and GPS coordinate updates. Previously, the crosshair was conditionally added only when `syncViewsToLocation()` was called, leading to inconsistencies in 3D isometric views. The solution standardizes crosshair placement by using current GPS coordinates (or fallback defaults) in OSM views and verifying its presence in Plotly-based views.

## Key Functions

### ``initializeOSMViewsForLayout()``

Adds a center marker to OSM views using available GPS coordinates or defaults.

### ``onLayoutModeChange()``

Ensures crosshair is added when switching between layout modes (e.g., OSM, 3D-only, 2D-only).

### ``updatePlot()` (in `plot-3d-box.js` and `plot-2d-box.js`)`

Maintains crosshair at (0,0,0) for Plotly views.

### ``addCenterMarker()``

Core function in `osmIntegrationBox` to render the crosshair at specified coordinates.

## Usage

To apply this fix:
1. Ensure `masterControls` or `osmIntegrationBox.currentLocation` contains valid GPS coordinates.
2. Call `initializeOSMViewsForLayout()` during OSM view initialization.
3. Trigger `onLayoutModeChange()` when switching between layout modes.
4. Verify crosshair updates in `updatePlot()` for Plotly views.

## Dependencies

> ``osmIntegrationBox``
> ``masterControls``
> ``window.osmIntegrationBox.currentLocation``
> ``plot-3d-box.js``
> ``plot-2d-box.js``

## Related

- [[`crosshair-initialization]]
- [[`3d-view-coordinates]]

>[!INFO] Critical Fallback
> If `masterControls` or `osmIntegrationBox.currentLocation` is unavailable, the crosshair defaults to (0,0) coordinates, ensuring visibility even without GPS data.

>[!WARNING] Coordinate Dependency
> Crosshair accuracy depends on `latitude`/`longitude` availability. Missing data may result in incorrect positioning. Always validate coordinates before rendering.
