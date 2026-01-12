**Tags:** #coordinate-systems, #gps-localization, #drone-simulation, #data-separation, #api-endpoints
**Created:** 2026-01-12
**Type:** documentation

# position-vs-gps-location-analysis

## Summary

```
Analyzes the distinction between local position (drone coordinates) and Earth-based GPS coordinates in HMRS simulation to prevent incorrect data mixing.
```

## Details

> This document defines and validates the separation between **local Cartesian position** (meters from a base reference at `[0, 0, 0]`) and **geographic GPS coordinates** (latitude/longitude in decimal degrees). It ensures the simulation system correctly distinguishes these coordinates to avoid conflicts in physics, weather integration, and API endpoints. The analysis highlights a critical bug where an API endpoint incorrectly returned local position values as GPS coordinates and vice versa, requiring a fix to enforce strict separation via `base_position` (numpy array) and `base_latitude/longitude` (floats).

## Key Functions

### ``set_base_position(position)``

Updates local Cartesian coordinates (meters) relative to the base.

### ``set_base_gps(latitude, longitude)``

Updates Earth-based GPS coordinates (decimal degrees).

### ``GPSTracker``

Uses `base_position` for relative position calculations (not GPS coordinates).

### ``Master Controls API Endpoint``

Previously incorrectly exposed local position as GPS data (now fixed).

## Usage

1. **Local Position**: Use `set_base_position()` for drone movement in simulation physics.
2. **GPS Coordinates**: Use `set_base_gps()` for real-world location services (e.g., weather, OSM maps).
3. **API Endpoints**: Ensure endpoints return `base_latitude`/`base_longitude` (GPS) and do not mix with local coordinates.

## Dependencies

> ``numpy``
> ``hmrs_simulation_live.py` (core simulation module)`
> ``GPSTracker` class (for relative position calculations).`

## Related

- [[hmrs_simulation_live]]
- [[GPS_Tracker_Implementation]]
- [[Coordinate_System_Design_Decision]]

>[!INFO] Critical Fix Applied
> The bug in `Master Controls API` was resolved by replacing incorrect local position values with GPS coordinates (`base_latitude`/`base_longitude`) in both GET and POST endpoints. This prevents data corruption when integrating GPS-based services.


>[!WARNING] Data Separation Risk
> If `base_position` and GPS coordinates are not strictly separated, relative position calculations (e.g., in `GPSTracker`) may yield incorrect results. Always validate coordinate updates via `set_base_position` and `set_base_gps` separately.
