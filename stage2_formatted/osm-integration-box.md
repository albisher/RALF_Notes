**Tags:** #Cesium, #OpenStreetMap, #3DVisualization, #Geospatial, #ViewSynchronization, #DataCaching, #PerformanceTracking
**Created:** 2026-01-13
**Type:** code-notes

# osm-integration-box

## Summary

```
Manages OpenStreetMap (OSM) building data integration and synchronization between Cesium 3D/2D views with performance tracking.
```

## Details

> The `OSMIntegrationBox` class handles OSM data loading, caches converted buildings for Plotly visualization, and manages synchronization between Cesium 3D and 2D top-viewers. It enforces single responsibility by isolating OSM data handling from viewer logic. Core features include:
> - Concurrent loading prevention via `_loadingBuildings` promise.
> - Highlighting selected buildings via `selectedBuildings` Map.
> - GPS-based view centering with `centerMarker3D`/`centerMarker2D` HTML overlays.
> - Comprehensive tracking of location updates, viewer commands, and performance metrics (e.g., `locationUpdateCounts`, `cesiumCommandCounts`).
> - Best-practice validation for Cesium commands (e.g., `requestRender` timing thresholds).

## Key Functions

### ``constructor()``

Initializes viewer references, caches, and tracking structures.

### ``_loadingBuildings``

Prevents concurrent OSM building loads via a promise.

### ``plotlyBuildingsCache``

Stores converted OSM buildings for Plotly visualization to avoid reprocessing.

### ``locationUpdateCounts``

Tracks frequency of location-based updates across views.

### ``cesiumCommandLog``

Logs all Cesium viewer commands for performance analysis.

### ``commandTiming``

Validates timing thresholds (e.g., 16ms between `requestRender` calls).

## Usage

1. Initialize the class: `const box = new OSMIntegrationBox()`.
2. Load OSM buildings: `box.loadOSMBuildings()`.
3. Sync views to location: `box.syncViewsToLocation(lat, lng)`.
4. Monitor performance via `box.cesiumCommandCounts` or `box.commandTiming`.

## Dependencies

> `Cesium.js`
> `Plotly.js (for building visualization)`
> `WebGL/HTML5 Canvas (for viewer rendering)`
> `Promises (for async control).`

## Related

- [[CesiumViewerIntegration]]
- [[OSMDataLoader]]
- [[PerformanceOptimizationGuide]]

>[!INFO] **Concurrency Prevention**
> `_loadingBuildings` ensures only one OSM load runs at a time, preventing race conditions.

>[!WARNING] **Cache Invalidation**
> `plotlyBuildingsCache` must be reset if OSM data changes significantly to avoid stale visualizations.
