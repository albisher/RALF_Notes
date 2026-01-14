**Tags:** #biome-generation, #environmental-simulation, #moisture-distribution, #wind-patterns, #planet-science
**Created:** 2026-01-13
**Type:** code-notes

# moisture_calculator_box

## Summary

```
Calculates moisture levels for biome assignment using Whittaker Diagram principles, accounting for distance from water, wind, and elevation.
```

## Details

> This code implements a `MoistureCalculatorBox` class that computes moisture values for each cell in a Voronoi grid based on its proximity to water bodies, prevailing wind direction, and elevation. The Whittaker Diagram logic is applied to determine biome suitability by combining moisture, temperature (implicitly via elevation), and wind effects. Water cells (below sea level) are assigned a moisture value of 1.0, while other cells derive moisture from their distance to the nearest water source, adjusted by wind patterns and elevation (rain shadow effect).

## Key Functions

### ``execute(self, input_data`

BoxInput) -> BoxOutput`**: Orchestrates the moisture calculation pipeline, validating inputs, computing moisture values, and returning results with metadata.

### ``_distance(self, p1`

List[float], p2: List[float]) -> float`**: Computes Euclidean distance between two 2D coordinates (cell positions).

### ``_max_distance(self, cells`

List[Dict]) -> float`**: Determines the maximum pairwise distance among all cells to normalize moisture calculations.

### ``_calculate_wind_factor(self, ...)``

Adjusts moisture based on wind direction (e.g., westerly moisture from western water sources) using a deterministic hash (`world_hash`) for reproducibility.

## Usage

1. Initialize `MoistureCalculatorBox` and call `execute()` with a `BoxInput` containing:
   - `operation="calculate_moisture"` (required).
   - `cells`: List of Voronoi cells (each with `i` and `p` keys).
   - `heights`: Dictionary mapping cell IDs to elevation values.
   - `wind_direction`: Optional wind direction (default: "westerly").
2. Output includes `moisture` (per-cell values) and `wind_pattern` metadata.

## Dependencies

> `numpy`
> `hashlib`
> `boxes.core.box_interface`

## Related

- [[Whittaker Diagram for Biome Classification]]
- [[Voronoi Cell-Based Terrain Generation]]

>[!INFO] Wind Direction Dependency
> The wind factor (`_calculate_wind_factor`) assumes a deterministic relationship between wind direction and moisture contribution. For example, westerly winds may push moisture from western water cells eastward, but this logic is simplified and may need tuning for specific planetary conditions.


>[!WARNING] Edge Case Handling
> If no water cells are found (`water_cells_found = 0`), all cells will default to `0.0` moisture. Ensure `heights` and `cells` are properly populated to avoid this. The `max_dist` fallback (`1.0`) prevents division by zero but may distort results if distances are negligible.
