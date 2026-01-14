**Tags:** #visualization, #biome_mapping, #geospatial, #image_processing
**Created:** 2026-01-13
**Type:** code-notes

# biome_visualizer

## Summary

```
Generates biome visualizations from geographic polygons into pixel-based images using customizable color schemes.
```

## Details

> This script converts biome polygons (geographic coordinates) into pixel-based images by mapping geographic locations to pixel positions. It uses a `BIOME_COLORS` dictionary to assign RGB values to biome types, then renders polygons centered around specified coordinates. The `geo_to_pixel` function converts latitude/longitude to pixel coordinates based on zoom level and image dimensions. The `generate_biome_map` function loads biome polygons, sorts them (water first, then land), and draws them onto an image using PIL/Pillow. Default fallback colors are applied if biome data is missing.

## Key Functions

### `geo_to_pixel(lat, lon, center_lat, center_lon, zoom_factor, image_size)`

Converts geographic coordinates to pixel coordinates for rendering.

### `generate_biome_map(center_coords, zoom_factor, image_size)`

Main function that loads biome polygons, processes them, and renders a biome map image.

### `load_biome_polygons()`

Loads biome polygon data (assumed imported from `Biomes.biomes`).

### `get_biome_name_from_id(biome_id)`

Retrieves biome name from its ID (assumed imported from `Biomes.biomes`).

## Usage

1. Call `generate_biome_map(center_coords, zoom_factor, image_size)` with:
   - `center_coords`: Tuple of (latitude, longitude) for the map center.
   - `zoom_factor`: Determines the scale of the map (affects polygon size).
   - `image_size`: Output image dimensions (default: 512).
2. The function returns a PIL `Image` object with biome polygons rendered.

## Dependencies

> `numpy`
> `PIL/Pillow`
> `Biomes.biomes module (custom project dependency)`

## Related

- [[Biomes]]

>[!INFO] Coordinate Parsing
> The script assumes `parse_coordinates(center_coords)` exists to validate input coordinates (e.g., parsing strings like `"lat,lon"`). If not implemented, it raises a `ValueError`.

>[!WARNING] Fallback Behavior
> If biome polygons fail to load, the script defaults to a `Deep Ocean` base color and returns a blank map. For pixel-by-pixel fallback, uncomment `generate_biome_map_pixel_by_pixel` (not implemented here).
