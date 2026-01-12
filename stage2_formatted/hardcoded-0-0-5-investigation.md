**Tags:** #hardcoded, #drone-coordination, #simulation-config, #altitude-offset, #swarm-robotics
**Created:** 2026-01-12
**Type:** code-notes

# hardcoded-0-0-5-investigation

## Summary

```
Investigates hardcoded drone base position `(0, 0, 5)` across codebase, distinguishing between fixed values and configurable defaults.
```

## Details

> This investigation examines where the hardcoded position `(0, 0, 5)` is used in drone return-to-base logic. The analysis reveals four **inaccessible hardcoded** instances in drone return methods, where drones cannot dynamically adjust their base position. Conversely, two locations use `(0, 0, 5)` as a default but allow override via API or configurable methods. Additionally, two instances define altitude offsets (e.g., `5.0`) relative to a base position, ensuring flexibility in simulation setup.

## Key Functions

### ``_update_returning` (in `simulation/swarm/*_drone.py`)`

Drone logic for returning to a fixed base position.

### ``get_position()``

Retrieves drone’s current coordinates.

### ``set_base_position()` (line 702)`

Configurable method to update base position dynamically.

### ``takeoff` (in `mission_config.py`)`

Defines drone takeoff altitude offset relative to base.

## Usage

To modify drone base behavior:
1. **For hardcoded values**: Requires code edits in `_update_returning` methods.
2. **For configurable defaults**: Use `set_base_position()` or override `position` via API.
3. **For altitude offsets**: Adjust `base + np.array([0, 0, 5.0])` in `mission_config.py`.

## Dependencies

> ``numpy` (for array operations)`
> ``simulation/swarm/*_drone.py` (core drone logic)`
> ``simulation/hmrs_simulation_live.py` (simulation API).`

## Related

- [[mission_config]]
- [[ground_master]]
- [[hmrs_simulation_live]]

>[!INFO] Critical Hardcoding
> The four `_update_returning` methods in drone classes enforce a fixed base position `(0, 0, 5)`, breaking modularity. This violates the principle of dynamic configuration.

>[!WARNING] Altitude Offset Misinterpretation
> While `(0, 0, 5)` appears as an offset in `mission_config.py`, it is **relative** to a base position (e.g., `base + 5`). Misinterpreting it as an absolute value could lead to incorrect altitude calculations.
