**Tags:** #drone-movement, #mission-priority, #command-execution, #autonomous-behavior
**Created:** 2026-01-13
**Type:** code-notes

# 0018-movement-fixes-applied

## Summary

```
Fixes drone movement logic to prioritize command execution over autonomous mission updates.
```

## Details

> This file addresses issues where scout drones' mission-specific behaviors (e.g., mapping) interfered with command-based movement. Key changes include:
> - Ensuring command execution runs first via `super().update(dt)` before mission-specific logic.
> - Conditionally executing mission updates only when `command_mode is None` to prevent conflicts.
> - Maintaining command priority by deferring autonomous behavior until after command processing.

## Key Functions

### ``update(self, dt`

float)`**: Modified to prioritize command execution via `super().update(dt)` before mission-specific logic.

### ``_update_mapping(dt)``

Only called when `command_mode is None` to avoid interference.

## Usage

To test, spawn drones and send `move_to` commands. Verify drones execute commands immediately and transition mission states (e.g., `mapping`) correctly.

## Dependencies

> ``simulation/swarm/base_drone``
> ``simulation/swarm` (shared drone logic and state management).`

## Related

- [[base_drone]]
- [[0018-movement-fixes-applied#Code-Changes]]

>[!INFO] Priority Logic
> Command execution now runs first in `update()`, ensuring commands override autonomous behavior.

>[!WARNING] State Transition
> Ensure `mission_state` is initialized (e.g., `idle`) before sending `move_to` commands to avoid unexpected behavior.
