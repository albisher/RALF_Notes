**Tags:** #hillshading, #3D-visualization, #geospatial, #box-processing, #vector-analysis
**Created:** 2026-01-13
**Type:** code-notes

# hillshading_box

## Summary

```
Generates simulated 3D lighting effects (hillshading) for terrain visualization using height data and light direction.
```

## Details

> This module implements a hillshading algorithm within a `Box` class framework, designed to compute shadow and highlight intensities based on terrain elevation differences. It processes Voronoi cells, calculates gradients from neighboring cells, and applies lighting based on configurable light angles and elevation. The algorithm handles edge cases (e.g., missing neighbors) by defaulting to neutral shading (0.5). The `_build_neighbor_map` method constructs adjacency relationships between cells to derive surface normals.

## Key Functions

### `HillshadingBox`

Core class encapsulating hillshading logic, including initialization, validation, and execution.

### `execute`

Main method that validates input, computes lighting direction, and applies hillshading per cell.

### `_build_neighbor_map`

Private helper to map cell IDs to their neighbors for gradient calculation.

## Usage

1. Instantiate `HillshadingBox()`.
2. Call `execute()` with a `BoxInput` containing:
   - `operation="calculate_hillshade"`
   - `world_type` (e.g., "planet")
   - `cells`: List of cell coordinates (e.g., `[{"i": 1, "p": (x, y)}]`).
   - `heights`: Dictionary mapping cell IDs to elevation values.
   - Optional: `light_angle` (default: 315°) and `light_elevation` (default: 45°).
3. Retrieve results via `BoxOutput` containing `hillshade` (0–1 range) and `light_direction`.

## Dependencies

> `numpy`
> `boxes.core.box_interface`

## Related

- [[None]]

>[!INFO] Light Direction Handling
> Light direction is derived from `light_angle` and `light_elevation` using spherical coordinates, converting to Cartesian vectors for dot-product illumination calculation. Default values (315° azimuth, 45° elevation) simulate top-left lighting.


>[!WARNING] Edge Cases
> Missing neighbors or invalid heights default to neutral shading (0.5). Exceptions in execution propagate as errors in `BoxOutput.error`.
