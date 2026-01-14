**Tags:** #map-optimization, #box-component, #coordinate-centering, #spatial-visualization
**Created:** 2026-01-13
**Type:** code-notes

# map_view_optimization_box

## Summary

```
Optimizes map viewer settings to center coordinates and reduce empty space by calculating zoom and offset dynamically.
```

## Details

> This module extends a `Box` class to compute optimal map view parameters (scale, offset, viewBox) based on input map data, viewer dimensions, and optional parameters like `centerOnZero` and `padding`. It dynamically determines map bounds from vertices or derived metadata, ensuring the (0,0) coordinate is centered while trimming excess whitespace. The algorithm supports multiple world types (e.g., planets, galaxies) by falling back to metadata if vertex data is unavailable.

## Key Functions

### ``constructor()``

Initializes the `MapViewOptimizationBox` with metadata (version, dependencies, input schema).

### ``_executeInternal(inputData)``

Validates input and delegates to `_calculateOptimalView`; returns success/error via `BoxOutput`.

### ``_calculateOptimalView(mapData, viewerWidth, viewerHeight, centerOnZero, padding)``

Core logic:

## Usage

1. Pass `mapData` (containing `pack.cells`, `vertices`, `derivedInfo`), `viewerWidth`, `viewerHeight`, and optional `centerOnZero`/`padding`.
2. The box returns a `BoxOutput` with optimized `viewBox` and `center` for rendering.
3. Example:
   ```js
   const result = await mapViewBox.optimize({ mapData, viewerWidth: 800, viewerHeight: 600 });
   ```

## Dependencies

> ``../core/box_interface.js` (Box framework for input/output handling)`
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`.`

## Related

- [[Space Pearl Map Framework]]
- [[Coordinate System Standardization]]

>[!INFO] Edge-Case Handling
> If `vertices` are missing, the code defaults to `mapNativeWidth`/`height` or `info.width`/`height`, ensuring compatibility across world types (e.g., galaxies with sparse vertex data).

>[!WARNING] Zero-Padding Risk
> Setting `padding=0` may expose raw map edges; ensure `viewerWidth/Height` accommodate the result.
