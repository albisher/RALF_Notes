**Tags:** #bugfix, #simulation, #drone, #api, #motion, #verification
**Created:** 2026-01-12
**Type:** documentation

# simulation-motion-verification

## Summary

```
Documentation outlining fixes for a motion simulation UI issue where drones were invisible and simulation did not run.
```

## Details

> This document records a bug fix for a simulation system where users reported no visible motion. The root causes included a non-running simulation thread, absence of spawned drones, and incorrect command formatting. Fixes involved starting the simulation via an API endpoint, spawning a drone at a visible position, and correcting the JSON command structure. The fix ensures the simulation runs, drones are visible, and motion commands execute properly.

## Key Functions

### ``/api/start``

Initiates the simulation thread.

### ``/api/spawn``

Creates a drone object at a specified location.

### ``/api/command``

Sends movement instructions to drones.

### ``POST /api/health``

Checks simulation operational status.

## Usage

1. Call `/api/start` to begin simulation.
2. Use `/api/spawn` to deploy a drone (e.g., `VisibleDrone` at (0, 0, 0)).
3. Send commands via `/api/command` with the corrected format:
   ```json
   {"drone_name": "VisibleDrone", "command_type": "move_to", "target": [10, 10, 10]}
   ```
4. Verify UI updates: Check `Sim Time` progression, drone visibility, and motion history.

## Dependencies

> `- WebSocket (for real-time updates`
> `if applicable)
- JSON-based API communication layer`

## Related

- [[drone-movement-rc-tracking-implementation]]
- [[session-clear-and-create-summary]]

>[!INFO] Important Note
> Ensure the WebSocket connection is active if real-time updates are expected. Monitor the browser console for errors during API calls.


>[!WARNING] Caution
> Incorrect command formatting (e.g., `"command": { ... }`) will result in silent failures. Always validate API responses for `running: true` and drone visibility.
