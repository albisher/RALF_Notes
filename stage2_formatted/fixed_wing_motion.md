**Tags:** #aerodynamics, #fixed-wing, #robotics, #physics-simulation, #control-theory, #pybullet
**Created:** 2026-01-13
**Type:** code-notes

# fixed_wing_motion

## Summary

```
Handles fixed-wing aircraft motion control with thrust, lift, and stability calculations for forward flight.
```

## Details

> This file defines a `FixedWingMotion` class inheriting from `BaseMotionPattern`, implementing forward-flight control for a fixed-wing aircraft. It calculates throttle, aileron, elevator, and rudder inputs based on airspeed, position error, and orientation. Aerodynamic coefficients (lift/drag) and control surface limits are initialized, while stall-speed detection ensures safe minimum airspeed. The `compute_control` method uses PyBullet’s physics client to derive forward direction from orientation and applies proportional control to track a target position.

## Key Functions

### ``__init__``

Initializes fixed-wing parameters (mass, wing area, thrust limits, stall speed) and aerodynamic coefficients.

### ``compute_control``

Computes control inputs (throttle, aileron, elevator, rudder) via PID-like logic for airspeed and heading alignment.

## Usage

1. Instantiate `FixedWingMotion` with aircraft-specific parameters.
2. Call `compute_control` with current state (position, velocity, orientation) and target waypoint.
3. Apply returned control signals (throttle, aileron, etc.) to actuators.

## Dependencies

> `numpy`
> `pybullet`
> ``.base_motion_pattern``

## Related

- [[base_motion_pattern]]
- [[pybullet_physics_client]]

>[!INFO] Aerodynamic Assumptions
> Assumes constant lift/drag coefficients; real-world aircraft require dynamic tuning (e.g., angle-of-attack-dependent lift).

>[!WARNING] Stall Risk
> Below `min_airspeed`, throttle is forced to 1.0 to avoid stall; abrupt throttle changes may cause oscillations.
