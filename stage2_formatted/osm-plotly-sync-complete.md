**Tags:** #synchronization, #geospatial, #3d-visualization, #openstreetmap, #plotly, #cesium, #coordinate-conversion
**Created:** 2026-01-12
**Type:** code-notes

# osm-plotly-sync-complete

## Summary

```
Implementation of OSM-Plotly synchronization for real-time geographic data visualization across 2D/3D views.
```

## Details

> This implementation synchronizes OpenStreetMap (OSM) data with Plotly visualizations by converting OSM building coordinates from GPS (lat/lon) to simulation-local meters. The system ensures both views (2D top and 3D isometric) display identical geographic areas, with OSM buildings rendered as gray polygons in Plotly. Camera positioning is dynamically adjusted to center on the simulation base (0,0,0) when OSM data loads, maintaining alignment between OSM and Plotly views.

## Key Functions

### ``getOSMBuildingsForPlotly()``

Extracts OSM buildings from Cesium entities and converts GPS coordinates to simulation-local meters.

### ``updatePlotsWithData()``

Merges OSM building data into Plotly visualization, applying gray styling for transparency.

### ``onToggleOSMView()``

Handles synchronization logic when switching between OSM and Plotly views, resetting Plotly’s camera to the base coordinate (0,0,0).

### ``automaticCameraCentering()``

Checks and resets Plotly’s camera if it deviates beyond 10 meters from the base, ensuring OSM buildings remain visible.

## Usage

1. Load OSM data via Cesium entities.
2. Call `getOSMBuildingsForPlotly()` to extract and convert building coordinates.
3. Use `updatePlotsWithData()` to render OSM buildings in Plotly.
4. Trigger `onToggleOSMView()` when switching between OSM and Plotly views.
5. Plotly’s camera auto-resets to (0,0,0) if OSM buildings are loaded.

## Dependencies

> `Cesium (for OSM data extraction)`
> `Plotly.js (for visualization)`
> `JavaScript (for frontend logic).`

## Related

- [[osm-integration-box]]
- [[app-data]]

>[!INFO] Coordinate Conversion Critical
> OSM coordinates (lat/lon) must be converted to simulation-local meters (e.g., via Cesium’s `toSimLocal()`) to ensure accurate alignment in Plotly. Failure to do so results in misaligned visualizations.

>[!WARNING] Camera Reset Sensitivity
> The 10-meter threshold for camera reset is adjustable. Lowering it may cause unintended resets if OSM buildings are loaded near the base. Test edge cases to avoid visual glitches.
