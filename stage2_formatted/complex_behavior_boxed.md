**Tags:** #drone-autonomy, #modular-architecture, #behavioral-boxes, #path-planning, #obstacle-avoidance
**Created:** 2026-01-13
**Type:** code-notes

# complex_behavior_boxed

## Summary

```
Drone autonomy implementation using modular behavioral boxes for path planning and obstacle avoidance.
```

## Details

> This file implements a `ComplexBehaviorDrone` class that integrates multiple specialized "box" components to achieve autonomous navigation. The drone uses a modular design where each behavior (path planning, obstacle detection, control logic) is encapsulated in separate boxes, accessed only through defined interfaces. The system dynamically replans paths when obstacles are detected or when a new target is set, leveraging LiDAR and camera inputs for real-time decision-making.
> 
> The `ComplexBehaviorDrone` initializes with four key boxes (`MLControllerBox`, `PathPlannerBox`, `LiDARProcessorBox`, `CameraProcessorBox`) and integrates them through their interfaces, ensuring no bypass of intended behavior logic. Sensors (GPS, battery, weather) and navigation state variables (target position, current path, waypoints) are managed internally, with path replanning triggered periodically.

## Key Functions

### ``set_target``

Updates the navigation target and triggers path replanning.

### ``_replan_path``

Orchestrates obstacle detection via LiDAR and path recalculation via `PathPlannerBox`.

### ``MLControllerBox``

Handles execution logic for waypoint navigation.

### ``PathPlannerBox``

Generates safe paths while accounting for obstacle clearance.

### ``LiDARProcessorBox``

Detects obstacles using raycasting from drone position.

### ``CameraProcessorBox``

(Incomplete in snippet) Likely provides visual verification feedback.

## Usage

1. Initialize `ComplexBehaviorDrone` with drone ID, starting position, and physics client.
2. Call `set_target(new_position)` to update navigation goals.
3. The drone automatically replans paths every `replan_interval` (2s) if obstacles are detected or conditions change.
4. Boxes (`MLControllerBox`, `PathPlannerBox`) are instantiated and configured via constructor arguments.

## Dependencies

> ``.base_drone``
> ``.gps_tracker``
> ``.battery_model``
> ``.weather_system``
> ``.boxes` (contains `MLControllerBox``
> ``PathPlannerBox``
> ``LiDARProcessorBox``
> ``CameraProcessorBox`)`
> ``numpy``
> ``time`.`

## Related

- [[drone_autonomy_architecture]]
- [[modular_behavior_components]]

>[!INFO] Modularity Enforcement
> The design enforces strict box interfaces, preventing direct bypass of intended behavior logic (e.g., no direct path recalculation outside `PathPlannerBox`). This ensures maintainability and predictability.

>[!WARNING] Reactive Behavior Limitation
> The `max_range` for `LiDARProcessorBox` is set to 50.0m, but the snippet shows a shorter range (50.0) in initialization. Ensure this matches intended obstacle detection scope to avoid premature replanning or missed detections.
