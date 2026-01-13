**Tags:** #robotics, #aerial_vehicles, #physics_simulation, #control_theory, #pybullet
**Created:** 2026-01-13
**Type:** code-notes

# helicopter_motion

## Summary

```
Implements a single-rotor helicopter motion control system for simulation using PyBullet.
```

## Details

> This file defines a `SingleRotorHelicopterMotion` class inheriting from `BaseMotionPattern`, implementing a control strategy for a single-rotor helicopter. It models lift via the main rotor and yaw control via a tail rotor, using collective and cyclic pitch inputs. The class computes control commands (collective pitch, cyclic pitch, roll, tail rotor) based on position/velocity errors relative to a target, accounting for wind and gravity. Key physics parameters like rotor thrust limits and mass are configurable.

## Key Functions

### ``__init__``

Initializes helicopter parameters (mass, rotor sizes, thrust limits) and inherits base motion pattern functionality.

### ``compute_control``

Core method that calculates pitch inputs for vertical/horizontal motion and tail rotor thrust based on error vectors and desired acceleration.

## Usage

1. Instantiate `SingleRotorHelicopterMotion` with desired physics parameters.
2. Call `compute_control()` with current state (position, velocity, orientation) and target coordinates to generate control inputs.
3. Apply outputs (collective/cyclic pitch) to helicopter actuators in simulation.

## Dependencies

> `numpy`
> `pybullet`
> ``.base_motion_pattern``

## Related

- [[helicopter_actuators]]
- [[base_motion_pattern]]

>[!INFO] Collective Pitch Clipping
> Collective pitch is clipped between 0.0 and 1.0 to prevent over-thrusting, though hover_collective is calculated as a fraction of max thrust.

>[!WARNING] Body-Frame Transformation Assumption
> The horizontal acceleration transformation assumes the helicopter’s forward axis aligns with the world’s X-axis; misalignment may require additional orientation corrections.
