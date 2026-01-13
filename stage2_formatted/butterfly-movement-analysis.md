**Tags:** #simulation, #drone, #movement-analysis, #waypoints, #butterfly-pattern, #debugging, #drone-control, #data-recording
**Created:** 2026-01-13
**Type:** research

# butterfly-movement-analysis

## Summary

```
Analyzes why a drone failed to execute a figure-8 (butterfly) flight pattern despite receiving waypoint commands.
```

## Details

> This document details a failed drone movement analysis where a simulated drone remained stationary despite receiving 50 waypoint commands for a butterfly flight pattern. The analysis reveals discrepancies between expected and actual movement metrics, including zero distance traveled, no positional updates, and a recording rate far below expected. The root causes include potential issues with drone command processing, simulation timing, motion history recording, and drone controller state.

## Key Functions

### ``update_visualization_data()``

Records drone position updates (should run at 240Hz but recorded only 4 points).

### ``receive_command()``

Likely responsible for processing waypoint commands (not confirmed active).

### `Motion history management`

Limits data to last 200 points, causing incomplete tracking.

## Usage

To reproduce this analysis:
1. Run a drone simulation with a figure-8 pattern.
2. Monitor `update_visualization_data()` for position updates.
3. Compare recorded data against expected metrics (e.g., 28,800 updates at 240Hz).
4. Investigate drone controller state and command queue.

## Dependencies

> `- Simulation engine (e.g.`
> `PX4`
> `ArduPilot`
> `or custom drone SDK)
- Drone controller library (e.g.`
> `MAVLink`
> `custom state machine)
- Position tracking system (e.g.`
> `ROS`
> `custom logging)`

## Related

- [[Drone-Simulation-Setup]]
- [[Waypoint-Command-Protocol]]
- [[Motion-Recording-Code]]

>[!INFO] Expected vs Actual Mismatch
> The discrepancy between expected 28,800 position updates (240Hz × 120s) and only 4 recorded updates suggests either:
> - The drone was not actively tracked during most of the simulation.
> - The motion history buffer was cleared prematurely.
> - The drone was not part of the spawned drones list during critical steps.


>[!WARNING] Drone Command Ignorance
> If `receive_command()` is not called or the drone controller is inactive, commands may be silently ignored. Verify:
> - Command queue depth.
> - Controller initialization (e.g., MAVLink connection).
> - Simulation loop timing (e.g., step rate vs. command processing).
