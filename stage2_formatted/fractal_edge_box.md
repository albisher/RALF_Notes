**Tags:** #fractal-generation, #geometric-processing, #noise-algorithms, #procedural-terrain, #box-processing
**Created:** 2026-01-13
**Type:** code-library

# fractal_edge_box

## Summary

```
Generates fractal/noisy edges for procedural terrain boundaries like coastlines, craters, and asteroid edges.
```

## Details

> This module implements a **fractal edge generation** algorithm using **midpoint displacement**, a classic technique for creating natural-looking boundaries. It processes Voronoi cell edges by recursively subdividing segments and applying random perpendicular displacements based on a hash-derived seed. The algorithm supports deterministic generation via a world hash, allowing consistent fractal patterns across runs. It integrates with a box-processing framework (`Box`) to handle structured input/output, including world type validation and error handling.

## Key Functions

### ``FractalEdgeBox``

Main class wrapping the fractal edge generation logic, inheriting from `Box` for compatibility with the processing pipeline.

### ``execute()``

Core method that validates input, generates fractal edges per cell, and returns processed data with metadata.

### ``_subdivide_edge()``

Recursive helper that subdivides an edge into smaller segments, applies perpendicular noise, and reduces roughness with each subdivision.

## Usage

1. Initialize `FractalEdgeBox()` and call `execute()` with input data containing:
   - `operation="generate_fractal_edges"`
   - `world_hash` (for deterministic generation)
   - `world_type` (must be "planet", "moon", or "asteroid")
   - `cells` (Voronoi cell data with vertex IDs)
   - Optional: `roughness` (default: 0.5) and `subdivisions` (default: 3).
2. Output includes `fractal_vertices` (per-cell fractal edges) and `edge_data` (metadata like vertex counts).

## Dependencies

> `numpy`
> `hashlib`
> `boxes.core.box_interface`

## Related

- [[Procedural Terrain Generation]]
- [[Voronoi Cell Processing]]

>[!INFO] Deterministic Seeding
> Uses SHA-256 hashing of `world_hash` to generate a fixed seed for reproducible fractal patterns. The `seed` parameter in `_subdivide_edge()` further refines noise distribution per segment.

>[!WARNING] Edge Length Sensitivity
> Displacement magnitude scales with edge length (`displacement = roughness * length * 0.1`). Short edges may produce negligible noise; adjust `roughness` or `subdivisions` for stronger effects.
