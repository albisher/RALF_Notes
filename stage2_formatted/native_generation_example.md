**Tags:** #Voronoi-diagram, #Perlin-noise, #Biome-generation, #Map-generation, #Python-algorithms
**Created:** 2026-01-13
**Type:** documentation-research

# native_generation_example

## Summary

```
Generates procedural maps using Python’s Voronoi diagrams and Perlin noise for terrain and biome assignment.
```

## Details

> This script implements a native map generation system in Python, replicating Azgaar’s approach with Voronoi diagrams for cell division and Perlin noise for height variation. It includes methods for seed point distribution, Voronoi diagram creation, heightmap generation, biome assignment, and conversion to Azgaar-compatible JSON format. The code uses `scipy.spatial.Voronoi` for geometric computations and `noise.pnoise2` for natural-looking terrain.

## Key Functions

### ``generate_seed_points``

Creates uniformly distributed seed points for Voronoi sampling.

### ``generate_voronoi``

Computes a Voronoi diagram with boundary points to ensure full map coverage.

### ``generate_heightmap``

Applies Perlin noise to assign height values to each Voronoi cell.

### ``assign_biomes``

Maps height ranges to biome types (e.g., Ocean, Forest) using predefined thresholds.

### ``voronoi_to_azgaar_format``

Converts the generated data into a JSON structure compatible with Azgaar’s map system.

## Usage

1. Initialize `NativeMapGenerator` with a seed for reproducibility.
2. Call `generate_seed_points` to create Voronoi seed coordinates.
3. Use `generate_voronoi` to compute the diagram.
4. Apply `generate_heightmap` to assign terrain heights via Perlin noise.
5. Assign biomes with `assign_biomes` and convert to Azgaar format with `voronoi_to_azgaar_format`.

## Dependencies

> ``scipy``
> ``numpy``
> ``noise``
> ``shapely` (implied for boundary handling`
> `though not explicitly imported).`

## Related

- [[`Azgaar’s Procedural Map System`]]
- [[`Voronoi Diagram Tutorials`]]

>[!INFO] Boundary Handling
> The `generate_voronoi` method adds boundary points to ensure the Voronoi diagram fully encloses the map area, preventing edge artifacts.

>[!WARNING] Simplification Note
> The `generate_seed_points` method uses uniform random sampling for simplicity; a production implementation should use Poisson disc sampling for better point distribution.
