**Tags:** #data-processing, #map-coordinates, #json-manipulation
**Created:** 2026-01-13
**Type:** documentation

# process_map_data

## Summary

```
Processes map data from a JSON file to extract and transform map boundaries, coordinates, and biome information for visualization or analysis.
```

## Details

> This script reads a JSON file containing map data, extracts vertex coordinates, and computes map boundaries (origin and dimensions). It also calculates internal coordinate mappings for global lines (Prime Meridian and Equator) based on provided geographic data. The script processes map metadata, vertices, biomes, and cells, ensuring compatibility with different data formats (e.g., Azgaar export vs. original format). Default values are applied if missing data is detected.

## Key Functions

### `calculate_map_boundaries_from_vertices(vertices_p_list)`

Computes the map’s origin (min/max coordinates) and native dimensions from vertex coordinates.

### `calculate_global_lines_internal_coords(map_coords_data, info_data)`

Maps geographic coordinates (longitude/latitude) to internal pixel coordinates for rendering global lines.

### `process_map_data(input_file_path, output_file_path)`

Orchestrates loading, parsing, and transforming the input JSON file into a structured output, handling vertices, biomes, and cells.

## Usage

1. Call `process_map_data()` with paths to input (`input_file_path`) and output (`output_file_path`) JSON files.
2. The script validates input, defaults missing metadata, and processes vertices, biomes, and cells.
3. Output includes processed metadata, vertices, and structured cell data.

## Dependencies

> `json`
> `sys`
> `os`

## Related

- [[none]]

>[!INFO] Default Values
> If no valid vertices are provided, the function returns default dimensions (1000x1000) to avoid division-by-zero errors.

>[!WARNING] Biome Index Handling
> If biome data arrays (`name`, `color`, `original_id`) are mismatched in length, indices are clamped to avoid index errors. Ensure consistency in input data.
