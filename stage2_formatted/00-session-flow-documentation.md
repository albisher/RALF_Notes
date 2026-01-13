**Tags:** #session_management, #api_endpoints, #simulation_flow, #workflow_automation, #parallel_execution
**Created:** 2026-01-13
**Type:** documentation

# 00-session-flow-documentation

## Summary

```
Documentation outlining session lifecycle, initialization, and preparation workflows for the HMRS simulation system.
```

## Details

> This document details how sessions are created, initialized, and prepared in the HMRS simulation system. It covers key API triggers (`/api/start`, `/api/restart`, `/api/sessions/create-demo`) and the internal logic for session state management, including clearing drones, generating IDs, and preparing scenes (e.g., spawning buildings). The workflow emphasizes modularity, with scene preparation being automatic during session initialization.

## Key Functions

### ``_initialize_session()``

Clears drones, generates session ID, resets state, and prepares scene (buildings/master base) for a new session.

### ``run_simulation_thread()``

Starts the background simulation thread after validating session readiness and ensuring scene readiness.

### ``_clear_all_drones_for_new_session()``

Removes all drones from previous sessions.

### ``_spawn_initial_buildings()``

Dynamically spawns buildings if none exist (only during non-running simulations).

## Usage

To trigger a new session:
1. Call `/api/start` (or `/api/restart`/`create-demo`) to start the workflow.
2. The system automatically:
   - Initializes session state.
   - Prepares the scene (buildings/master base).
   - Starts the simulation thread in the background.
3. Session ID is auto-generated in `YYYYMMDDHHMM` format.

## Dependencies

> ``datetime``
> ``os.path``
> ``pathlib.Path``
> ``threading``
> ``hmrs_simulation_live.py` (core simulation logic)`
> ``training_sessions_dir` (directory for session storage).`

## Related

- [[`00-core_simulation_logic]]
- [[`00-data_preparation]]

>[!INFO] **Session ID Format**
> Session IDs follow `YYYYMMDDHHMM` (e.g., `202412191430`), ensuring uniqueness across sessions.

>[!WARNING] **Thread Safety**
> Background threads (e.g., `run_simulation_thread`) are daemonized—ensure the main process exits cleanly to avoid resource leaks.
