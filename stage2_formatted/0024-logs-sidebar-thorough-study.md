**Tags:** #logging-system, #sidebar-ui, #real-time-data, #socket-io, #backend-frontend-integration, #performance-optimization, #data-flow, #error-handling
**Created:** 2026-01-12
**Type:** research

# 0024-logs-sidebar

## Summary

```
Comprehensive analysis of the logging system and logs sidebar implementation, identifying gaps in integration, format consistency, and real-time updates.
```

## Details

> This study evaluates the current state of the logging infrastructure, focusing on the **LoggingBox** backend and frontend components. The system uses a hybrid approach with **Socket.IO** for real-time updates and **API polling**, but inefficiencies exist due to redundant data flows. The logs sidebar displays logs via a UI component, but data inconsistencies arise from mismatched backend/frontend log formats and disconnected Socket.IO event handling. The research highlights lingering legacy `print()` and `console.log()` statements and incomplete integration of LoggingBox across modules.

## Key Functions

### `LoggingBox (Backend)`

Manages log standardization, filtering, and output channels (UI, console, Socket.IO, API, file).

### `LoggingBox (Frontend)`

JavaScript counterpart with Vue integration, handling UI routing and error/communication logs.

### `Socket.IO Event Mismatch`

Backend emits `'log-update'`; frontend expects `'communication-log-update'` (batch logs).

### `Legacy Fallbacks`

~60-70 `print()` and ~30-40 `console.log()` statements bypass LoggingBox.

### `Data Flow`

Logs from `BaseDrone`, `MasterCoordinator`, and `HMRSSimulationLive` use LoggingBox, but ~30% still rely on older mechanisms.

## Usage

To analyze logs via the sidebar:
1. Ensure LoggingBox is initialized in all relevant modules (e.g., `BaseDrone`, `MasterCoordinator`).
2. Verify Socket.IO event consistency between backend (`'log-update'`) and frontend (`'communication-log-update'`).
3. Replace legacy `print()`/`console.log()` with LoggingBox for standardized output.

## Dependencies

> `- Backend: `simulation/swarm/boxes/logging_box.py`
- Frontend: `simulation/frontend/boxes/logging-box.js`
- External: Socket.IO library`
> `Vue.js framework (for frontend integration).`

## Related

- [[LoggingSystemArchitecture]]
- [[SocketIOIntegrationGuide]]

>[!INFO] **Critical Event Mismatch**
> The backend emits `'log-update'` (single log), but the frontend expects `'communication-log-update'` (batch logs). This disconnect causes incomplete log updates in the sidebar.

>[!WARNING] **Performance Overhead**
> Redundant polling (500ms API + 2s Socket.IO) degrades real-time responsiveness. Optimize by unifying log sources or reducing polling frequency.
