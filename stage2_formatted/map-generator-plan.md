**Tags:** #procedural-generation, #map-algorithms, #biome-distribution, #heightmap, #noise-algorithms, #coordinate-system, #world-building, #event-triggering
**Created:** 2026-01-13
**Type:** documentation-research

# map-generator-plan

## Summary

```
Plans for integrating Azgaar’s Fantasy Map Generator into an app to create dynamic world maps with height, biomes, and cities tied to story events via coordinates and timestamps.
```

## Details

> This document outlines a **modular, box-based architecture** for generating maps using Azgaar’s algorithms, ensuring compatibility with existing world/event systems. The plan leverages **Perlin/Simplex noise** for heightmap generation, biome assignment based on elevation/climate, and city placement via terrain analysis. The system integrates with a **coordinate-based world** where events and story elements reference spatial and temporal data (e.g., `latitude/longitude`, `timestamps`). The implementation prioritizes **reusability** and **standardized I/O** through OOP-based `Box` components, each handling a specific generation step (e.g., heightmap, biome, city placement).

## Key Functions

### ``HeightmapGenerationBox``

Creates elevation data using procedural noise, supports templates, and provides normalized height statistics.

### ``BiomeAssignmentBox``

Maps cells to biomes based on height, precipitation, and temperature, with customizable rules.

### ``CityPlacementBox``

Places settlements by evaluating terrain features (e.g., water proximity, elevation), respecting constraints like city spacing.

### ``process_map_data.py``

Parses Azgaar’s map format (e.g., `pack.cells` with `h`, `biome`, `p` fields) for downstream systems.

### ``Box` architecture`

Enables modularity—each box processes input/output via `BoxInput/BoxOutput` and supports multiple operations (e.g., `generate`, `customize`).

## Usage

1. **Initialize Boxes**: Instantiate each box (e.g., `heightmapBox.generate()`) with parameters like `seed`, `width`, or `numCities`.
2. **Chain Operations**: Feed outputs from one box (e.g., `heightmap`) into the next (e.g., `biomeAssignmentBox.assign()`).
3. **Integrate with World System**: Use generated coordinates (`p`) to link cities/events to story cards (e.g., `coordinates: {x, y}` in JSONB).
4. **Customize**: Override default rules (e.g., `biomeRules`, `minDistance`) via input parameters.

## Dependencies

> ``ui-beta/src/boxes/maps/heightmap_generation_box.js``
> ``ui-beta/src/boxes/maps/biome_assignment_box.js``
> ``ui-beta/src/boxes/maps/city_placement_box.js``
> ``app/process_map_data.py``
> ``js-noise` (for procedural noise)`
> ``jsonb` (for coordinate storage).`

## Related

- [[Azgaar Fantasy Map Generator Documentation]]
- [[World Building Coordinate System Design]]
- [[Event Triggering System Integration Plan]]

>[!INFO] **Coordinate System Alignment**
> The map’s `mapCoordinates` (e.g., `latN`, `lonW`) must align with the app’s world system’s `latitude/longitude` fields to ensure spatial consistency. Mismatches could cause events to appear misplaced.

>[!WARNING] **Biome Rule Overrides**
> Custom `biomeRules` in `BiomeAssignmentBox` may conflict with default climate assumptions (e.g., deserts at high elevation). Test edge cases (e.g., extreme precipitation/temperature) to avoid unrealistic biome placements.

>[!INFO] **City Placement Constraints**
> The `minDistance` parameter in `CityPlacementBox` must balance density and aesthetics. Values too low may result in overcrowded maps; too high could yield sparse settlements. Iterate with user feedback.
