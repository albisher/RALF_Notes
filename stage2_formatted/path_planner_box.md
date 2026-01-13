**Tags:** #path_planning, #obstacle_avoidance, #navigation, #robotics, #numpy
**Created:** 2026-01-13
**Type:** code-notes

# path_planner_box

## Summary

```
A modular path planner for safe navigation between waypoints with obstacle avoidance.
```

## Details

> The `PathPlannerBox` class implements a basic path planner that computes safe trajectories from a start position to a target position while avoiding obstacles. It uses a safety margin to ensure a buffer around obstacles. The planner first checks if a direct straight-line path is safe before attempting obstacle avoidance.

## Key Functions

### ``__init__(self, safety_margin`

float = 2.0)`**: Initializes the planner with a configurable safety margin around obstacles.

### ``plan_path(self, start, target, obstacles)``

Orchestrates path planning logic, returning either a direct path (if safe) or an avoidance path.

### ``_is_path_safe(self, start, target, obstacles)``

Evaluates whether a straight-line path between `start` and `target` intersects any obstacles within the safety margin.

### ``_plan_avoidance_path(self, start, target, obstacles)``

Implements a basic avoidance strategy (e.g., "go up and over") when direct path safety fails.

## Usage

1. Initialize the planner with a `safety_margin` (default: 2.0 meters).
2. Call `plan_path()` with:
   - `start`: Start position as a NumPy array `[x, y, z]`.
   - `target`: Target position as a NumPy array `[x, y, z]`.
   - `obstacles`: Optional list of obstacle dictionaries (e.g., `{'position': [x, y, z], 'radius': radius}`).
3. The method returns a list of waypoints (including `start` and `target`).

## Dependencies

> `numpy`
> `typing`

## Related

- [[none]]

>[!INFO] Safety Margin
> The `safety_margin` parameter ensures a buffer around obstacles (e.g., `2.0m`). Adjusting it may change collision detection sensitivity.

>[!WARNING] Simplistic Avoidance
> `_plan_avoidance_path()` uses a basic heuristic ("go up and over"). For complex scenes, consider A* or RRT algorithms for robustness.
