**Tags:** #JSON_Structure, #Map_Data, #Galaxy_Simulation, #Data_Comparison, #Biome_System, #Metadata_Fields
**Created:** 2026-01-13
**Type:** documentation

# GALAXY_MAP_COMPARISON

## Summary

```
Compares JSON structures of a galaxy map and a fantasy planet map, highlighting differences in biome representation, metadata, and spatial coordinates.
```

## Details

> This document analyzes the JSON file structures of two map datasets: a galaxy map (`galaxy_map_jjj.json`) and a fantasy planet map (`ui-beta/maps/quraan_map.json`). While both follow a similar top-level JSON schema, they differ significantly in biome representation (dict vs. list), metadata completeness, and spatial coordinate ranges. The galaxy map uses a simplified cell-to-biome mapping with string identifiers, whereas the Quraan map employs detailed biome objects with color and ID attributes. The galaxy map also includes cities for star systems, while the Quraan map lacks them. Both share identical cell structure definitions but differ in resolution and metadata fields.

## Key Functions

### ``biomes` (dict/list)`

Maps cell IDs to biome names or stores biome objects with metadata.

### ``mapCoordinates``

Defines spatial bounds (galactic vs. planetary).

### ``cities``

Contains star systems/outposts (galaxy) or empty (planet).

### ``info``

Metadata section with version, description, and export details.

### ``pack``

Core container for vertices, biomes, and cell data.

## Usage

To apply these findings:
1. **Convert Biomes**: Adjust galaxy map biomes to match Quraan’s list format if frontend expects it.
2. **Add Metadata**: Include missing fields (`version`, `seed`, etc.) in galaxy maps for consistency.
3. **Validate Coordinates**: Ensure spatial ranges align with intended use cases (e.g., tropical boundaries for Quraan).
4. **Statistics**: Add missing statistics section to galaxy maps for completeness.

## Dependencies

> ``json``
> ``Obsidian/Markdown` (for documentation)`
> ``Fantasy-map-generator` (for Quraan map generation)`
> ``StarMapTools` (for galaxy map tools).`

## Related

- [[Galaxy_Map_Generator_Guide]]
- [[Fantasy_Map_Comparison_Notes]]
- [[JSON_Structure_Standards]]

>[!INFO] Biome Format Impact
> Frontend applications may require conversion between dict (`{cell_id: "biome"}`) and list (`[{name, color, id}]`) formats to avoid rendering errors.

>[!WARNING] Metadata Inconsistency
> Missing fields like `seed` or `mapId` in galaxy maps could cause errors if referenced externally (e.g., in game engines or analytics). Always validate metadata completeness.
