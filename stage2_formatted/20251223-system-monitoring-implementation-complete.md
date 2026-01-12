**Tags:** #system-monitoring, #logging-separation, #frontend-implementation, #error-handling, #dashboard
**Created:** 2026-01-12
**Type:** code-notes

# simulation/frontend/pages/system-monitoring-page-component.js

## Summary

```
Implements a dedicated system monitoring page for tracking errors, alerts, and performance metrics, separating simulation logs from system logs.
```

## Details

> This component creates a comprehensive system monitoring dashboard (`/sm/`) that consolidates all system-level logs, errors, and alerts. The implementation separates simulation logs (e.g., drone commands, sensor data) from system logs (e.g., API failures, OSM errors) and routes them to distinct panels. The main page now displays a notification indicator when system issues are detected, directing users to the monitoring page for detailed diagnostics.
> 
> The system logs panel includes error logs, alerts, network diagnostics, and performance metrics, while simulation logs remain in the sidebar. The design ensures minimal UI disruption by hiding the indicator on the monitoring page and linking it to the `/sm/` route.

## Key Functions

### ``SystemMonitoringPageComponent``

Main dashboard rendering system health metrics, logs, and alerts.

### ``isSimulationLog()``

Helper function to classify logs as simulation vs. system logs.

### ``hasSystemIssues()``

Computed property detecting active errors/alerts for the notification indicator.

### ``systemLogs`, `systemErrorLog`, `systemAlerts``

Computed properties aggregating system-level log data.

## Usage

1. Navigate to `/sm/` to view the system monitoring dashboard.
2. Use the bottom-right indicator to trigger a redirect to `/sm/` when system issues are detected.
3. Interact with panels (e.g., expand error logs, refresh metrics) to diagnose problems.

## Dependencies

> ``simulation/frontend/app.js``
> ``simulation/frontend/app-component.js``
> ``simulation/frontend/boxes/url-routing-box.js``
> ``simulation/frontend/boxes/layout-navigation-box.js``
> ``simulation/frontend/index.html``
> ``simulation/frontend/app-data.js``
> ``simulation/frontend/components/logs-sidebar-component.js``

## Related

- [[app-component]]
- [[app-data]]
- [[url-routing-box]]

>[!INFO] Log Separation Logic
> The `isSimulationLog()` function relies on the presence of `sim_time` in log entries to distinguish between simulation and system logs. Ensure all logs adhere to this convention to avoid misclassification.

>[!WARNING] Indicator Visibility
> The system issues indicator is **hidden** when on the `/sm/` page to prevent redundant navigation. Ensure the route `/sm/` is correctly mapped in `url-routing-box.js` to avoid broken links.
