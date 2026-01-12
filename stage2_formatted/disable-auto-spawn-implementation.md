**Tags:** #simulation, #drone-spawning, #api-integration, #user-control, #programmatic-config
**Created:** 2026-01-12
**Type:** code-notes

# disable-auto-spawn-implementation

## Summary

```
Modifies drone spawning behavior to disable automatic drone spawning, enforcing manual or API-driven spawning.
```

## Details

> This implementation disables the default auto-spawn feature in `simulation/hmrs_simulation_live.py`, ensuring drones only spawn via explicit user interaction (UI button) or API calls (`/api/spawn`). The change replaces automatic spawning with conditional logic, requiring programmatic override (`auto_spawn_drones = True`) for testing scripts. Saved configurations remain non-spawnable templates, while the `auto_spawn_delay` and `auto_spawn_count` variables are now inactive by default.

## Key Functions

### ``self.auto_spawn_drones``

Boolean flag controlling auto-spawn logic (now `False`).

### ``/api/spawn` (POST)`

Endpoint for manual drone spawning via API.

### `Spawn Modal UI`

UI component for user-triggered drone selection.

### ``self.programmatic_mode``

Enables/disables simulation automation (used for testing).

## Usage

1. **Manual Spawn**: Click UI button to open modal and select drones.
2. **API Spawn**: Call `POST /api/spawn` with drone type/position data.
3. **Programmatic Spawn**: Set `auto_spawn_drones = True` in code (e.g., for testing).

## Dependencies

> ``simulation/hmrs_simulation_live.py``
> ``drone_configurations.json``
> ``/api/spawn` endpoint.`

## Related

- [[hmrs_simulation_live]]
- [[`drone_configurations]]
- [[spawn` documentation]]

>[!INFO] **Verification Check**
> Ensure `/api/state` returns empty `"drones": []` after 5+ seconds without manual intervention.

>[!WARNING] **Config Preservation**
> Saved configurations in `drone_configurations.json` are **templates only**—do not auto-spawn drones from them.
