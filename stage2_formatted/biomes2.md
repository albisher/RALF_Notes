**Tags:** #biome-data, #geospatial-processing, #text-file-parsing, #logging, #ast-literal-eval
**Created:** 2026-01-13
**Type:** code-library

# biomes2

## Summary

```
Processes biome polygons from a text file, mapping IDs to names and extracting geographic coordinates.
```

## Details

> This script loads biome polygons stored in a text file, where each line contains a biome ID and its corresponding polygon coordinates (latitude/longitude pairs). It uses `ast.literal_eval` to parse structured text entries, validates data integrity, and logs errors or warnings. The script handles missing files, malformed entries, and skips comments/empty lines. The `BIOME_ID_TO_NAME` dictionary provides a lookup for biome names by ID.

## Key Functions

### `get_biome_name_from_id(biome_id)`

Returns the biome name for a given integer ID using the predefined mapping.

### `load_biome_polygons(file_path)`

Parses a text file containing biome polygons, validates entries, and returns a list of dictionaries with `id` and `polygon` data. Returns `None` on error or `[]` if no valid entries exist.

## Usage

1. Ensure the file `extracted_biomes_with_coords.txt` exists at the specified path (`Maps/Code/extracted_biomes_with_coords.txt`).
2. Each line should follow the format: `"BiomeID: ID, Coordinates: [[[lat,lon], ...]]"`.
3. Call `load_biome_polygons()` to load polygons, or `get_biome_name_from_id(biome_id)` to resolve biome names.

## Dependencies

> ``os``
> ``ast``
> ``logging``

## Related

- [[none]]

>[!INFO] Important Note
> The script skips lines with `#` (comments) or empty whitespace. Ensure the input file matches the expected format exactly.

>[!WARNING] Caution
> Using `ast.literal_eval` can be unsafe if the input file contains untrusted data. Validate file integrity before execution.
