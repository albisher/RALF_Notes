**Tags:** #database-migration, #alembic, #sqlalchemy, #weather-system, #jsonb, #postgresql
**Created:** 2026-01-13
**Type:** documentation

# 20251120_170100_add_weather_system

## Summary

```
Adds a weather system to a game/world database by extending the `worlds` table with weather conditions and introducing a dedicated `weathers` table for dynamic weather data.
```

## Details

> This migration script uses Alembic to extend a game/world database by:
> 1. Adding a `weather_conditions` JSONB column to the `worlds` table (defaulting to an empty JSON object `{}`).
> 2. Creating a new `weathers` table to store dynamic weather data (e.g., temperature, humidity, weather types) linked to `worlds`, `users`, and optional `locations` via foreign keys.
> 3. Adding an index on `location_id` and `timestamp` for optimized query performance.
> 
> The `weather_conditions` field in `worlds` allows storing static weather metadata (e.g., default values), while the `weathers` table tracks real-time or event-driven weather changes.

## Key Functions

### ``upgrade()``

Applies the migration by:

### ``downgrade()``

Reverts the changes by:

## Usage

To apply this migration:
1. Run `alembic upgrade head` in the project directory.
2. The database will now support weather systems via:
   - Static weather data in `worlds.weather_conditions`.
   - Dynamic entries in the `weathers` table (e.g., for events, user modifications).

## Dependencies

> `- `alembic``
> ``sqlalchemy``
> ``sqlalchemy.dialects.postgresql` (for JSONB support).`

## Related

- [[None]]

>[!INFO] Default JSONB Behavior
> The `weather_conditions` column defaults to `{}`, allowing empty weather metadata. If no data is provided, the field will be `null` unless explicitly set.

>[!WARNING] Foreign Key Constraints
> `location_id` in `weathers` references `cards.id` (ondelete=SET NULL), so orphaned locations will not break the table. Ensure `world_id` and `user_id` exist in `worlds` and `users` tables before running this migration.
