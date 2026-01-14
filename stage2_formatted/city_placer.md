**Tags:** #terrain-analysis, #biome-placement, #proximity-checking, #population-estimation, #deterministic-generation
**Created:** 2026-01-13
**Type:** code-library

# city_placer

## Summary

```
Generates optimal city placements based on terrain, biome, and proximity factors.
```

## Details

> The `CityPlacer` class evaluates land cells for suitability by scoring elevation, biome compatibility, water proximity, and area size. It then places cities in the highest-scoring locations while enforcing minimum distance constraints. The system uses deterministic seeding for reproducibility and assigns names/populations based on scoring thresholds.

## Key Functions

### ``calculate_suitability()``

Computes a weighted score for each cell based on elevation, biome, water proximity, and area.

### ``place_cities()``

Filters land cells, sorts by suitability, and places cities while respecting minimum distance requirements.

### ``_has_nearby_water()``

Checks if a cell is adjacent to water within a configurable radius.

### ``_distance()``

Euclidean distance calculation for spatial checks.

### ``_generate_name()``

Cyclically generates city names from predefined prefixes/suffixes.

### ``_calculate_population()``

Maps suitability scores to population ranges (1000–1,000,000).

### ``_determine_type()``

Classifies cities as capital, city, town, or village based on score and index.

## Usage

```python
placer = CityPlacer(seed="my_map")
cells = [...]  # List of cell dictionaries with 'i', 'p', 'area' keys
heightmap = {...}  # Height values by cell index
biomes = {...}    # Biome names by cell index
cities = placer.place_cities(cells, heightmap, biomes, num_cities=10)
```

## Dependencies

> ``random``
> ``math``
> ``hashlib` (Python standard library)`
> `no external dependencies.`

## Related

- [[World Generation Framework]]
- [[Biome Classification Module]]

>[!INFO] **Deterministic Seeding**
> Uses MD5 hashing of the input seed to ensure reproducible placements across runs.

>[!WARNING] **Water Proximity Approximation**
> `_has_nearby_water()` uses a fixed radius multiplier (50×) for cell-to-cell distance checks; adjust if cell sizes vary.
