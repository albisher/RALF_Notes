**Tags:** #data-integration, #gis, #plotly, #cesium, #osm, #visualization, #coordinate-transformation
**Created:** 2026-01-12
**Type:** code-implementation

# 

## Summary

```
Converts OpenStreetMap (OSM) building data from Cesium into Plotly-compatible format for visualization.
```

## Details

> This integration bridges OSM building data extracted from Cesium entities into Plotly, enabling OSM structures to be rendered in Plotly viewers. The solution converts GPS coordinates to local simulation coordinates (meters from a base point), formats building metadata (e.g., ID, dimensions, polygon points), and merges OSM data into Plotly’s visualization pipeline. The transformation ensures accurate spatial representation while maintaining transparency and distinct styling (gray) for OSM buildings.

## Key Functions

### ``getOSMBuildingsForPlotly(baseLatitude, baseLongitude)`** (in `osm-integration-box.js`)`

Extracts OSM building data from Cesium, converts GPS coordinates to local simulation space, and returns formatted objects for Plotly.

### ``updatePlotsWithData(data)`** (in `app-data.js`)`

Integrates OSM building data into Plotly’s visualization pipeline, conditionally adding OSM data only when required (e.g., if OSM is loaded and base coordinates exist).

## Usage

1. **Trigger Data Extraction**:
   Call `window.osmIntegrationBox.getOSMBuildingsForPlotly(latitude, longitude)` to fetch OSM buildings in local coordinates.
2. **Merge with Plotly**:
   In `updatePlotsWithData()`, prepend OSM buildings to the existing `data.buildings` array if conditions are met (e.g., OSM box exists and base coordinates are available).
3. **Render in Plotly**:
   Pass the merged `data` to Plotly’s update function to visualize OSM buildings alongside other simulation data.

## Dependencies

> ``cesium``
> ``plotly.js``
> ``simulation/frontend/boxes/osm-integration-box.js``
> ``simulation/frontend/app-data.js``

## Related

- [[osm-integration-box]]
- [[app-data]]

>[!INFO] **Coordinate Conversion Note**
> The `gpsToLocal` function assumes Earth’s radius (`earthRadius`) is defined (e.g., `6371000` meters). Ensure this value matches the simulation’s global reference.

>[!WARNING] **Conditional Data Loading**
> The integration skips OSM data if `window.osmIntegrationBox` or base coordinates are unavailable. Test edge cases where OSM data might fail silently.
