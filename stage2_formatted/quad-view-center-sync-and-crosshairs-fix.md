**Tags:** #fix, #quad-view, #gps-sync, #crosshairs, #osm, #plotly, #3d-visualization, #view-synchronization, #gis, #data-visualization
**Created:** 2026-01-12
**Type:** code-notes

# quad-view-center-sync-and-crosshairs-fix

## Summary

```
Fixed quad-view synchronization issues to ensure consistent GPS centering, crosshair visibility, and proper data display across OSM and Plotly views.
```

## Details

> This fix addresses critical rendering inconsistencies in a quad-view GIS application, ensuring:
> - **2D Top and 3D Isometric OSM views** display the same GPS coordinates.
> - **Green crosshairs** appear in all OSM and Plotly views when in quad mode.
> - **Data visualization** (OSM maps and Plotly plots) loads and updates correctly.
> - **View initialization** properly handles dual rendering systems (OSM/Cesium for top/isometric, Plotly for front/side views).

## Key Functions

### ``syncViewsToLocation()``

Synchronizes GPS coordinates across views to ensure alignment.

### ``update2DTopView()``

Adjusts camera positioning for precise centering in 2D Top view.

### ``onLayoutModeChange()``

Initializes crosshairs when OSM is enabled in quad mode.

### ``prepareScene()``

Ensures OSM views receive center markers post-initialization.

### ``addCenterMarker()``

Explicitly adds crosshairs to OSM views.

### ``updatePlots()``

Updates Plotly plots with visualization data after initialization.

## Usage

1. **Initialize views** in quad mode with OSM/Plotly systems.
2. **Call `syncViewsToLocation()`** after OSM views load to align GPS coordinates.
3. **Trigger `onLayoutModeChange()`** to enable crosshairs in OSM views.
4. **Update data** via `updatePlots()` for Plotly and ensure OSM maps sync with GPS.

## Dependencies

> `Cesium`
> `Plotly.js`
> `OSM (OpenStreetMap) API`
> `custom GIS/3D visualization libraries.`

## Related

- [[Quad View Architecture]]
- [[GIS View Synchronization Guide]]
- [[Crosshair Implementation Notes]]

>[!INFO] Critical Alignment
> Ensure `syncViewsToLocation()` is called **after** OSM views initialize to prevent desync between 2D Top and 3D Isometric views.

>[!WARNING] Data Loading Order
> Plotly plots must be updated **before** OSM maps sync to avoid empty views. Initialize Plotly first, then OSM, then sync.
