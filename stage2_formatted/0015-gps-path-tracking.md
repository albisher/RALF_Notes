**Tags:** #gps-tracking, #drone-autonomy, #rtk-integration, #coordinate-systems, #sensor-data
**Created:** 2026-01-13
**Type:** code-notes

# 0015-gps-path-tracking

## Summary

```
Tracks 3D drone paths using dual GPS coordinate systems (absolute/relative) and physics data for redundancy.
```

## Details

> This implementation extends a drone simulation system to log GPS-derived positions alongside physics-based motion. It maintains a hybrid tracking approach where GPS absolute coordinates (from RTK addons) and relative positions (GPS minus base station) are stored alongside physics simulation data. The system automatically falls back to physics data when GPS addons are unavailable, ensuring continuous tracking. Key components include motion history entries with metadata (fix quality, satellite counts) and sensor readings that preserve backward compatibility while adding new GPS-specific fields.

## Key Functions

### ``update_visualization_data()``

Updates visualization with GPS tracking data.

### ``_collect_sensor_readings()``

Retrieves GPS data from addons and constructs sensor readings.

### `GPS relative coordinate calculation`

Subtracts base position from GPS absolute coordinates.

### ``verify_time_based_data.py``

Displays GPS path visualization and metadata.

## Usage

1. Initialize drone with base position (default [0, 0, 0]).
2. Attach GPS RTK addon to drone.
3. System automatically:
   - Detects GPS addon.
   - Logs GPS absolute/relative coordinates in motion history.
   - Includes GPS metadata in sensor readings.
4. Fallback to physics data if GPS fails.

## Dependencies

> ``hmrs_simulation_live.py``
> ``verify_time_based_data.py``
> `GPS/RTK addon (CUAV C-RTK 9Ps or similar)`
> `drone autonomy framework.`

## Related

- [[`0014-drone-autonomy-framework`]]
- [[`0016-sensor-data-aggregation`]]

>[!INFO] Dual Coordinate Fallback
> GPS tracking prioritizes RTK fix quality (fix_quality ≥ 4) for accuracy. If GPS fails, physics position (relative to base) is used, preserving continuity.

>[!WARNING] Base Position Sensitivity
> Incorrect base position initialization (e.g., [0, 0, 0] misaligned) invalidates GPS relative coordinates. Verify base station coordinates match real-world deployment.
