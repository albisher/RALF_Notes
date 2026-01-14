**Tags:** #weather, #celestial, #world-building, #procedural-generation, #environmental
**Created:** 2026-01-13
**Type:** documentation

# weather_calculation_box

## Summary

```
Calculates dynamic weather conditions based on celestial influences, world moods, and location-specific factors.
```

## Details

> This box integrates celestial object data (e.g., stars, moons) and world conditions (e.g., a giant’s mood) to generate realistic weather outcomes. It adjusts temperature, humidity, and weather type (sunny, stormy, rainy, etc.) based on overrides or default rules. The system also incorporates location metadata (e.g., biome type) for refined environmental effects.

## Key Functions

### `execute`

Orchestrates weather calculation by processing inputs (world_id, celestial objects, etc.), applying conditional logic, and returning structured weather data.

### `World.query.filter_by`

Retrieves world data from a database to fetch base celestial objects and conditions.

### `Card.query.filter_by`

Fetches location-specific metadata (e.g., biome) for adjustments.

## Usage

1. Pass required `world_id` and optional `location_id`/`timestamp` to compute weather.
2. Override celestial objects or world conditions via `celestial_objects`/`world_conditions` dictionaries.
3. Output includes `weather_type`, `temperature`, `humidity`, and metadata on influencing factors.

## Dependencies

> `db`
> `World`
> `Card`
> `Weather (SQLAlchemy models)`
> `Box`
> `BoxInput`
> `BoxOutput (from `..core.box_interface`)`
> `datetime`

## Related

- [[World Building System]]
- [[Procedural Environment Generation]]

>[!INFO] Default Values
> Defaults (e.g., `sunny`, `20.0°C`, `50% humidity`) are used when no overrides exist, but overrides can override these entirely.

>[!WARNING] Clamping Values
> Temperature/humidity values are clamped to realistic ranges (`-50°C` to `60°C` for temp, `0%` to `100%` for humidity) to avoid unrealistic extremes.
