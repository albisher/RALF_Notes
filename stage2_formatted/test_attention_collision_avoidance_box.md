**Tags:** #unittest, #swarm, #autonomous-systems, #collision-avoidance, #attention-box
**Created:** 2026-01-13
**Type:** code-notes

# test_attention_collision_avoidance_box

## Summary

```
Tests for an attention collision avoidance mechanism in drone swarm navigation.
```

## Details

> This file contains unit tests for `AttentionCollisionAvoidanceBox`, a component designed to prevent collisions by dynamically tracking nearby obstacles and drones within a defined radius. The tests verify initialization, attention computation (filtering objects outside the radius), and safe trajectory generation (evaluating collision risk and avoidance needs). The `compute_attention` method checks which objects (obstacles/drones) fall within the drone’s attention radius, while `compute_safe_trajectory` assesses path safety and suggests avoidance maneuvers if obstacles are detected.

## Key Functions

### ``AttentionCollisionAvoidanceBox``

Core class encapsulating collision avoidance logic with configurable parameters (e.g., `attention_radius`, `max_attention_objects`).

### ``compute_attention``

Filters objects (obstacles/drones) based on Euclidean distance from the drone’s current position, returning a dictionary of tracked objects and their proximity scores.

### ``compute_safe_trajectory``

Evaluates a target path, computes collision risk, and returns a decision (e.g., `requires_avoidance`) if obstacles are detected within the safety margin.

## Usage

1. Initialize the box with parameters (e.g., `attention_radius=10.0`).
2. Call `compute_attention` to get nearby objects (obstacles/drones) within the radius.
3. Call `compute_safe_trajectory` to analyze a path and determine collision risk/avoidance needs.

## Dependencies

> `numpy`
> `unittest`
> `swarm.boxes.attention_collision_avoidance_box`

## Related

- [[swarm.boxes.attention_collision_avoidance_box]]
- [[swarm.test.test_attention_collision_avoidance_box]]

>[!INFO] Parameter Sensitivity
> The `safety_margin` and `min_safe_distance` parameters critically influence collision detection thresholds. Adjusting them alters when avoidance actions are triggered.

>[!WARNING] Distance Metric
> Euclidean distance is used for proximity checks. For curved paths or non-linear trajectories, this may underestimate risk in complex environments.
