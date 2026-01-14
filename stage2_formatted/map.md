**Tags:** #interactive-map, #geospatial-data, #javascript, #svg-visualization, #coordinate-system
**Created:** 2026-01-13
**Type:** code-notes

# map

## Summary

```
Manages a dynamic SVG-based map visualization with zoom, grid labeling, and coordinate reference systems.
```

## Details

> This file (`map.js`) defines a JavaScript module for rendering and interacting with a map displayed via SVG. It initializes global variables for map data (cells, vertices, and biome data), SVG dimensions, and zoom controls. The code fetches processed map data from `processed_map.json`, validates it, and processes it into `mapCellsData` and `mapVerticesData`. It includes utility functions for formatting grid labels (e.g., converting internal coordinates to longitude/latitude-like strings) and converting between slider-based zoom inputs and logarithmic zoom factors. The map layer and grid layer are dynamically updated based on user interactions (e.g., zoom slider adjustments).

## Key Functions

### `formatXLabel(value)`

Converts an internal X-coordinate to a formatted string (e.g., "123E" or "0° (PM)").

### `formatYLabel(value)`

Converts an internal Y-coordinate to a formatted string (e.g., "45N" or "0° (Eq)").

### `sliderValueToActualZoom(sVal)`

Maps a slider value (0–100) to an exponential zoom factor (1.0–4500.0).

### `actualZoomToSliderValue(aZoom)`

Maps an actual zoom factor back to a slider value (0–100).

### `displayMessage(msg, isErr)`

Updates a message area with error/success feedback.

### `Fetch and process `processed_map.json``

Loads and validates map data (cells, vertices, biomes) for rendering.

## Usage

1. Load the script after the SVG container (`<svg id="map">`) and DOM elements (`<div id="map-layer">`, etc.) are rendered.
2. Call `fetch('processed_map.json')` to load map data. The script validates and processes it internally.
3. Interact with the map via:
   - **Zoom slider**: Adjusts `currentViewBox` and updates the SVG view.
   - **Grid labels**: Dynamically formatted using `formatXLabel`/`formatYLabel`.
   - **Error handling**: Displays messages via `displayMessage`.

## Dependencies

> ``processed_map.json``
> `DOM elements (`#map``
> ``#map-layer``
> ``#grid-layer``
> `etc.)`
> `SVG libraries (implicitly via browser SVG support).`

## Related

- [[map-rendering]]
- [[coordinate-system-conversion]]
- [[interactive-ui-controls]]

>[!INFO] Global Coordinate References
> The script relies on `internalXForLon0` and `internalYForLat0` to map internal coordinates to geographic directions (e.g., "E/W" for longitude, "N/S" for latitude). These must be set externally (e.g., via `mapInfoWidthForGlobalRef`/`mapInfoHeightForGlobalRef`) for proper labeling.

>[!WARNING] Zoom Limits
> The logarithmic zoom scale (`ACTUAL_ZOOM_MIN=1.0`, `ACTUAL_ZOOM_MAX=4500.0`) may cause distortion at extreme values. Ensure `processed_map.json` data scales appropriately for the intended zoom range.
