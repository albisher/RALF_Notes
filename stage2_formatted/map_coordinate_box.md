**Tags:** #geospatial, #coordinate-projection, #map-visualization, #box-pattern, #parallel-processing
**Created:** 2026-01-13
**Type:** code-notes

# map_coordinate_box

## Summary

```
Handles map coordinate transformations and projections for spatial data processing.
```

## Details

> This module implements a `MapCoordinateBox` class extending a generic `Box` component, providing core functionality for converting between geographic coordinates (latitude/longitude) and screen/map coordinates. It supports five operations: projecting lat/lon to screen space, converting lat/lon to map coordinates, normalizing coordinates, and bidirectional conversions between screen and geographic spaces. The class uses a modular approach with private helper methods for each operation, validating inputs and applying simple linear transformations based on configurable parameters like map dimensions, scale, and offsets.

## Key Functions

### ``_executeInternal(inputData)``

Orchestrates the execution of the selected operation (project, convert, normalize, etc.) based on input parameters.

### ``_projectCoordinates(params)``

Converts lat/lon to screen coordinates using a linear projection formula.

### ``_convertLatLonToMap(params)``

Converts lat/lon to map coordinates with configurable map dimensions and scaling.

### ``_normalizeCoordinates(params)``

Scales coordinates to a 0-100 range (placeholder for future expansion).

### ``_screenToLatLon(params)``

Maps screen coordinates back to lat/lon (simplified placeholder).

### ``_latLonToScreen(params)``

Maps lat/lon to screen coordinates using screen dimensions (simplified placeholder).

## Usage

1. Initialize `MapCoordinateBox` and pass required parameters (e.g., map dimensions, scale).
2. Call `_executeInternal` with an operation (e.g., `operation: 'project'`) and coordinates.
3. Handle the returned `BoxOutput` (success/error) containing transformed coordinates.

## Dependencies

> ``../core/box_interface.js` (Box class and utilities)`
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory``

## Related

- [[Space Peral Core Architecture]]
- [[Box Pattern Implementation Guide]]

>[!INFO] Input Validation
> All operations validate input parameters (e.g., checks for valid lat/lon values, array length for projections). Missing or invalid data triggers errors.

>[!WARNING] Simplified Projections
> Current implementations use basic linear transformations. For accurate geospatial projections, consider integrating libraries like `proj4js` or `mercator` for proper Earth-centric calculations.
