**Tags:** #autonomous_drones, #state_machine, #exploration_algorithms, #robotics
**Created:** 2026-01-13
**Type:** code-notes

# exploration_manager_box

## Summary

```
Manages autonomous exploration lifecycle for drones using frontier detection.
```

## Details

> The `ExplorationManagerBox` class implements a state machine to coordinate autonomous exploration of an environment. It processes inputs from a drone’s state (position/orientation) and sensor data (via `lidar_box`) to generate commands (scan, move_to, completed, wait). The system transitions between states: **idle** → **scanning** (on initialization), **scanning** → **moving** (after frontier selection), **moving** → **scanning** (when target reached), and **scanning** → **completed** (when no frontiers remain). The manager enforces a `scan_interval` to regulate sensor updates and tracks exploration metrics like distance traveled and scan count.

## Key Functions

### ``__init__``

Initializes the manager with dependencies (`lidar_box`, `frontier_explorer`) and sets up state tracking (e.g., `exploration_state`, `scan_interval`).

### ``update``

Core method that dispatches to state-specific handlers (`_handle_idle_state`, `_handle_scanning_state`, etc.) based on the current state, returning an action dictionary.

### ``_handle_idle_state``

Starts scanning immediately after initialization.

### ``_handle_scanning_state``

Processes sensor data to detect frontiers and transition to moving state (missing in snippet; implied to call `frontier_explorer`).

### ``_handle_moving_state``

(Incomplete in snippet) Likely handles path planning and collision avoidance (via `collision_avoidance`).

## Usage

1. Initialize with required dependencies (e.g., `lidar_box`, `frontier_explorer`).
2. Call `update()` periodically with drone state and simulation time to generate actions.
3. State transitions are managed internally; external code should only interact via `update()`.

## Dependencies

> ``numpy``
> ``typing` (Python standard libraries)`
> ``lidar_box` (custom `AdvancedLiDARBox`)`
> ``frontier_explorer` (custom `FrontierExplorerBox`)`
> ``collision_avoidance` (optional `AttentionCollisionAvoidanceBox`).`

## Related

- [[None]]

>[!INFO] State Machine Design
> The state machine (`idle` → `scanning` → `moving` → `scanning` → `completed`) ensures deterministic exploration progression. Missing `_handle_moving_state` implies collision avoidance and pathfinding logic must be implemented separately.

>[!WARNING] Scan Interval Enforcement
> The `scan_interval` (default: 2.0s) prevents excessive sensor data overload. Override cautiously if real-time constraints require shorter intervals.
