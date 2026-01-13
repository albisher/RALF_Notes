**Tags:** #physics-simulation, #aerial-vehicles, #tiltrotor, #robotics, #pybullet, #motion-control
**Created:** 2026-01-13
**Type:** code-notes

# tiltrotor_motion

## Summary

```
Implements a tiltrotor motion control system for VTOL-to-forward flight transitions.
```

## Details

> This file defines a `TiltrotorMotion` class inheriting from `BaseMotionPattern`, handling dynamic rotor tilt between vertical (VTOL) and horizontal (forward flight) configurations. It uses PyBullet for physics simulation and computes control inputs based on airspeed and position error. The system transitions smoothly between flight modes (vertical, transition, forward) by adjusting rotor tilt angles, with parameters like thrust distribution and tilt rate governing behavior.

## Key Functions

### ``__init__``

Initializes tiltrotor parameters (mass, motor count, thrust limits, wing area) and sets up VTOL/forward flight transition logic.

### ``compute_control``

Determines rotor tilt angle and thrust distribution based on airspeed and position error, returning a control dictionary for PyBullet.

### ``self.mode``

Tracks current flight mode (vertical, transition, forward) and updates dynamically.

### ``self.rotor_tilt_angle``

Stores current rotor tilt angle (0° vertical, 90° horizontal) with gradual transitions.

## Usage

1. Instantiate `TiltrotorMotion` with desired parameters (e.g., `TiltrotorMotion(mass=4.0, motor_count=2)`).
2. Call `compute_control` with current state (position, velocity, orientation) and target waypoint.
3. Use returned `thrusts` and `tilt_angle` to drive PyBullet physics simulation.

## Dependencies

> `numpy`
> `pybullet`
> ``.base_motion_pattern` (BaseMotionPattern class)`

## Related

- [[base_motion_pattern]]
- [[pybullet_physics_simulation]]

>[!INFO] Mode Transition Logic
> The airspeed thresholds (8.0 m/s → vertical, 15.0 m/s → transition) and tilt rate (30°/s) define smooth VTOL-to-forward transitions. Adjust these values for performance tuning.

>[!WARNING] Tilt Angle Clamping
> The `tilt_rate` and `min/max` checks in `compute_control` prevent overshooting desired tilt angles, but abrupt changes may cause jitter. Smoother interpolation could improve stability.
