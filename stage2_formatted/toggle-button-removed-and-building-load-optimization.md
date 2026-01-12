**Tags:** #optimization, #ui-design, #concurrency-control, #api-integration, #cesium, #frontend
**Created:** 2026-01-12
**Type:** code-notes

# toggle-button-removed-and-building-load-optimization

## Summary

```
Removed redundant toggle button and optimized building load to prevent concurrent API calls and improve performance.
```

## Details

> This document details the removal of a toggle button for Plotly/OSM switching and the implementation of a load optimization system for building data. The toggle button was redundant since OSM is now handled via a dedicated left-side button, and Quad View defaults to Plotly. The optimization prevents multiple concurrent building loads by tracking a loading promise, ensuring efficient API usage and avoiding duplicate entities.

## Key Functions

### ``loadOSMBuildings``

Async function that loads building data with concurrency prevention.

### ``clearOSMBuildings``

Clears existing building data before reloading.

### ``onToggleOSMView`** (in `app-data.js`)`

Internal handler for OSM toggle logic (still functional but UI removed).

## Usage

1. **Toggle Button Removal**:
   - Remove UI references to the toggle button in frontend components.
   - Ensure OSM toggle logic remains functional via `onToggleOSMView` (internal use only).

2. **Building Load Optimization**:
   - Call `loadOSMBuildings(latitude, longitude, options)` to load buildings.
   - The function internally handles concurrency prevention and cleanup.

## Dependencies

> ``simulation/frontend/components/visualization-view-component.js``
> ``simulation/frontend/pages/simulation-page-component-layout5.js``
> ``simulation/frontend/app-component.js``
> ``simulation/frontend/app-data.js``
> `Cesium Ion/Overpass API`
> ``nu` (likely a utility for clearing promises).`

## Related

- [[visualization-view-component]]
- [[simulation-page-component-layout5]]
- [[app-data]]

>[!INFO] Concurrent Load Prevention
> The `_loadingBuildings` promise ensures no duplicate API calls by checking if a load is already in progress. This prevents redundant data fetching and improves performance.

>[!WARNING] Internal Logic Preserved
> While the UI toggle button is removed, the `onToggleOSMView` function remains active for internal OSM view toggling. Ensure backward compatibility if needed.
