**Tags:** #noise-generation, #procedural-generation, #simplex-noise, #hash-based-algorithm, #terrain-generation
**Created:** 2026-01-13
**Type:** code-library

# simplex_noise_box

## Summary

```
Generates Simplex noise (an improved Perlin noise variant) for procedural world generation, optimized for smoother gradients and reduced directional artifacts.
```

## Details

> This code implements a **Simplex noise box**, a procedural generation module that leverages a hash-based approach to create deterministic, high-quality noise patterns. It supports multiple world types (e.g., planets, galaxies) and allows customization via parameters like scale, octaves, and seed offsets. The core logic uses a triangular grid interpolation method to approximate Simplex noise, improving upon Perlin noise by reducing directional artifacts and enhancing smoothness. The `_generate_simplex_like_noise` method constructs gradient vectors from SHA-256 hashes of cell coordinates, then applies smooth interpolation to compute noise values across a 2D grid.

## Key Functions

### ``SimplexNoiseBox``

Base class defining noise generation capabilities, with support for specific world types.

### ``execute``

Main method that validates input, computes noise, and returns results as a structured `BoxOutput`.

### ``_generate_simplex_like_noise``

Core algorithm that:

## Usage

1. Initialize `SimplexNoiseBox` and call `execute` with a `BoxInput` containing:
   - `operation="generate_noise"` (required).
   - Required fields: `world_hash`, `width`, `height`.
   - Optional fields: `scale`, `octaves`, `seed_offset`.
2. The output includes a 2D noise array (0–1 range) and metadata (e.g., min/max values).

## Dependencies

> `numpy`
> `hashlib`
> `boxes.core.box_interface`

## Related

- [[SimplexNoiseAlgorithms]]
- [[PerlinNoiseComparison]]
- [[ProceduralWorldGeneration]]

>[!INFO] **Deterministic Hashing**
> The `base_hash` and `seed_offset` combine to ensure reproducibility across runs. SHA-256 ensures consistent gradient directions for identical inputs.

>[!WARNING] **Edge Cases in Grid Scaling**
> If `scale` or `octaves` are too small, `grid_size_x/y` may underflow, leading to missing gradients. Always validate `width/height` against `octave_scale` to avoid silent failures.
