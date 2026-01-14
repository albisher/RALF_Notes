**Tags:** #heightmap-generation, #procedural-terrain, #Voronoi-neighbor-propagation, #Azgaar-algorithm, #deterministic-randomness
**Created:** 2026-01-13
**Type:** code-library

# heightmap_generator

## Summary

```
Generates deterministic heightmaps using neighbor propagation for procedural terrain generation.
```

## Details

> This code implements Azgaar’s neighbor propagation algorithm to create heightmaps from Voronoi cells. It begins with a random seed for reproducibility, then assigns high initial heights to a starting cell before propagating decrements to adjacent cells. The algorithm ensures efficient neighbor lookup via spatial indexing, identifying cells sharing edges (at least two vertices). Remaining unprocessed cells are filled with a sea level threshold.

## Key Functions

### ``HeightmapGenerator.__init__(seed)``

Sets up deterministic randomness using MD5-hashed seed.

### ``generate_heightmap(cells, sea_level)``

Core algorithm: starts with a random cell, assigns high height, propagates decrements to neighbors, and fills gaps with sea level.

### ``_build_neighbor_map(cells)``

Precomputes adjacency relationships between Voronoi cells for O(n log n) neighbor lookups.

## Usage

1. Initialize with a seed: `generator = HeightmapGenerator("my_seed")`
2. Define Voronoi cells (each with `i` and `v` keys): `cells = [...]`
3. Generate heights: `heights = generator.generate_heightmap(cells, sea_level=0.2)`

## Dependencies

> ``random``
> ``hashlib``
> ``typing.List``
> ``typing.Dict``
> ``typing.Set``

## Related

- [[Procedural Terrain Generation Notes]]
- [[Voronoi-Based Algorithms]]

>[!INFO] Deterministic Seed Handling
> Uses MD5 hashing to convert a string seed into a 32-bit integer for reproducible randomness.

>[!WARNING] Edge-Case Handling
> If no cells are provided, returns an empty dictionary. Neighbor map may include self-references if cells share all vertices (avoided via `not in neighbor_map[other_cell_id]` check).
