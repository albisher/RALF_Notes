**Tags:** #logging, #building-spawn, #system-step, #simulation, #debugging, #api-integration, #data-visualization, #workflow-state
**Created:** 2026-01-13
**Type:** code-notes

# building-spawn-and-system-step-logging

## Summary

```
Enhanced logging for building spawns and system workflow transitions to improve visibility and debugging.
```

## Details

> This document outlines fixes for two issues: (1) buildings were spawned without logging, and (2) system workflow steps weren’t logged. The solution includes:
> - **Building Spawn Logging**: Enhanced `spawn_invisible_building()` to log building details (name, position, dimensions) with structured data and a dedicated log type (`building_spawned`). API endpoints (`/api/buildings/spawn-random` and `/api/buildings/spawn-training`) were updated to log spawns and training workflows with summaries.
> - **System Step Logging**: Modified `_update_workflow_state()` to log transitions between states (e.g., `initializing → buildings_spawned`) with metadata like session ID and simulation time, using `system_step_completed`.

## Key Functions

### ``spawn_invisible_building()``

Enhanced logging for building spawns with detailed metadata.

### ``/api/buildings/spawn-random``

Added logging for API-triggered spawns with source identifier.

### ``/api/buildings/spawn-training``

Added start/completion logging for training workflows, including spawned buildings vs. requested count.

### ``_update_workflow_state()``

Logs all system state transitions with old/new states and optional reasons.

## Usage

1. **For Developers**:
   - Ensure `spawn_invisible_building()` is called with building data (e.g., `name`, `position`, `dimensions`).
   - Trigger API endpoints (`/api/buildings/spawn-random`, `/api/buildings/spawn-training`) to log spawns/training workflows.
   - Monitor logs in the UI for building spawns (`building_spawned`) and system steps (`system_step_completed`).

2. **For Users**:
   - Logs now appear in the UI with formatted visuals (e.g., emojis for states) and structured data for debugging.

## Dependencies

> `- `simulation/hmrs_simulation_live.py` (core logic)
- Logger system (for structured logging)
- API framework (for `/api/buildings/*` endpoints)`

## Related

- [[hmrs_simulation_live]]
- [[logging-configuration]]
- [[api-endpoints-reference]]

>[!INFO] Important Note
> Logs now include **formatted dimensions** (e.g., `10.5m × 8.2m × 3.0m`) and **total building counts** for context. Example:
> `🏢 Building spawned: Warehouse-01, dimensions: 10.5m × 8.2m × 3.0m, total_buildings: 4`.


>[!WARNING] Caution
> Overuse of `system_step_completed` logs may impact performance if workflow states are frequent. Ensure logs are filtered or throttled in production.
