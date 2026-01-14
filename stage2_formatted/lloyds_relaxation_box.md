**Tags:** #Voronoi, #Geospatial, #Optimization, #Spatial, #DataProcessing, #PhysicsSimulation, #IterativeAlgorithm
**Created:** 2026-01-13
**Type:** code-implementation

# lloyds_relaxation_box

## Summary

```
Implements Lloyd’s relaxation algorithm to refine Voronoi cell boundaries by iteratively moving points toward polygon centroids.
```

## Details

> This box class processes spatial point distributions to improve Voronoi cell smoothness by repeatedly moving each point toward the centroid of its associated polygon. The algorithm:
> 1. Takes initial seed points and applies a Voronoi diagram computation.
> 2. For each iteration, it calculates polygon centroids (averaging vertices) and moves points toward these centroids.
> 3. Clips vertices to map boundaries and enforces clamping to prevent out-of-bounds movement.
> 4. Supports configurable iterations (default: 2) and validates world types (e.g., "planet") before processing.

## Key Functions

### `LloydsRelaxationBox`

Core class wrapping the relaxation logic, with `execute()` handling input/output and `supported_world_types` defining applicable environments.

### `execute()`

Core method that:

### `_calculate_centroid()`

Helper method computing polygon centroids as the arithmetic mean of vertices.

## Usage

```python
# Initialize and call
box = LloydsRelaxationBox()
result = box.execute({
    "operation": "relax_points",
    "world_type": "planet",  # Must match supported_world_types
    "points": [[x1,y1], [x2,y2]],  # Initial Voronoi seeds
    "width": 1000, "height": 1000,
    "iterations": 2  # Optional (default: 2)
})
```

## Dependencies

> ``numpy``
> ``scipy.spatial.Voronoi``
> ``boxes.core.box_interface` (Box`
> `BoxInput`
> `BoxOutput).`

## Related

- [[VoronoiDiagramProcessing]]
- [[SpatialOptimizationAlgorithms]]

>[!INFO] Iteration Handling
> Defaults to 2 iterations but allows customization via `iterations` parameter. Higher values improve smoothness but risk instability for degenerate polygons.


>[!WARNING] Boundary Clamping
> Clamped centroids may deviate from true polygon centers if vertices exceed map bounds. Explicit bounds checking (`max(0, min(width, v[0]))`) mitigates this but may distort results.
