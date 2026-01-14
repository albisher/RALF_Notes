**Tags:** #database-schema, #time-system, #biomes, #solar-system, #planets, #world-generation, #PostgreSQL, #JSONB, #flexible-configuration
**Created:** 2026-01-13
**Type:** documentation

# 2025-08-16_world-database-schema-timesystem-biomes-solar-syst

## Summary

```
Designs a flexible PostgreSQL schema for a world database, integrating time systems, biomes, solar systems, and planetary data with JSONB for dynamic configurations.
```

## Details

> The schema leverages PostgreSQL’s `JSONB` for flexible metadata storage while normalizing frequently queried attributes into dedicated columns. It organizes entities like `TimeSystem`, `Biomes`, `SolarSystem`, and `Planets` as specialized `WorldElement` types or separate tables, linked via foreign keys. Core logic includes balancing normalization for performance with JSONB for evolving configurations (e.g., biome attributes, leap year rules). The design supports extensibility for AI-generated elements like plants and technology.

## Key Functions

### `TimeSystem`

Manages configurable time parameters (e.g., `days_per_year`, `hours_per_day`) via JSONB for complex rules.

### `Biome`

Stores environmental properties (temperature, humidity, flora/fauna) with flexible JSONB fields for dynamic data.

### `SolarSystem`

Tracks star type and planet count with foreign key links to `Planets`.

### `Planet`

Contains orbital/rotation data, biome references, and atmosphere metadata in JSONB.

### `WorldElement`

Base class extending `World` with JSONB for metadata, enabling modular schema evolution.

## Usage

1. Extend `WorldElement` with new types (e.g., `TimeSystem`, `Biome`) using SQLAlchemy.
2. Use `data_jsonb` for nested configurations (e.g., biome attributes).
3. Normalize critical fields (e.g., `orbital_period`) for indexing.
4. Apply Alembic migrations to evolve schema incrementally.
5. Validate data integrity via application-layer constraints (e.g., `days_per_year > 0`).

## Dependencies

> `PostgreSQL`
> `SQLAlchemy (for ORM)`
> `Alembic (for migrations)`
> `JSONB extension.`

## Related

- [[PostgreSQL JSONB Guide]]
- [[SQLAlchemy Core Documentation]]
- [[Alembic Migration Guide]]

>[!INFO] JSONB Advantage
> JSONB allows dynamic field additions (e.g., `atmosphere` in `Planet`) without schema migrations, ideal for evolving world data.

>[!WARNING] Normalization Tradeoff
> Over-normalization reduces flexibility; use JSONB for highly variable data (e.g., biome rules) to avoid rigid schema changes.
