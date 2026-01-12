**Tags:** #verification, #osm-integration, #plotly, #3d-visualization, #cesium, #coordinate-systems, #data-synchronization, #gps-coordinates, #buildings
**Created:** 2026-01-12
**Type:** documentation

# osm-plotly-sync-verification

## Summary

```
Document outlining synchronization verification issues between OSM (Cesium) and Plotly visualization systems, focusing on missing OSM building data and coordinate system mismatches.
```

## Details

> This document details a verification process for synchronizing OpenStreetMap (OSM) data with Plotly-based 3D/2D visualizations via Cesium. The core issue is that OSM buildings fail to load, preventing validation of street layout and coordinate system alignment between OSM (GPS-based lat/lon) and Plotly (simulation-based meters). The verification highlights functional components like the OSM toggle, view switching, and GPS presets, but critical synchronization gaps remain due to missing OSM building data extraction and transformation logic.

## Key Functions

### ``updatePlotsWithData``

Expected to merge OSM building data into Plotly visualizations but is not found due to timing issues.

### ``getOSMBuildingsForPlotly``

Responsible for extracting OSM building data from Cesium entities and converting coordinates to simulation space.

### `OSM Toggle Button`

Enables switching between OSM (Cesium) and Plotly views but lacks OSM building data.

### `Cesium Viewers (3D/2D)`

Render OSM data but fail to populate Plotly with matching building data.

## Usage

To verify synchronization:
1. Ensure OSM buildings load in Cesium (3D/2D views).
2. Extract building data via `getOSMBuildingsForPlotly` and transform coordinates to simulation space.
3. Call `updatePlotsWithData` to merge OSM data into Plotly plots.
4. Compare street layouts and camera angles between OSM (GPS) and Plotly (simulation) views.

## Dependencies

> `- `osm-integration-box.js` (contains `getOSMBuildingsForPlotly` and `updatePlotsWithData` logic)
- Cesium.js (for OSM rendering in 3D/2D views)
- Plotly.js (for 3D/2D simulation plots)
- WebGL (for Cesium rendering`
> `with potential GPU acceleration needs)`

## Related

- [[osm-integration-box]]
- [[cesium-visualization-guide]]
- [[plotly-coordinate-transformation]]

>[!INFO] Important Note
> OSM buildings must be loaded and converted to simulation coordinates (meters) for Plotly to display them. The current failure stems from missing data extraction or transformation steps.


>[!WARNING] Caution
> WebGL errors in Cesium headless mode may indicate GPU acceleration is required for proper initialization. Ensure the environment supports WebGL and Cesium’s coordinate system conversions.
