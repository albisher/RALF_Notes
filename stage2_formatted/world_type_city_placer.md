**Tags:** #world-generation, #procedural-placement, #game-dev, #procedural-naming, #space-systems
**Created:** 2026-01-13
**Type:** code-library

# world_type_city_placer

## Summary

```
Generates and evaluates city placements with world-type-specific logic for names, types, and suitability scoring.
```

## Details

> This code defines a `WorldTypeCityPlacer` class that dynamically assigns city suitability scores based on world type (e.g., fantasy planet, space station, galaxy outpost). It uses a deterministic seed for reproducibility and categorizes worlds into predefined types (e.g., "galaxy," "space_station") via `_categorize_world()`. Suitability is calculated via specialized methods (e.g., `_calculate_planet_suitability()`, `_calculate_station_suitability()`), which apply world-specific rules (e.g., elevation, biome preference, or proximity to water for planets; deck-level suitability for space stations). The class integrates heightmaps and biome data to compute scores, which determine optimal city placement.

## Key Functions

### ``__init__(self, seed`

str, world_type: str, world_description: str)`**: Initializes the placer with a seed for reproducibility and categorizes the world type.

### ``_categorize_world(self, world_type`

str, description: str)`**: Determines the world category (e.g., "fantasy_planet," "space_station") based on keywords in `world_type` or `world_description`.

### ``calculate_suitability(self, cell`

Dict, cells: List[Dict], heightmap: Dict[int, float], biomes: Dict[int, str])`**: Delegates suitability calculation to the appropriate world-type method.

### ``_calculate_planet_suitability(self, ...)``

Computes suitability for fantasy planets using elevation, biome preference, and water proximity.

### ``_calculate_galaxy_suitability(self, ...)``

Evaluates suitability for galaxy outposts based on energy/density (heightmap) and nebula/void biome scores.

### ``_calculate_station_suitability(self, ...)``

Assigns scores to space station sections (e.g., core, habitation) based on biome type.

### ``_calculate_ship_suitability(self, ...)``

(Incomplete; likely intended to handle space ship deck-level suitability.)

### ``_has_nearby_water(self, cell`

Dict, cells: List[Dict], heightmap: Dict[int, float], radius: int)`**: Helper to check if a cell is near water (used in planet suitability).

## Usage

1. Instantiate `WorldTypeCityPlacer` with a seed and world details:
   ```python
   placer = WorldTypeCityPlacer(seed="my_seed", world_type="Planet", world_description="A lush fantasy world")
   ```
2. Use `calculate_suitability()` to evaluate a cell’s suitability for city placement:
   ```python
   cell = {"i": 123, "area": 200}
   heightmap = {123: 0.45}
   biomes = {123: "forest"}
   score = placer.calculate_suitability(cell, [], heightmap, biomes)
   ```
3. The score determines city type/name generation logic (e.g., higher scores favor grassland cities).

## Dependencies

> ``random``
> ``math``
> ``typing``
> ``hashlib` (Python standard library); no external libraries.`

## Related

- [[Procedural World Generation Notes]]
- [[Space Station Design Guide]]

>[!INFO] World Categorization
> The `_categorize_world()` method uses keyword matching (e.g., "galaxy," "station") to auto-categorize worlds, enabling dynamic suitability logic. This avoids hardcoding for all possible world types.

>[!WARNING] Incomplete Ship Suitability
> The `_calculate_ship_suitability()` method is truncated (ends with `=` instead of `==`). Ensure this is fixed to avoid runtime errors during space-ship placements.
