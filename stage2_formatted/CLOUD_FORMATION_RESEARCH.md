**Tags:** #procedural-generation, #2d-top-view, #cloud-formation, #perlin-noise, #fast-algorithms
**Created:** 2026-01-13
**Type:** code-notes

# CLOUD_FORMATION_RESEARCH

## Summary

```
Fast procedural cloud generation for low-resolution 2D top-view maps using deterministic noise and hash-based patterns.
```

## Details

> This code implements fast procedural algorithms for generating cloud formations in low-resolution 2D top-view maps. It combines Perlin-like noise generation with hash-based pseudo-randomness to create cloud density variations, floating platforms, layered cloud formations, and natural boundaries. The system uses additive noise layers, Gaussian distributions for platform shapes, and deterministic parameters derived from input hashes to ensure reproducibility.

## Key Functions

### `generate_cloud_noise_fast`

Creates cloud-like noise patterns using hash-based pseudo-Perlin noise with configurable octaves and scale.

### `generate_cloud_platforms_fast`

Produces floating cloud platforms with varying radii, elevations, and noise-based boundaries.

### `generate_layered_clouds_fast`

Generates multi-layer cloud formations with distinct scales and opacities per layer.

### `generate_cloud_world_fast`

Combines all cloud components into a single deterministic cloud world map.

## Usage

1. Call `generate_cloud_noise_fast` to create base cloud noise.
2. Use `generate_cloud_platforms_fast` to add floating cloud clusters with natural boundaries.
3. Apply `generate_layered_clouds_fast` to stack multiple cloud layers with varying properties.
4. Finally, combine all layers in `generate_cloud_world_fast` to produce a complete map using a base hash for deterministic results.

## Dependencies

> `numpy`
> `hashlib`

## Related

- [[Map Generation Path - World Type: Cloud World]]

>[!INFO] Deterministic Hashing
> All functions use hash-based parameters to ensure reproducible cloud formations across runs with the same input hash.

>[!WARNING] Normalization Sensitivity
> Small changes in noise values can drastically alter cloud appearance due to normalization steps. Ensure consistent hash inputs for predictable results.
