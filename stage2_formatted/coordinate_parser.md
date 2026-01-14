**Tags:** #geospatial, #coordinate-transformation, #cartesian-conversion, #re-regular-expression, #input-validation
**Created:** 2026-01-13
**Type:** code-library

# coordinate_parser

## Summary

```
Converts geographic coordinates (latitude/longitude) into Cartesian coordinates using Earth’s radius, with support for decimal or cardinal direction formats.
```

## Details

> This script parses user input strings containing latitude/longitude and zoom values in either decimal or cardinal direction (N/S/E/W) format. It validates inputs, converts them into a structured dictionary, and computes Cartesian coordinates (x, y, z) using Earth’s average radius. The `calculate_cartesian()` function transforms geographic coordinates (φ, λ) into spherical Cartesian coordinates (x, y, z) via trigonometric calculations. Input validation ensures latitude is between -90° to 90°, longitude between -180° to 180°, and zoom is non-negative.

## Key Functions

### `parse_input(input_str)`

Parses input strings into latitude, longitude, and zoom values using regex, supporting both decimal and cardinal formats.

### `calculate_cartesian(latitude_deg, longitude_deg, radius_km)`

Converts geographic coordinates to Cartesian coordinates using Earth’s radius and trigonometric functions.

### ``EARTH_RADIUS_KM``

Imports Earth’s average radius from `coordinate.py` for use in Cartesian calculations.

## Usage

1. Run the script and input a string like:
   - `'c=40.7128,-74.0060 z=10'` (decimal format)
   - `'c=N40.7128,W74.0060 z=10'` (cardinal format).
2. The script outputs parsed values and Cartesian coordinates (x, y, z) derived from Earth’s radius.

## Dependencies

> ``re``
> ``math``
> ``coordinate` (custom module containing `EARTH_RADIUS_KM`).`

## Related

- [[`coordinate]]
- [[`geospatial-transformations`]]

>[!INFO] Input Validation
> The script validates ranges for latitude (-90° to 90°), longitude (-180° to 180°), and zoom (must be ≥ 0). Invalid inputs return `None` with an error message.

>[!WARNING] Cardinal Direction Parsing
> Cardinal directions (N/S/E/W) are case-insensitive but must be explicitly included (e.g., `'c=N40.7128,W74.0060'`). Missing cardinals will fail validation.
