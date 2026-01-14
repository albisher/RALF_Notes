**Tags:** #flask, #api, #map-processing, #world-management, #json-handling, #file-system, #subprocess
**Created:** 2026-01-13
**Type:** documentation-research

# map_management_bp

## Summary

```
Manages map uploads, validation, processing, and storage for world-specific maps in a Flask-based backend.
```

## Details

> This API box (`MapManagementAPIBox`) handles the lifecycle of map files for a game world, including:
> 1. **Authentication & Validation**: Ensures the user owns the world and validates file inputs (e.g., JSON extension).
> 2. **Storage**: Saves raw and processed maps in a world-specific directory with timestamps.
> 3. **Conditional Processing**: Skips processing if the map already contains derived metadata (e.g., `derivedInfo`).
> 4. **Script Integration**: Uses an external Python script (`process_map_data.py`) to transform raw maps into processed formats via `subprocess`.
> 
> Key workflows:
> - Upload → Validate → Store → Process (if needed) → Return confirmation.

## Key Functions

### ``upload_map()``

Endpoint for POST requests to `/api/maps/upload`. Validates user/world, checks file, and orchestrates storage/processing.

### ``_register_routes()``

Dynamically registers the `/api/maps/upload` route with Flask’s Blueprint.

### ``process_map_data.py``

External script (called via `subprocess`) that converts raw JSON maps into processed formats (e.g., Azgaar-specific metadata).

## Usage

1. **Call**: `POST /api/maps/upload` with:
   - `world_id` (required) and `map_file` (JSON file).
   - JWT token for authentication.
2. **Response**: JSON payload confirming success/error (e.g., `{"error": "Map processing script not found"}`).

## Dependencies

> `Flask`
> `Flask-JWT-Extended`
> `SQLAlchemy (via `models.db`)`
> ``subprocess``
> ``json``
> ``os``
> ``datetime``
> ``logging`.`

## Related

- [[Flask-JWT-Extended Documentation]]
- [[SQLAlchemy Core]]
- [[process_map_data]]

>[!INFO] File Naming Convention
> Raw maps use `{world_name}_raw_{timestamp}.json`, processed maps use `{world_name}_map_{timestamp}.json`. Replace spaces in `world.name` with underscores to avoid path conflicts.

>[!WARNING] Script Dependency
> If `process_map_data.py` fails to locate, the API returns a 500 error. Ensure all paths in `possible_paths` are correct (e.g., Docker container paths). Test with `os.getcwd()` logging to debug.
