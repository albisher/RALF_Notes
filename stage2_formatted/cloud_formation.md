**Tags:** #perlin_noise, #hash_based_generation, #numerical_simulation, #cloud_generation, #procedural_terrain
**Created:** 2026-01-13
**Type:** code-library

# cloud_formation

## Summary

```
Generates procedural cloud platforms and heightmaps using hash-based pseudo-Perlin noise for dynamic cloud world generation.
```

## Details

> This code implements a system to create floating cloud platforms and heightmaps using deterministic hash-based algorithms. It generates distinct cloud clusters with varying elevations, radii, and densities by leveraging SHA-256 hashing to derive parameters like center coordinates, radii, and elevation levels. The `generate_cloud_noise_fast` function uses a pseudo-Perlin noise approach to add natural noise for cloud boundaries. The `generate_cloud_world_fast` function combines platforms and applies a threshold to create a binary cloud/void map. The `generate_cloud_heightmap_hash_based` function maps cell coordinates to cloud density values, converting them into height values for terrain representation.

## Key Functions

### `generate_cloud_platforms_fast`

Creates floating cloud clusters with randomized parameters derived from a base hash.

### `generate_cloud_noise_fast`

Implements hash-based pseudo-Perlin noise for natural cloud boundary effects.

### `generate_cloud_world_fast`

Combines platforms into a complete cloud/void map with thresholding for dense regions.

### `generate_cloud_heightmap_hash_based`

Maps cell coordinates to cloud density values, converting them into height values for procedural terrain.

## Usage

1. Call `generate_cloud_platforms_fast` to generate individual cloud clusters.
2. Use `generate_cloud_noise_fast` to add noise for natural cloud edges.
3. Combine platforms into a full map with `generate_cloud_world_fast`.
4. For terrain heightmaps, use `generate_cloud_heightmap_hash_based` with a list of cell coordinates.

## Dependencies

> `numpy`
> `hashlib`

## Related

- [[cloud_formation_research]]
- [[procedural_generation_techniques]]

>[!INFO] Important Note
> The `generate_cloud_platforms_fast` function uses SHA-256 hashing to derive platform parameters, ensuring reproducibility with the same base hash.

>[!WARNING] Caution
> The `generate_cloud_noise_fast` function uses bilinear interpolation, which may introduce artifacts if the grid resolution is too coarse relative to the target resolution. Ensure `scale` and `octaves` are appropriately tuned for desired noise quality.
