**Tags:** #abstract-class, #drone-control, #physics-simulation, #motion-patterns, #multi-rotor, #pybullet
**Created:** 2026-01-13
**Type:** code-notes

# base_motion_pattern

## Summary

```
Core abstract base class defining drone motion pattern interfaces for physics-based flight simulation.
```

## Details

> This file defines an abstract base class (`BaseMotionPattern`) for drone motion patterns, enabling implementation of physics-driven control for various drone types (quadcopters, fixed-wing, VTOL, etc.). It uses PyBullet for physics simulation and enforces abstract methods for control computation, force application, and motor/actuator specifications. The class tracks drone state (mass, flight mode) and provides a framework for deriving specialized motion patterns.

## Key Functions

### ``MotionPatternType``

Enum defining supported drone types (e.g., `QUADCOPTER`, `HELICOPTER`).

### ``BaseMotionPattern.__init__()``

Initializes drone-specific parameters (mass, physics client) and state variables (e.g., `last_update_time`).

### ``compute_control()` (abstract)`

Abstract method to compute forces/torques for reaching a target position, accounting for wind.

### ``apply_forces()` (abstract)`

Abstract method to apply computed forces in PyBullet physics simulation.

### ``get_motor_count()` (abstract)`

Returns the number of motors/actuators for the drone type.

### ``get_max_thrust()` (abstract)`

Returns maximum thrust per motor/actuator.

### ``update(dt)``

Updates internal state (e.g., flight mode) over a time step `dt`.

## Usage

1. Subclass `BaseMotionPattern` for a specific drone type (e.g., `QuadcopterMotion`).
2. Implement abstract methods (`compute_control`, `apply_forces`, etc.) to define drone-specific physics and control logic.
3. Initialize with `motion_type` (e.g., `MotionPatternType.QUADCOPTER`) and pass a PyBullet client for simulation.
4. Call `update(dt)` to advance state and `compute_control()` to generate control outputs.

## Dependencies

> `numpy`
> `PyBullet (via `physics_client` parameter)`
> `typing extensions (Python 3.5+)`
> ``enum` module.`

## Related

- [[PyBullet Physics Simulation]]
- [[Drone Control Algorithms]]
- [[Multi-Rotor Flight Dynamics]]

>[!INFO] Abstract Methods Mandatory
> All derived classes **must** implement `compute_control()`, `apply_forces()`, `get_motor_count()`, and `get_max_thrust()` to avoid runtime errors. Failure to do so raises `TypeError`.

>[!WARNING] Physics Client Dependency
> The `physics_client` parameter (e.g., PyBullet ID) must be provided during initialization. If omitted, `apply_forces()` will fail silently. Always validate `physics_client` before use.
