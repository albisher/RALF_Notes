**Tags:** #drone-autonomy, #path-planning, #box-based-architecture, #navigation, #gps-tracking
**Created:** 2026-01-13
**Type:** code-notes

# worker_drone_boxed

## Summary

```
Worker drone implementation using a box-based architecture for path planning and control.
```

## Details

> The `WorkerDroneBoxed` class extends `BaseDrone` and refactors drone navigation using `PathPlannerBox` for path generation. It integrates a GPS tracker (`GPSTracker`) and battery model (`BatteryModel`) for autonomous operations. The drone processes commands via `receive_command`, delegating path planning to `PathPlannerBox` while optionally using `MLControllerBox` for advanced control (falling back to PID if disabled). Navigation state includes waypoint tracking, connection status, and performance metrics.

## Key Functions

### ``__init__``

Initializes drone with box-based components (path planner, ML controller), sensors (GPS, battery), and navigation state.

### ``receive_command``

Parses incoming commands (e.g., `move_to`) and triggers path planning via `PathPlannerBox`.

### ``_plan_path_to_target`** (implicitly called)`

Internal method to generate a path to a target position using `PathPlannerBox`.

## Usage

1. Instantiate `WorkerDroneBoxed` with drone ID, initial position, physics client, and worker ID.
2. Set `use_ml_control=True` to enable ML-based control (default: PID fallback).
3. Send commands (e.g., `move_to`) via `receive_command` to update target position/height.
4. Path planning is handled internally by `PathPlannerBox`.

## Dependencies

> ``.base_drone``
> ``.gps_tracker``
> ``.battery_model``
> ``.boxes` (contains `PathPlannerBox``
> ``MLControllerBox`)`
> ``numpy``
> ``time`.`

## Related

- [[worker_drone_base]]
- [[path_planner_box]]
- [[gps_tracker]]

>[!INFO] Path Delegation
> All navigation logic is encapsulated in `PathPlannerBox`, ensuring modularity and reusability. Avoid bypassing this interface to maintain consistency.

>[!WARNING] Command Validation
> Ensure `command['type']` matches expected values (e.g., `'move_to'`). Invalid types may cause silent failures in path planning.
