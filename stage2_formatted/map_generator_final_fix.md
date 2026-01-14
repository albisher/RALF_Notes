**Tags:** #data-structure, #error-handling, #type-mismatch, #frontend-backend-integration, #map-generation, #biome-rendering
**Created:** 2026-01-13
**Type:** code-fix

# map_generator_final_fix

## Summary

```
Fixes incorrect parameter type in map generator, ensuring biome data is passed as a dictionary for proper rendering.
```

## Details

> The `_assemble_map` function previously received a `List[Dict]` (biome_list) instead of a `Dict[int, str]` (biomes), causing the frontend to fail when rendering Voronoi cells. The fix ensures the biome data is structured correctly as a dictionary, where keys are cell identifiers and values are biome names. The `MapRenderBox` component was also updated to handle both formats for backward compatibility, extracting biome data from cells if not found in the packed data.

## Key Functions

### ``_assemble_map``

Assembles map data from cells, biomes, and cities, ensuring biome data is passed as a dictionary.

### ``MapRenderBox``

Renders Voronoi cells with biome colors and cities as red dots, with support for both dict and list biome formats.

## Usage

1. Call `_assemble_map` with `biomes` (a dictionary) instead of `biome_list` (a list).
2. Ensure `MapRenderBox` receives the correct biome structure to render properly.
3. Test by generating a map via the frontend form and verifying the rendered output matches expectations.

## Dependencies

> ``services/map-generator/engine/map_generator.py``
> ``pack` (likely a module handling serialized map data)`
> ``List``
> ``Dict` (Python standard types)`
> `and frontend components (`MapPreview``
> ``WorldMap2D`).`

## Related

- [[map_generator]]
- [[map-rendering-components]]
- [[pack]]

>[!INFO] Important Note
> The fix ensures `pack.biomes` is a dictionary (`{cellId: 'biome_name'}`) for accurate Voronoi rendering. If backward compatibility is critical, the `MapRenderBox` update handles both formats gracefully.


>[!WARNING] Caution
> If the frontend expects a list format, ensure the `MapRenderBox` logic is updated to handle both cases explicitly to avoid rendering inconsistencies. Test thoroughly with both input types.
