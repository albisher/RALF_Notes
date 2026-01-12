**Tags:** #monitoring, #performance, #cesium, #plotly, #real-time-data, #logging, #system-metrics
**Created:** 2026-01-12
**Type:** documentation

# view-loading-time-monitoring-2025-01-27

## Summary

```
Tracks and visualizes loading performance metrics for multiple 2D/3D views across Cesium and Plotly systems.
```

## Details

> This implementation monitors loading times for six views (2D Top, Front, Side, and 3D Isometric variants) across two rendering engines (Cesium and Plotly). It records metrics like last/average/min/max load times, load counts, and a rolling history of the last 100 loads. The system integrates with a dedicated `/sm/` dashboard to display these metrics in color-coded sections, while logging all data to system logs with a `view_performance` type.

## Key Functions

### ``trackViewLoadingTime(viewKey, loadingTimeMs, trigger)``

Records and updates loading statistics for a given view.

### ``simulation/frontend/boxes/system-monitoring-box.js``

Manages the UI display of loading metrics (e.g., `loadingTimes`, `avgLoadingTime`).

### ``simulation/frontend/app-data.js``

Tracks triggers (e.g., `page-load`, `layout-mode-change`) and initializes timing measurements for views.

## Usage

1. **Trigger Monitoring**: Call `trackViewLoadingTime()` after refreshing a view (e.g., via `command`, `user-change`, or `refresh`).
2. **View Metrics**: Access metrics via `viewStatus` (e.g., `viewStatus.cesium2DTop.loadingTimes`).
3. **Dashboard Access**: Navigate to `/sm/` to view real-time performance data.

## Dependencies

> `Cesium.js`
> `Plotly.js`
> `system-monitoring utilities (e.g.`
> `logging framework)`
> `frontend UI components (e.g.`
> ``simulation/frontend/boxes`).`

## Related

- [[system-monitoring-box]]
- [[app-data]]
- [[system-monitoring-logs]]

>[!INFO] Trigger Flexibility
> The `trackViewLoadingTime()` function accepts a `trigger` parameter to categorize load events (e.g., `'layout-mode-change'` for Quad View switches).

>[!WARNING] Data Retention
> The `loadingTimes` array caps at 100 entries; older values are discarded to maintain performance.
