**Tags:** #data-visualization, #biome-mapping, #geospatial, #projection-conversion
**Created:** 2026-01-13
**Type:** code-notes

# biome_visualizer2

## Summary

```
Converts biome polygons into visual representations using geographic coordinates and pixel-based rendering for map visualization.
```

## Details

> This script handles biome data visualization by mapping geographic coordinates (latitude/longitude) to pixel coordinates for rendering on an image. It includes functions for converting between geographic and pixel-based systems, determining grid intervals based on zoom levels, and defining biome-specific color mappings. The script relies on external biome polygon data and processes them to render biome boundaries on an image grid, allowing for interactive or static biome map visualization.
> 
> The `BIOME_COLORS` dictionary assigns RGB values to biome types, while `geo_to_pixel` and `pixel_to_geo` functions approximate equirectangular projection conversions. The `get_grid_interval` function adjusts sampling resolution dynamically based on zoom level, ensuring clarity at varying scales.

## Key Functions

### `geo_to_pixel(lat, lon, center_lat, center_lon, zoom_factor, image_size)`

Converts geographic coordinates to pixel coordinates for rendering biome polygons.

### `pixel_to_geo(pixel_x, pixel_y, center_lat, center_lon, zoom_factor, image_size)`

Converts pixel coordinates back to approximate geographic coordinates (incomplete/inverse logic).

### `get_grid_interval(zoom_factor)`

Dynamically adjusts grid sampling resolution based on zoom level for optimal biome boundary rendering.

### `format_coord_label(value, is_latitude)`

Formats coordinate labels (e.g., "N12.34") for display purposes (incomplete snippet).

## Usage

1. Load biome polygon data via `load_biome_polygons()`.
2. Define a center point (latitude/longitude) and zoom level.
3. Call `geo_to_pixel()` to map biome coordinates to pixel positions for rendering.
4. Use `BIOME_COLORS` to assign colors to biome IDs.
5. Render polygons on an image using PIL’s `ImageDraw` and save via `save_image()`.

## Dependencies

> `numpy`
> `PIL (Pillow)`
> `image_saver (custom module)`

## Related

- [[Generators.Biomes.biomes2 (Core biome data module)
image_saver]]

>[!INFO] Incomplete Inverse Conversion
> `pixel_to_geo()` is a simplified approximation and may not perfectly reverse `geo_to_pixel()` due to projection limitations. For precise geospatial accuracy, consider using a dedicated mapping library (e.g., `geopy`).

>[!WARNING] Zoom-Level Bias
> Grid intervals (`get_grid_interval`) are heuristic and may not perfectly align with biome granularity at all zoom levels. Test with varying zoom factors for optimal rendering.
