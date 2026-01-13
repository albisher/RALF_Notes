**Tags:** #python, #datetime, #error-fix, #module-import, #swarm-drone
**Created:** 2026-01-13
**Type:** code-fix

# datetime-import-fix

## Summary

```
Fixes missing `datetime` import causing `NameError` in drone simulation code.
```

## Details

> The code originally failed due to an undefined `datetime` module in `base_drone.py`, despite its usage in timestamp formatting. The root issue was an oversight in importing the module, which was resolved by adding `from datetime import datetime` to the imports section. The fix ensures ISO-formatted timestamps are generated correctly in methods like `get_state()` and `apply_thrust()`, maintaining compatibility with containerized environments.

## Key Functions

### `get_state()`

Generates and returns ISO-formatted timestamps for state messages.

### `apply_thrust()`

Uses `datetime.now()` for timestamping thrust-related operations.

### `All message timestamps`

All occurrences of timestamp generation rely on the `datetime` module.

## Usage

The fix requires updating `simulation/swarm/base_drone.py` to include the `datetime` import. After applying, restart the container or ensure the file is synced to reflect changes.

## Dependencies

> ``pybullet``
> ``numpy``
> ``typing``
> ``time``

## Related

- [[iso-timestamps-rc-translator-integration]]

>[!INFO] Container Sync
> If running in a container, ensure the updated file is synced to the container before execution to avoid runtime errors.

>[!WARNING] Restart Required
> After modifying the import, restart the container to load the updated `datetime` import.
