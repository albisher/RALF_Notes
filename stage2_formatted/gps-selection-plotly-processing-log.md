**Tags:** #logging, #gps, #plotly, #user-interaction, #system-monitoring, #data-visualization, #quad-view
**Created:** 2026-01-12
**Type:** code-notes

# gps-selection-logging

## Summary

```
Tracks and logs Plotly processing activity triggered by GPS location selection for system monitoring.
```

## Details

> This logging system records Plotly update events after GPS location selection (preset, custom, or random) to ensure visibility into user interactions. The log captures metadata like coordinates, layout mode, and OSM settings, enabling debugging and performance analysis. The implementation logs to a centralized monitoring system (`/sm/`) under "View & Usage Logs" for easy filtering and inspection.

## Key Functions

### ``onUpdateGpsPosition()``

Triggers Plotly update logging before `updatePlotsWithData()`.

### ``updatePlotsWithData()``

Updates Plotly views with new GPS data (called after logging).

### ``loggingBox.log()``

Internal logging function (via `window.loggingBox`) that formats and sends structured logs to the system monitoring dashboard.

## Usage

1. **Trigger**: When a user selects a GPS location (via preset, custom, or random selection).
2. **Action**: The `onUpdateGpsPosition()` method logs Plotly processing details before updating views.
3. **View**: Navigate to `/sm/` → "View & Usage Logs" to filter logs by `source: 'MainAppData'` and `action: 'gps_selection_plotly_update'`.

## Dependencies

> ``simulation/frontend/app-data.js``
> ``system-monitoring-page-component.js``
> ``loggingBox` (custom logging utility).`

## Related

- [[system-monitoring-page-component]]
- [[loggingBox implementation]]

>[!INFO] Important Note
> The log includes **fallback values** (e.g., `this.data.buildings ? ... : 0`) to handle undefined arrays gracefully, ensuring robustness.

>[!WARNING] Caution
> Ensure `window.loggingBox` is initialized before calling `loggingBox.log()` to avoid `undefined` errors. Verify the `View & Usage Logs` filter matches the exact `type: 'user_interaction'` and `action` criteria.
