**Tags:** #drone-movement, #configurable-positions, #hardcoded-verification, #altitude-offset, #base-position
**Created:** 2026-01-12
**Type:** test-reference

# movement-test-hardcoded-verification

## Summary

```
Verifies drone movement system avoids hardcoded positions by using configurable base coordinates.
```

## Details

> This document confirms that a drone movement system does not rely on hardcoded base positions like `(0, 0, 5)` but instead uses a configurable `base_position` attribute. The system dynamically adjusts drone altitude by adding a fixed offset of `[0, 0, 5]` to the stored base coordinates, ensuring flexibility and avoiding hardcoded values. The test verifies that all drone classes (`BaseDrone`, `HMRSScoutDrone`, etc.) adhere to this design, with configurable base positions tracked via timestamps.

## Key Functions

### ``get_base_position()``

Returns configurable base position plus a fixed altitude offset `[0, 0, 5]`.

### ``update_base_position()``

Updates the drone’s base position with timestamp tracking.

### ``base_position_history``

Logs all changes to the base position.

### ``_update_returning()`** (in `HMRSScoutDrone`)`

Uses `get_base_position()` for return-to-base operations.

## Usage

1. Configure drone base position via `base_position` attribute.
2. Use `get_base_position()` to retrieve the base position with a 5m altitude offset.
3. Implement return-to-base logic by calling `get_base_position()` in methods like `_update_returning()`.

## Dependencies

> ``numpy` (for array operations)`
> `drone-specific classes (`BaseDrone``
> ``hmrs_scout_drone.py``
> `etc.).`

## Related

- [[movement-system-design]]
- [[drone-configuration-guidelines]]

>[!INFO] Altitude Offset Clarification
> The `[0, 0, 5]` offset in `get_base_position()` is intentional and represents a fixed altitude (5 meters) above the base position, not a hardcoded spatial coordinate. The actual base position is fully configurable via `base_position`.


>[!WARNING] Configurable Base Dependency
> If `base_position` is not set before initialization, the drone may fail to return to a valid base position. Ensure proper initialization in drone classes.
