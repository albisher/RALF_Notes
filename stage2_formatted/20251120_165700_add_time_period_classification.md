**Tags:** #database-migration, #alembic, #sqlalchemy, #timeline-classification, #postgresql
**Created:** 2026-01-13
**Type:** documentation

# 20251120_165700_add_time_period_classification

## Summary

```
Adds a `time_period_classification` column and `era_metadata` JSONB field to timelines and timeline events tables for categorizing historical periods.
```

## Details

> This migration script enhances a timeline database by introducing a `time_period_classification` field (string, max 50 chars) and a `era_metadata` JSONB column (PostgreSQL) to categorize time periods. The `time_period_classification` is initially set to `'imaginary'` as a default, while `era_metadata` defaults to an empty JSON object. The script also propagates classifications from timelines to their associated events via SQL updates. The downgrade reverses these changes by dropping the columns.

## Key Functions

### `upgrade()`

Executes Alembic’s migration steps to add columns and populate default values.

### `downgrade()`

Reverts changes by dropping the added columns.

## Usage

Run via Alembic command:
```bash
alembic upgrade head
```
To revert:
```bash
alembic downgrade head
```

## Dependencies

> ``alembic``
> ``sqlalchemy``
> ``sqlalchemy.dialects.postgresql``

## Related

- [[20251120_165629]]
- [[database_schema_timeline]]

>[!INFO] Default Values
> `time_period_classification` defaults to `'imaginary'` for backward compatibility, while `era_metadata` defaults to `{}` (empty JSON). This ensures existing records are preserved during migration.

>[!WARNING] Null Handling
> Null values in `timelines.time_period_classification` are explicitly set to `'imaginary'` to avoid data loss. Events inherit classifications via a correlated subquery, which may fail if `timelines.id` references non-existent records.
