**Tags:** #database-migration, #world-hierarchy, #json-storage, #foreign-key
**Created:** 2026-01-13
**Type:** documentation

# 20251120_165629_add_world_flexibility_fields

## Summary

```
Adds flexible fields to the `worlds` table for hierarchical parent-child relationships, metadata storage, and celestial object tracking.
```

## Details

> This migration script extends the `worlds` table by introducing three new columns:
> 1. **`parent_world_id`** – Establishes a hierarchical relationship (e.g., universe → solar system → planet) via a foreign key.
> 2. **`world_metadata`** – Stores JSONB-formatted world-specific configurations (e.g., custom settings, flags).
> 3. **`celestial_objects`** – Captures JSONB data for celestial bodies (e.g., stars, moons) influencing weather/environment.
> 
> The `world_type` column (already present) remains for validation at the application layer, not the database.

## Key Functions

### ``upgrade()``

Executes Alembic’s `add_column` and `create_foreign_key` to add/modify columns.

### ``downgrade()``

Reverts changes by dropping constraints and columns in reverse order.

## Usage

Apply via Alembic:
```bash
alembic upgrade head
```
For downgrading:
```bash
alembic downgrade head
```

## Dependencies

> ``alembic``
> ``sqlalchemy``
> ``sqlalchemy.dialects.postgresql``

## Related

- [[`cecdde0e47cd`]]
- [[`worlds_table_schema`]]

>[!INFO] Hierarchy Note
> `parent_world_id` enforces a tree structure (e.g., `universe` → `solar_system` → `planet`). Nullable values allow root nodes (e.g., universes) without parents.

>[!WARNING] JSONB Caution
> Ensure application logic validates `world_metadata`/`celestial_objects` to prevent malformed JSON or unintended behavior. Defaults (`{}`) are safe but may not reflect real-world data.
