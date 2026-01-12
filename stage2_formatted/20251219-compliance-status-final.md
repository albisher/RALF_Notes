**Tags:** #compliance, #logging, #debugging, #backend, #simulation
**Created:** 2026-01-12
**Type:** code-notes

# simulation/swarm/boxes/logging_box.py

## Summary

```
Tracks and manages log data across simulation components for structured compliance and debugging.
```

## Details

> This file implements a centralized `LoggingBox` system to standardize logging across the simulation framework. It replaces legacy `print()` statements with a unified logging mechanism, supporting multiple output channels (UI, console, Socket.IO, API, file) and log-level filtering. The system includes history management, statistics tracking, and integration with Vue.js for frontend display. The backend component handles log routing and storage, while the frontend component visualizes logs in real-time.

## Key Functions

### ``simulation/swarm/boxes/logging_box.py``

Core logging backend with standardized format, multi-channel output, and history management.

### ``simulation/frontend/boxes/logging-box.js``

Frontend Vue app integration for UI-based log display and console routing.

### ``simulation/swarm/boxes/__init__.py``

Exports the `LoggingBox` for modular use across the simulation.

### ``log()` method (CoreClass)`

Updated to use `LoggingBox` instead of direct `print()` calls.

## Usage

1. Initialize `LoggingBox` in `__init__` of any simulation class.
2. Replace legacy `print()` statements with `log()` method calls.
3. Use `LoggingBox` for structured logging (e.g., `logging_box.log("Event", level="INFO")`).
4. Frontend components route logs via `console.log` to the `logging-box.js` handler.

## Dependencies

> ``simulation/swarm/boxes/__init__.py``
> ``simulation/frontend/index.html``
> ``simulation/frontend/app.js``
> `Vue.js`
> `Socket.IO`
> `Python logging utilities (if applicable).`

## Related

- [[app]]
- [[__init__]]
- [[logging-box]]
- [[hmrs_simulation_core]]

>[!INFO] Important Note
> The `LoggingBox` system is designed to replace ~100+ legacy `print()` statements across the simulation. Debug logs in `update()` methods (e.g., in `BaseDrone`) remain as exceptions due to dynamic execution contexts.


>[!WARNING] Caution
> Remaining `console.log()` calls (~100+) in `app-data.js` and other components must be audited to avoid bypassing the `LoggingBox` integration. Incomplete frontend log routing may lead to inconsistent UI visibility.
