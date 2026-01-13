**Tags:** #drone-control, #rc-translation, #motor-thrust, #swarm-ai, #direct-control
**Created:** 2026-01-13
**Type:** code-notes

# rc-translator-box-created

## Summary

```
Converts RC-style commands into motor thrusts for direct drone control in a swarm system.
```

## Details

> This box translates simple RC commands (e.g., `up`, `left`) into proportional motor thrust values for quadcopter/octocopter drones. It maintains an internal state of throttle, roll, pitch, yaw, and speed multiplier, scaling them between -1.0 to 1.0 (or 0.1–2.0 for speed). Motor thrusts are computed via control mixing, supporting both 4-motor and 8-motor configurations. The system integrates with a `BaseDrone` class, enabling direct command execution when `command_mode == 'rc'`.

## Key Functions

### ``RCCommandTranslatorBox``

Core class initializing RC state and motor calculations.

### ``process_rc_command()``

Handles individual commands (e.g., `up`, `yaw_right`) with optional intensity.

### ``compute_thrusts()``

Generates motor thrust vectors based on current RC state.

### ``rc_translator` attribute`

Attached to `BaseDrone` for direct command routing.

## Usage

1. Initialize with `RCCommandTranslatorBox(motor_count=4, base_thrust=0.5)`.
2. Call `process_rc_command()` for discrete commands or set raw RC state via API.
3. Retrieve thrusts with `compute_thrusts()` for real-time motor control.

## Dependencies

> ``swarm` (base drone library)`
> ``numpy` (for thrust calculations)`
> ``pydrone` (optional`
> `if drone hardware is involved).`

## Related

- [[swarm-ai-base-drone]]
- [[motor-control-mixing-equations]]

>[!INFO] Priority Handling
> RC commands override high-level commands (e.g., `move_to`) when `command_mode == 'rc'`.

>[!WARNING] State Clipping
> Values exceed ±1.0 or 2.0 (speed) will be clamped to avoid motor saturation.
