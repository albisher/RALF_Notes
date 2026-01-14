**Tags:** #Voronoi, #Geospatial, #Generative, #Procedural, #MapGeneration, #SpatialPartitioning
**Created:** 2026-01-13
**Type:** code-library

# voronoi_generator

## Summary

```
Generates deterministic Voronoi diagrams for procedural map cell structures with configurable seed and point count.
```

## Details

> This library implements a Voronoi diagram generator using `scipy.spatial.Voronoi` to create spatial partitions for map design. It initializes with a seed value for reproducibility, then generates random points within specified map dimensions, computes cell centers, areas, and clipped vertices to ensure they remain within bounds. The core workflow involves point distribution, Voronoi construction, and post-processing to extract structured cell data.

## Key Functions

### `VoronoiGenerator`

Main class initializing generator with seed and point count.

### `generate_points(width, height)`

Creates random seed points scaled to map dimensions.

### `create_voronoi(points)`

Constructs Voronoi diagram from input points.

### `extract_cells(voronoi, width, height)`

Processes regions into structured cell dictionaries with metadata.

### `_calculate_center(vertices)`

Computes centroid of polygon vertices using arithmetic mean.

### `_calculate_area(vertices)`

Implements shoelace formula for polygon area calculation.

### `_clip_vertices(vertices, width, height)`

Truncates vertex coordinates to map boundaries.

## Usage

```python
generator = VoronoiGenerator(seed="my_map", num_points=100)
points = generator.generate_points(width=1000, height=500)
voronoi = generator.create_voronoi(points)
cells = generator.extract_cells(voronoi, width=1000, height=500)
```

## Dependencies

> `numpy`
> `scipy.spatial.Voronoi`
> `hashlib`

## Related

- [[Procedural Terrain Generation]]
- [[Spatial Partitioning Algorithms]]

>[!INFO] Deterministic Seed Handling
> Uses MD5 hashing of input seed to ensure consistent random number generation across runs.

>[!WARNING] Edge Region Filtering
> Skips invalid regions (containing -1 or empty vertices) to prevent malformed cell data.
