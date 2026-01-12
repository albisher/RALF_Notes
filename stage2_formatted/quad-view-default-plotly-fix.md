**Tags:** #javascript, #plotly, #cesium, #quad-view, #osm, #frontend, #visualization, #default-state, #layout-mode, #user-experience
**Created:** 2026-01-12
**Type:** code-fix

# app-data.js

## Summary

```
Fixes default behavior of Quad View to ensure Plotly plots render instead of OSM/Cesium viewers in 2D Top and 3D Isometric panels.
```

## Details

> The fix modifies default settings and behavior in `app-data.js` to ensure Quad View loads Plotly visualizations by default. Previously, the layout defaulted to OSM mode, and OSM views were enabled, causing empty Cesium viewers in Quad View panels. The solution adjusts default values (`layoutMode` to `'quad'` and `osmViewEnabled` to `false`) and enforces OSM disabling when switching to Quad View to prioritize Plotly rendering.

## Key Functions

### ``onLayoutModeChange``

Handles mode switching logic; disables OSM when switching to Quad View.

### ``prepareScene()``

Updated comments to reflect Quad View defaults to Plotly.

### ``layoutMode`/`osmViewEnabled``

Default configuration values for Quad View.

## Usage

After applying changes, users will see Plotly plots in Quad View panels by default. Switching to other modes (e.g., OSM) retains OSM functionality.

## Dependencies

> `Cesium`
> `Plotly.js`
> ``simulation/frontend` module.`

## Related

- [[frontend]]
- [[visualization-defaults]]
- [[quad-view-architecture]]

>[!INFO] Critical Default Change
> Default `layoutMode` now set to `'quad'` and `osmViewEnabled` to `false` to ensure Plotly plots render first.

>[!WARNING] OSM Disabling Logic
> Explicitly disabling OSM in `onLayoutModeChange` prevents residual OSM views in Quad View panels.
