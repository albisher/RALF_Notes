**Tags:** #visualization, #point-cloud, #nebula-fog, #galaxy-generation, #deterministic-randomness, #hashing, #density-mapping
**Created:** 2026-01-13
**Type:** code-notes

# galaxy_point_cloud_box

## Summary

```
Generates a smooth nebula point cloud for galaxy visualization, replacing rigid Voronoi borders with probabilistic energy-weighted points.
```

## Details

> This box processes galaxy data to create a soft, fog-like point cloud effect by sampling positions weighted by energy/density values from Voronoi cells. It uses deterministic hashing to ensure reproducibility while introducing controlled randomness for organic star-like variations. The system supports optional density mapping and hyperlane extraction from the Voronoi graph for travel routes.

## Key Functions

### `execute`

Core logic that validates input, generates points, computes density maps, and extracts hyperlanes based on Voronoi cell data.

### `_extract_hyperlanes`

Private method to derive travel routes from the Voronoi graph (not detailed in snippet).

### `GalaxyPointCloudBox`

Main class wrapping BoxInterface, enforcing world-type support for galaxies.

## Usage

1. Call with `operation="generate_point_cloud"` and required fields (`world_hash`, `cells`, `heights`).
2. Optional parameters: `num_points` (default 5000), `density_map` (default True).
3. Returns `point_cloud` (list of dicts with `x`, `y`, `brightness`, `size`), `density_map` (2D array), and `hyperlanes`.

## Dependencies

> `numpy`
> `hashlib`
> `boxes.core.box_interface`

## Related

- [[GalaxyVoronoiBox]]
- [[NebulaVisualizationPipeline]]

>[!INFO] Deterministic Randomness
> Uses SHA-256 hashing to ensure reproducible point distributions across runs while allowing controlled randomness via partial hashing (e.g., `point_hash[:8]` for x-coordinate).

>[!WARNING] Edge Cases
> If `cells` is empty or `world_type` is unsupported, returns early with metadata to avoid silent failures. Density maps normalize to `[0,1]`; invalid values default to 0.5.
