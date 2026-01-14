**Tags:** #location-service, #coordinate-generation, #biome-detection, #deterministic-placement, #geospatial-computation
**Created:** 2026-01-13
**Type:** documentation-research

# location_service

## Summary

```
Core service for generating deterministic locations, biome detection, and proximity-based element placement using hash-based inputs.
```

## Details

> This `LocationService` integrates external positioning and mapping generators to produce structured location data (latitude/longitude, biome, Cartesian coordinates) from user-provided hash seeds. It supports deterministic generation via hashing, coordinate parsing, biome lookup, and distance/bearing calculations. The service dynamically adapts to available generators (falling back to development paths if imports fail).
> 
> Key workflows include:
> 1. **Hash-based generation**: Converts input strings into deterministic coordinates using `hash_input` and `generate_coordinates`.
> 2. **Biome detection**: Uses `get_biome` to classify terrain at given coordinates.
> 3. **Proximity queries**: Implements Haversine formula for distance calculations between locations.

## Key Functions

### ``generate_location_from_hash``

Creates a `LocationData` object from a seed string, including formatted coordinates, biome, and zone metadata.

### ``parse_coordinate_input``

Extracts latitude/longitude/zoom from strings like `"c=40.7128,-74.0060 z=10"`.

### ``get_biome_at_coordinates``

Returns biome classification for raw coordinates (e.g., `"Temperate Forest"`).

### ``calculate_distance``

Computes Haversine distance between two `LocationData` instances.

### ``calculate_bearing``

Determines compass direction (in degrees) from one location to another.

### ``LocationData``

Structured container for all location attributes (e.g., `latitude`, `biome`, `hash_seed`).

### ``ProximityResult``

Stores results for proximity searches (e.g., element ID, distance, bearing).

## Usage

1. **Initialize**: `service = LocationService()` (checks if generators are available).
2. **Generate locations**: `location = service.generate_location_from_hash("seed123")`.
3. **Query biomes**: `biome = service.get_biome_at_coordinates(40.7128, -74.0060)`.
4. **Calculate distances**: `distance = service.calculate_distance(loc1, loc2)`.

## Dependencies

> ``Positioning.coordinate``
> ``Positioning.coordinate_parser``
> ``Maps.Biomes.biomes``
> ``math` (via `import math` in `calculate_distance`).`

## Related

- [[`coordinate_generation_guide]]
- [[`biome_detection_algorithm]]

>[!INFO] Fallback Mechanism
> If `LOCATION_GENERATORS_AVAILABLE` is `False`, the service raises `RuntimeError` for generation methods or returns `"Unknown"`/`"Generic Terrain"` for biome queries.

>[!WARNING] Precision Limits
> Cartesian coordinates use `EARTH_RADIUS_KM` (assumed constant), which may introduce rounding errors for extreme latitudes/longitudes.
