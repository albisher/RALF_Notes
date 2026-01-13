**Tags:** #collision_avoidance, #attention_mechanisms, #uav_autonomy, #control_barrier_functions, #swarming_ai, #real_time_autonomy
**Created:** 2026-01-13
**Type:** code-notes

# attention_collision_avoidance_box

## Summary

```
Implements an attention-based collision avoidance system for drones using CBFs to prioritize nearby obstacles and drones.
```

## Details

> This module computes safe trajectories by dynamically allocating attention weights to relevant objects (obstacles or other drones) within a configurable radius. It uses a control barrier function (CBF) to enforce safe distances, ensuring real-time collision avoidance. The system prioritizes nearby objects (higher attention weights) while maintaining a safety margin beyond minimum distances. It logs warnings if required dependencies (`pyswarming` or `uav_collision_avoidance`) are unavailable, falling back to a generic fallback method.

## Key Functions

### ``compute_attention``

Assigns attention weights to obstacles/drones based on proximity, with closer objects receiving higher weights.

### ``__init__``

Initializes attention parameters (radius, max objects, safety margins) and internal tracking structures (attention_weights, collision_history).

## Usage

1. Initialize the box with desired parameters (e.g., `attention_radius=10.0`).
2. Call `compute_attention()` with current drone position and lists of obstacles/drones to derive attention weights and safe directions.
3. Integrate `safe_direction` and `attention_weights` into trajectory planning.

## Dependencies

> `pyswarming (optional)`
> `uav_collision_avoidance (optional)`
> `numpy`
> `logging`

## Related

- [[swarming_ai_notes]]
- [[control_barrier_functions_guide]]

>[!INFO] Attention Weighting Logic
> Attention weights decay exponentially with distance (implicitly handled via proximity-based prioritization). Objects beyond `attention_radius` are ignored.

>[!WARNING] Dependency Fallback
> If `pyswarming`/`uav_collision_avoidance` fails, the system defaults to a generic collision-avoidance fallback, potentially reducing precision. Test fallback behavior under edge cases.
