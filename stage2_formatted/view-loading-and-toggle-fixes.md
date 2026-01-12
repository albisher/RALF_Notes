**Tags:** #view-loading, #cesium, #plotly, #osm, #vue, #layout-mode, #toggles, #3d-2d, #data-visualization, #interactivity
**Created:** 2026-01-12
**Type:** code-notes

# view-loading-and-toggle-fixes

## Summary

```
Fixed view initialization and toggle inconsistencies between OSM and Plotly views across different layout modes, ensuring proper state preservation and rendering.
```

## Details

> This file documents fixes for view loading and toggling between OSM (OpenStreetMap) and Plotly visualizations, addressing issues in Quad, 3D Only, 2D Only, and Both layout modes. The core logic involves dynamically initializing Cesium viewers or Plotly plots based on the current layout mode and OSM toggle state, ensuring no data loss or empty views during transitions. The solution includes reusing existing viewers, preserving camera states, and coordinating Vue lifecycle hooks for proper rendering synchronization.

## Key Functions

### ``initializeOSMViewsForLayout(layoutMode)``

Dynamically initializes Cesium viewers for OSM-based views based on the specified layout mode (Quad, 3D Only, 2D Only, Both).

### ``onToggleOSMView()``

Handles OSM toggle logic, reinitializing views when OSM is enabled/disabled and ensuring Plotly plots are updated.

### ``onLayoutModeChange()``

Updates view initialization based on layout mode (e.g., Quad, 3D Only) while respecting the OSM toggle state.

### ``initializePlots()``

Initializes Plotly plots when OSM is disabled.

### ``updatePlots()``

Updates Plotly plots with current data after toggles.

## Usage

To use these fixes:
1. Call `initializeOSMViewsForLayout(layoutMode)` when switching layout modes if OSM is enabled.
2. Call `initializePlots()` when disabling OSM to initialize Plotly plots.
3. Ensure `updatePlots()` is invoked after toggling to Plotly to reflect current data.
4. Preserve camera states by re-enabling Cesium viewers when switching back to OSM.

## Dependencies

> `Cesium.js`
> `Plotly.js`
> `Vue.js (for Vue lifecycle hooks and reactivity).`

## Related

- [[CesiumViewerInitializationGuide]]
- [[PlotlyDataVisualizationModule]]
- [[VueViewToggleComponent]]

>[!INFO] Important Note
> The solution assumes existing Cesium and Plotly viewer instances are preserved across toggles. If viewers are recreated, camera states must be explicitly saved/restored to avoid resets.

>[!WARNING] Caution
> Disabling OSM and enabling Plotly requires reinitializing plots. If data changes frequently, ensure `updatePlots()` is called promptly to avoid stale visualizations.
