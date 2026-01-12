**Tags:** #javascript, #vuejs, #openstreetmap, #plotly, #frontend, #data-visualization, #gps, #osm-integration, #reactivity, #debugging
**Created:** 2026-01-12
**Type:** code-notes

# osm-plotly-toggle-fixes-complete

## Summary

```
Fixed GPS preset selection issues and improved OSM-Plotly toggle smoothness for seamless data synchronization.
```

## Details

> This file documents fixes for GPS preset selection reliability in a Vue.js-based OSM-Plotly visualization system. The fixes address issues with dropdown selection updates, DOM value mismatches, and ensure OSM buildings persist correctly when toggling between OSM and Plotly views. Key improvements include DOM fallback reading, Vue reactivity enforcement, and explicit merging of OSM data into Plotly plots to prevent visibility gaps.

## Key Functions

### `onGpsPresetChange()`

Enhanced function to reliably update coordinates from a dropdown selection, using DOM fallback and Vue reactivity.

### `onToggleOSMView()`

Modified to merge OSM buildings into Plotly data, remove duplicates, and force updates to ensure synchronization.

### `getOSMBuildingsForPlotly()`

Helper function (likely in `osmIntegrationBox`) that extracts OSM building data for Plotly visualization.

## Usage

To apply these fixes:
1. Replace the problematic `onGpsPresetChange()` in `simulation/frontend/components/header-component.js` with the updated logic.
2. Modify `simulation/frontend/app-data.js` to include the enhanced `onToggleOSMView()` logic.
3. Ensure `osmIntegrationBox` is properly initialized and provides `getOSMBuildingsForPlotly()` with valid OSM data.

## Dependencies

> `Vue.js`
> `Plotly.js`
> `OpenStreetMap (OSM) API integration library (e.g.`
> ``osmIntegrationBox`)`
> ``simulation/frontend` module.`

## Related

- [[header-component]]
- [[app-data]]
- [[osmIntegrationBox]]

>[!INFO] Important Note
> The fixes rely on DOM element access via `querySelector` and Vue reactivity (`$nextTick`). Ensure the DOM is fully rendered before running these updates to avoid race conditions.

>[!WARNING] Caution
> Removing existing OSM buildings (`filter(b => b.type !== 'osm_hint')`) may cause data loss if buildings are critical for visualization. Test thoroughly in a staging environment before deployment.
