**Tags:** #input-parsing, #coordinate-conversion, #map-generation, #biome-visualization
**Created:** 2026-01-13
**Type:** code-notes

# map_input_parser

## Summary

```
Parses and validates map input coordinates (decimal or N/S/E/W format) for biome visualization, generating output images.
```

## Details

> This script handles flexible input formats for latitude/longitude coordinates (e.g., `c=40.7128,-74.0060 z=5.5` or `c=N40.7128,W74.0060 z=10`) and validates them using a biome visualization library. It converts inputs into a standardized N/S/E/W format, validates ranges, and ensures compatibility with a visualizer module. The validated data is then used to generate and save a map image to a specified directory.

## Key Functions

### `convert_decimal_to_nswe(lat, lon)`

Converts decimal latitude/longitude to directional format (e.g., `N40.7128,W74.0060`).

### `parse_flexible_input(input_str)`

Parses and validates user input strings for coordinates and zoom level, returning validated results or error messages.

### `generate_map(center_coords, zoom_factor, output_path)`

Placeholder for map generation logic (currently prints confirmation).

### `save_biome_map(validated_nswe_coords, validated_zoom, output_path)`

Delegates map generation to `biome_visualizer2` (external dependency).

## Usage

1. Run the script interactively by entering a coordinate input (e.g., `c=40.7128,-74.0060 z=5.5`).
2. The script validates input, sanitizes coordinates, and saves the generated map to `Maps/Images/` as a PNG file.
3. Supports both decimal and directional formats for latitude/longitude.

## Dependencies

> ``argparse``
> ``re``
> ``os``
> ``sys``
> ``math``
> ``numpy``
> ``PIL.Image``
> ``image_saver``
> ``Maps.Code.biome_visualizer2``

## Related

- [[biome_visualizer2]]
- [[Images]]
- [[Generators]]

>[!INFO] Input Validation
> The script enforces strict bounds for latitude (-90 to 90) and longitude (-180 to 180). Negative zoom values trigger an error.

>[!WARNING] Sanitization Risk
> `sanitized_coords` replaces invalid characters with underscores, which may alter filenames if not handled carefully. Ensure filenames are checked before use.
