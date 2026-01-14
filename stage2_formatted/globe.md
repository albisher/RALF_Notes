**Tags:** #Three.js, #WebGL, #Geospatial Visualization, #Map Data Processing, #Biome Rendering, #Real-time Interactivity
**Created:** 2026-01-13
**Type:** code-notes

# globe

## Summary

```
Visualizes a globe using Three.js with dynamic height scaling and biome-based terrain rendering from external map data.
```

## Details

> This code initializes a Three.js globe visualization where geographic polygons are extruded into 3D terrain based on height values from a processed map file (`processed_map.json`). The globe includes interactive orbit controls, adjustable height scaling, and supports multiple display modes (e.g., combined terrain/biome rendering). Ocean/water biomes are forced to remain at or below sea level, while other biomes use color-coded terrain extrusion. The map data is stretched to cover the full 360° longitude span to eliminate gaps, with a base ocean sphere acting as a fallback.

## Key Functions

### ``init()``

Sets up the Three.js scene, camera, renderer, lights, and event listeners for dynamic controls (e.g., height scale, display mode).

### ``loadMapData()``

Fetches and parses `processed_map.json` containing polygonized map data, vertices, and biome attributes.

### ``createGlobe()``

Constructs the 3D globe by:

### ``updateGlobe()`** (implicitly called via event listeners)`

Re-renders the globe when height scale or display mode changes.

## Usage

1. Load the script into an HTML file with a container (`<div id="container">`) and input controls for `heightScale` and `displayMode`.
2. Ensure `processed_map.json` is accessible at the same origin or preloaded.
3. Render the globe by calling `init()` (typically via `<script src="globe.js"></script>`).

## Dependencies

> `THREE.js`
> ``processed_map.json` (external JSON file with map data)`
> ``OrbitControls` (Three.js addon for interactive camera controls).`

## Related

- [[Three]]
- [[OrbitControls Usage Guide]]
- [[Map Data Schema for `processed_map]]

>[!INFO] Dynamic Height Scaling
> The `heightScale` slider adjusts the extrusion height of terrain features proportionally to the base globe radius (1). Values >1 amplify elevation, while <1 compresses it.

>[!WARNING] Water Biome Handling
> Water biomes (e.g., "Ocean") are explicitly capped at `heightValue = 1` to prevent over-extrusion. If `cell.t` (height) exceeds this, it will be clipped to 1.

>[!INFO] Stretched Map Projection
> The longitude span (`lonSpan`) is forced to 360° via `stretchFactor`, which may distort small-scale maps. For precise geographic accuracy, adjust `lonSpan` dynamically or preprocess the data.
