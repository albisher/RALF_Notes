**Tags:** #logging, #verification, #system-monitoring, #api-checklist, #drone-simulation
**Created:** 2026-01-12
**Type:** documentation

# logging-verification-checklist

## Summary

```
A checklist for verifying and ensuring proper logging of system interactions, API calls, and drone simulation events in a simulation environment.
```

## Details

> This document outlines a structured checklist for verifying logging functionality across multiple components of a simulation system. It details expected logs for API interactions, system monitoring, command tracking, and drone simulation events. The checklist is divided into two main sections: logs in the `/sm/` page (system monitoring) and logs in the right sidebar (drone simulation). It also includes current working statuses and areas needing verification.

## Key Functions

### `API Call Logging`

Tracks all API interactions with method, endpoint, status, and response time.

### `System Monitoring Box`

Captures box commands (Cesium/Plotly) and responses.

### `Command Tracking`

Logs sent commands, responses, and pending statuses for drones.

### `View Status Tracking`

Monitors statuses of all views, container IDs, timestamps, and errors.

### `Drone Simulation Logs`

Records drone positions, sensor/motor readings, and communication messages.

## Usage

This checklist is used to verify that all logging components (system monitoring, API logs, command tracking, and simulation logs) function correctly. It guides manual verification steps for each logged event, ensuring comprehensive coverage of system operations.

## Dependencies

> `FetchInterceptor (for API call logging)`
> `simulation backend components (Cesium/Plotly)`
> `drone management system.`

## Related

- [[Logging Infrastructure Design]]
- [[API Documentation]]
- [[Drone Simulation Guide]]

>[!INFO] Important Note
> The checklist assumes the system uses a FetchInterceptor for API logging. Ensure this interceptor is properly integrated and configured to capture all relevant API calls accurately.


>[!WARNING] Caution
> Verify the INFO level for box command logging, as it may not capture all necessary details if misconfigured. Cross-check with the actual system logs to ensure completeness.
