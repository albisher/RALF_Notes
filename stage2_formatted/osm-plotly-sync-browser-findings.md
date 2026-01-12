**Tags:** #browser-verification, #osm-integration, #plotly-sync, #vue-components, #cesium, #api-errors, #gps-presets, #network-issues
**Created:** 2026-01-12
**Type:** research

# osm-plotly-sync-browser-findings

## Summary

```
Browser verification report for OSM-Plotly synchronization system, highlighting functional components and critical issues in GPS preset selection, OSM building loading, and empty viewports.
```

## Details

> This document details findings from browser-based verification of an OSM-Plotly synchronization system using Vue components, Socket.IO, and Cesium viewers. While core functionality like page loading, view toggling, and camera reset works, critical issues prevent proper functionality: incorrect GPS preset dropdown values, failed OSM building API fetches, and empty visualization viewports. The verification was conducted via browser MCP tools on December 20, 2025.

## Key Functions

### ``simulation/frontend/components/header-component.js``

Manages GPS preset dropdown selection logic.

### ``simulation/frontend/boxes/osm-integration-box.js``

Handles OSM building data loading via Overpass API.

### ``loadBuildingsFromOverpass()``

Method responsible for fetching OSM building data with fallback mechanisms.

### `Socket.IO & Vue Components`

Enables real-time synchronization between OSM and Plotly views.

## Usage

To resolve issues:
1. Fix dropdown values in `header-component.js` to match expected preset keys.
2. Investigate Overpass API connectivity and bounding box calculations in `osm-integration-box.js`.
3. Ensure proper data flow between OSM and Plotly visualization components.

## Dependencies

> `Overpass API`
> `Cesium Ion`
> `Socket.IO`
> `Vue.js`
> `Plotly.js`
> `browser-based testing tools (MCP).`

## Related

- [[header-component]]
- [[osm-integration-box]]
- [[plotly-integration-box]]

>[!INFO] Important Note
> The Overpass API fallback mechanism (`Cesium Ion OSM Buildings`) is being used as a secondary source, but the primary API fetch fails, indicating a deeper connectivity or configuration issue.


>[!WARNING] Caution
> Incorrect GPS coordinates (e.g., `44.1253970, -146.97008`) will persist until the dropdown logic in `header-component.js` is corrected, leading to misaligned map views.
