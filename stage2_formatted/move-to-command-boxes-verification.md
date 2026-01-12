**Tags:** #verification, #priority-order, #fallback-logic, #motion-pattern, #rc-translator, #ml-controller, #drone-control, #code-update
**Created:** 2026-01-12
**Type:** code-notes

# move-to-command-boxes-verification

## Summary

```
Code update ensures drone command execution prioritizes existing motion and control boxes with fallback mechanisms.
```

## Details

> This document outlines the verification of a `move_to` command implementation for drones, ensuring it uses priority-based existing control boxes (Motion Pattern, RC Translator, ML Controller). The update enforces a structured fallback sequence: Motion Pattern (Priority 1) is checked first, followed by RC Translator (Priority 2) if Motion fails, and ML Controller (Priority 3) as a last resort. Key changes include adding a `motion_pattern_succeeded` flag, debug logging, and robust error handling. The verification confirms successful initialization of all boxes and proper fallback logic, with next steps focusing on backend monitoring and force validation.

## Key Functions

### ``motion_pattern.compute_control()``

Computes control forces for motion patterns.

### ``motion_pattern.apply_forces()``

Applies computed forces to drones.

### ``rc_translator.set_rc_state()``

Configures RC state for fallback control.

### ``rc_translator.compute_thrusts()``

Calculates thrust values from RC inputs.

### ``ml_controller_box.compute_control()``

Fallback ML-based control logic.

### ``BaseDrone.__init__()``

Initializes drone control boxes (RC Translator included).

### ``apply_thrust()``

Applies computed thrust to drone motors.

## Usage

1. **Initialize Drone**: Ensure `BaseDrone` and its child classes (e.g., `QuadcopterMotion`) are instantiated with required boxes.
2. **Execute `move_to` Command**: The system automatically prioritizes Motion Pattern, then RC Translator, then ML Controller if needed.
3. **Monitor Logs**: Check debug logs (every 240 frames) for active box status and errors.
4. **Validate Forces**: Adjust gains/throttle if forces are insufficient for desired motion.

## Dependencies

> ``motion_patterns/``
> ``boxes/rc_command_translator_box.py``
> ``ml_controller_box``
> ``base_drone.py``
> `external drone control libraries (e.g.`
> `PX4/ArduPilot).`

## Related

- [[Drone Control Architecture]]
- [[Motion Pattern Implementation]]
- [[RC Command Translator Docs]]

>[!INFO] Important Note
> Motion Pattern Box is prioritized first due to its direct integration with scout drones (e.g., QuadcopterMotion). If unavailable, the system defaults to RC Translator, which requires manual initialization in `BaseDrone.__init__()`.


>[!WARNING] Caution
> ML Controller (Priority 3) may not be initialized by default. Ensure it is loaded before relying on it as a fallback. Debug logs will indicate its activation status.
