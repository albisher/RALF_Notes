**Tags:** #javascript, #osm-vector-data, #map-plot-trigger, #gps-coordinate-check, #openstreetmap, #plotly, #data-fetching, #cache-management
**Created:** 2026-01-12
**Type:** code-notes

# plot-2d-box.js

## Summary

```
Analyzes the trigger flow for fetching and displaying OSM vector street data in a 2D top-view plot.
```

## Details

> This document outlines the sequence of events that initiate the retrieval and rendering of OpenStreetMap (OSM) vector street data for a 2D top-view plot (`plot-top`). The process begins with a function call to `updatePlot()`, which checks for valid GPS coordinates before fetching OSM data via an Overpass API query. The fetched data is cached and converted into Plotly-compatible traces to visualize streets as vector lines.

## Key Functions

### ``updatePlot('plot-top', data, 'x', 'y')``

Entry point that validates conditions and triggers OSM data fetching.

### ``fetchOSMVectorDataForPlotly(baseLatitude, baseLongitude, viewRange)``

Handles OSM API queries, caching, and conversion of OSM ways into Plotly traces.

### ``updatePlotsWithData()``

External function in `app-data.js` that calls `updatePlot` for multiple plots, including `plot-top`.

## Usage

To trigger this flow:
1. Call `updatePlot('plot-top', data, 'x', 'y')` with valid GPS coordinates.
2. Ensure `plot-top` is initialized and `this.plotsInitialized[plot-top]` is `true`.
3. The function checks for GPS coordinates (from `masterControls` or `data.base_gps`) and fetches OSM vector data if valid.

## Dependencies

> `- `window.app.masterControls` (for GPS coordinates)
- `data.base_gps` (fallback GPS data)
- Overpass API (for OSM vector data fetching)
- Plotly library (for rendering vector traces)
- `osmVectorCache` (for caching OSM data)`

## Related

- [[app-data]]
- [[Overpass API Documentation]]
- [[Plotly Documentation]]

>[!INFO] Important Note
> The `updatePlot` function prioritizes `window.app.masterControls` for GPS coordinates. If unavailable, it falls back to `data.base_gps`. Both must be non-zero values to proceed.


>[!WARNING] Caution
> If GPS coordinates are (0, 0), the OSM data fetch will be skipped, resulting in no vector streets displayed. Always validate coordinates before triggering the flow.
