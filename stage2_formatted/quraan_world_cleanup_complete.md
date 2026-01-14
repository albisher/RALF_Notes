**Tags:** #database_cleanup, #quran_world, #data_management, #duplicate_removal, #metadata_update
**Created:** 2026-01-14
**Type:** documentation

# quraan_world_cleanup_complete

## Summary

```
A comprehensive cleanup of the Quraan World database to ensure data integrity, eliminate duplicates, and standardize metadata.
```

## Details

> This script performed a complete cleanup of the Quraan World database by removing duplicate entries, ensuring all cards have accurate timestamps, and updating map metadata. The process retained only the most recent complete versions of each card, verified all historical data, and validated geographic and temporal consistency within the dataset.

## Key Functions

### ``cleanup_quraan_world.py``

Main script that identifies and removes duplicates, fixes missing timestamps, and updates metadata.

### `Duplicate Removal Logic`

Retains the highest-ID version of each card with a timestamp, discarding older incomplete entries.

### `Timestamp Validation`

Ensures all cards have timestamps within the historical range (555–632 CE) by cross-referencing with known events.

### `Metadata Update`

Integrates map file references (`quraan_map.json`) into the `world_metadata` JSONB field for the Quraan world entry.

## Usage

Execute via Docker Compose:
```bash
docker-compose exec backend python3 /app/scripts/cleanup_quraan_world.py
```
The script runs automatically in a backend container, requiring no manual intervention post-execution.

## Dependencies

> ``docker-compose``
> ``python3``
> ``json` (built-in)`
> ``scripts/cleanup_quraan_world.py` (internal script)`
> ``ui-beta/data/quraan_map.json``
> ``ui-beta/maps/quraan_map.json`.`

## Related

- [[`Quraan World Database Structure`]]
- [[`Cleanup Script Documentation`]]
- [[`Database Migration Guide`.]]

>[!INFO] Critical Validation
> All 27 remaining cards now include timestamps, coordinates, and source links, ensuring compatibility with frontend timeline and map rendering.

>[!WARNING] Historical Accuracy
> Timestamp ranges (e.g., Khadijah’s birth in 555 CE) rely on verified historical records; incorrect assumptions could skew temporal analysis. Verify source dates before deployment.
