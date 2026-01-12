**Tags:** #Cesium, #OpenStreetMap, #3DVisualization, #Geospatial, #PlotlyIntegration, #CompassFix, #OSMImagery, #MapRendering, #WebGL, #GIS
**Created:** 2026-01-12
**Type:** code-fix

# osm-street-maps-compass-and-plotly-fix

## Summary

```
Fixed OSM street map rendering issues, added compass orientation, and resolved Plotly OSM building visibility in Cesium-based geospatial viewers.
```

## Details

> This fix addresses three critical OSM integration problems in Cesium viewers: street map tiles were invisible due to dark base colors or missing imagery layers, no compass orientation was available, and Plotly failed to display OSM-builtings when toggled. The solution involved enabling the compass widget, adjusting globe base colors to white, explicitly adding OSM imagery providers, forcing tile renders, and retrying visibility checks with delays.

## Key Functions

### ``osmImageryProvider``

Provides OpenStreetMap imagery layers for Cesium.

### ``syncViewsToLocation()``

Synchronizes viewer states and triggers visibility checks for OSM imagery.

### ``cesiumViewer.scene.globe.imageryLayers``

Manages and configures Cesium’s globe imagery layers.

### ``this.cesiumViewer.scene.requestRender()``

Forces immediate rendering to trigger tile loading.

## Usage

To apply this fix:
1. Update `simulation/frontend/boxes/osm-integration-box.js` with the provided configurations.
2. Ensure Cesium viewers (`cesiumViewer` and `cesium2DTopViewer`) are initialized with `compass: true`.
3. Set `globe.baseColor` to `Cesium.Color.WHITE` for visibility.
4. Explicitly add OSM imagery providers and retry visibility checks if needed.

## Dependencies

> `Cesium.js`
> `OpenStreetMap API`
> `Plotly.js (indirectly for building visualization toggles)`
> `WebGL (for rendering).`

## Related

- [[osm-integration-box]]
- [[Cesium documentation on imagery providers]]
- [[OpenStreetMap API reference]]

>[!INFO] Compass Configuration
> The `compass: true` setting must be applied to both 2D and 3D Cesium viewers to ensure consistent orientation indicators. Navigation instructions should be hidden initially (`navigationInstructionsInitiallyVisible: false`) for cleaner UI.

>[!WARNING] Imagery Provider Retries
> If OSM imagery fails to load, implement retry logic with delays (e.g., 100ms, 500ms, etc.) to avoid silent failures. Explicitly calling `requestRender()` ensures tiles are reloaded dynamically.
