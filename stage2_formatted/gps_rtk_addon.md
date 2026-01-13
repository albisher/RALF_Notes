**Tags:** #gps, #rtk, #cuav, #drones, #realistic_simulation, #positioning, #satellite, #addon, #numerical_simulation, #drone_autonomy
**Created:** 2026-01-13
**Type:** code-notes

# gps_rtk_addon

## Summary

```
Simulates GPS/RTK positioning data for CUAV C-RTK 9Ps with configurable RTK and dual-GPS modes.
```

## Details

> This addon class (`GPSRTKAddon`) inherits from `BaseAddon` and simulates realistic GPS/RTK data generation based on CUAV’s C-RTK 9Ps specifications. It models RTK accuracy (0.01m + 1ppm CEP), update rates (20Hz RTK, 25Hz RAW/PVT), and supports multiple constellations (GPS, BeiDou, Galileo, GLONASS). Key state variables include satellite visibility, HDOP/VDOP/PDOP metrics, and position/velocity/heading tracking. The class initializes with optional RTK/dual-GPS modes and base station positioning, enforcing CUAV’s hardware specs (e.g., 30g weight, 0.5W power).

## Key Functions

### ``__init__``

Initializes the addon with RTK/dual-GPS settings, state variables, and CUAV-specific attributes (e.g., dimensions, power).

### ``on_a``

*(Incomplete; likely part of an event handler for simulation loops, e.g., `on_addon_activate` or `on_update`.)*

### ``variables``

Stores runtime metadata (e.g., `update_rate_hz`, `accuracy_m`) for dynamic adjustments.

## Usage

1. Instantiate `GPSRTKAddon` with `rtk_enabled=True/False` and `dual_gps=False/True`.
2. Set `base_station_position` (optional) to define RTK correction origin.
3. Simulate updates via event hooks (e.g., `on_a` would trigger periodic state updates).
4. Access simulated data via attributes like `last_position`, `heading`, or `rtk_fix_quality`.

## Dependencies

> `numpy`
> `typing`
> `time`
> `random`
> ``.base_addon` (local module)`

## Related

- [[CUAV_C_RTK_9Ps_Docs]]
- [[GPS_Simulation_Protocols]]

>[!INFO] RTK Accuracy Formula
> Accuracy = `0.01m + (1ppm * current_position_m)`, where `1ppm = 0.000001`. This ensures sub-centimeter precision under ideal conditions.

>[!WARNING] State Initialization
> `rtk_survey_in_complete` and `rtk_survey_in_time` must be managed externally to simulate RTK survey phases. Defaults to `False`/`0.0` for simplicity.
