**Tags:** #data-processing, #map-visualization, #coordinate-transformation, #worldmap-compatibility
**Created:** 2026-01-13
**Type:** code-module

# map_process_box

## Summary

```
Converts raw map data into a standardized format for the WorldMap2D viewer by computing derived metadata like origin coordinates and dimensions.
```

## Details

> This module extends a generic `Box` class to handle map data preprocessing. It validates input, computes spatial metadata (e.g., bounding box, native dimensions), and ensures compatibility with WorldMap2D’s expected structure. The core logic involves:
> 1. Extracting vertices from the map’s `pack` structure to derive geometric properties.
> 2. Calculating derived metadata (e.g., `mapOriginX/Y`, `mapNativeWidth/Height`) from vertex coordinates or fallback to map metadata.
> 3. Adding derived metadata to the output while preserving the original map data for reference.
> 
> The module supports error handling for missing fields (e.g., `mapData`) or invalid inputs (e.g., empty vertices). It also computes internal coordinate systems for global lines (Prime Meridian/Equator) using provided map bounds and dimensions.

## Key Functions

### ``_executeInternal``

Orchestrates the processing pipeline, validates input, and returns either a success/error response.

### ``_processMapData``

Copies input data, validates its structure, and adds derived metadata (e.g., `derivedInfo`).

### ``_calculateDerivedInfo``

Computes spatial properties (min/max coordinates, dimensions) from vertices or fallback values.

### ``_calculateGlobalLines``

Derives internal coordinates for global reference lines (e.g., `internalXForLon0`, `internalYForLat0`).

## Usage

1. Instantiate `MapProcessBox` and pass input data (e.g., `mapData`).
2. Call `_executeInternal` to trigger processing. The output includes:
   - `processedMap`: Modified data with derived metadata.
   - `originalMap`: Unaltered input for reference.
3. Handle errors (e.g., missing `mapData` or invalid vertices) via `BoxOutput.error`.

## Dependencies

> ``../core/box_interface.js` (Box class and utilities like `BoxOutput``
> ``BoxErrorCode`).`

## Related

- [[WorldMap2D documentation]]
- [[MapRenderBox]]
- [[Box core utilities]]

>[!INFO] Derived Metadata Priority
> If vertices are missing or invalid, the module falls back to map metadata (`info.width`, `info.height`) for dimensions, ensuring robustness.

>[!WARNING] Data Integrity
> Directly modifying `processed.pack.biomes` (e.g., converting dict → list) is handled internally but may require additional validation in downstream components. Ensure compatibility with MapRenderBox’s expectations.
