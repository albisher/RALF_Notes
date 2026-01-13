**Tags:** #drone-control, #physics-simulation, #multi-rotor, #pybullet, #numerical-motion
**Created:** 2026-01-13
**Type:** code-notes

# multirotor_motion

## Summary

```
Core motion pattern implementation for quad/hex/octocopter drones with physics-based control.
```

## Details

> This file defines a base class (`MultiRotorMotion`) for simulating multi-rotor drones (quadcopters, hexacopters, octocopters) using PyBullet physics. It handles motor positioning, thrust distribution, and PID-like control gains for position and attitude stabilization. The class inherits from `BaseMotionPattern` and initializes motor configurations based on the drone type (4, 6, or 8 motors), calculating their positions in the body frame relative to the drone’s center.
> 
> Key components include:
> - Motor position calculations for different layouts (e.g., X-configuration for quadcopters, circular for octocopters).
> - Control gains (`kp_position`, `kd_position`, etc.) tuned for responsiveness and damping.
> - Integration with PyBullet for physics simulation via a physics client ID.

## Key Functions

### ``_calculate_motor_positions()``

Computes motor positions in the body frame based on `motor_count` (4, 6, or 8) and `arm_length`.

### ``__init__()``

Initializes drone parameters (mass, thrust limits, motor count) and inherits from `BaseMotionPattern`.

## Usage

1. Subclass `MultiRotorMotion` for a specific drone type (e.g., `QuadcopterMotion`).
2. Override control logic or physics callbacks as needed.
3. Pass a PyBullet client ID to enable real-time simulation.

## Dependencies

> `numpy`
> `pybullet`
> ``.base_motion_pattern` (custom module)`

## Related

- [[base_motion_pattern]]
- [[drone_physics_simulation]]

>[!INFO] Motor Positioning Logic
> The `_calculate_motor_positions()` method uses trigonometric functions to distribute motors evenly around the drone’s center. For hex/octocopters, angles are sampled linearly to avoid gaps.

>[!WARNING] Physics Client Dependency
> If `physics_client` is `None`, the drone will not interact with PyBullet’s physics engine. Ensure this is set before simulation begins.
