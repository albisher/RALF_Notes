**Tags:** # procedural-generation, # noise-based-algorithms, # terrain-modelling, # hash-based-determinism, # numpy-array-operations
**Created:** 2026-01-13
**Type:** code-library

# terrain_formation

## Summary

```
Generates procedural continental landmasses and mountain ranges using Perlin/Simplex noise and hash-based randomization.
```

## Details

> This module implements terrain generation algorithms for creating natural-looking continents and mountain ranges. It uses deterministic noise generation (via Perlin/Simplex) seeded by input hashes to produce consistent yet varied terrain patterns. The `generate_continents_fast` function creates continent shapes by combining Gaussian distributions (for continent cores) with Perlin noise (for coastlines), while `generate_mountains_fast` produces linear mountain ranges using hash-derived parameters. The system supports fast computation with configurable noise octaves and scales.

## Key Functions

### `generate_continents_fast`

Creates continent landmasses with natural coastlines using multiple noise layers and Gaussian distributions.

### `generate_perlin_terrain_fast`

Implements a fast Perlin-like noise generator (with optional Simplex fallback) for procedural terrain.

### `generate_mountains_fast`

Produces mountain ranges via hash-derived ridge parameters and linear interpolation.

## Usage

1. Call `generate_continents_fast(base_hash, width, height)` to create continent maps.
2. Call `generate_perlin_terrain_fast(base_hash, width, height, scale=50.0, octaves=4)` for base terrain noise.
3. Call `generate_mountains_fast(base_hash, width, height)` to generate mountain ranges.

## Dependencies

> `numpy`
> `hashlib`
> `backend/boxes (Simplex noise implementation)`
> `sys`
> `os`

## Related

- [[TERRAIN_FORMATION_RESEARCH]]
- [[boxes (if applicable)]]

>[!INFO] Noise Fallback
> If Simplex noise is unavailable, the code falls back to a Perlin-like implementation, which may produce slightly different results but maintains procedural consistency.

>[!WARNING] Hash Dependency
> The generated terrain is deterministic based on the input hash. Changing the hash produces entirely new terrain patterns, which may not be visually intuitive for users expecting continuity.
