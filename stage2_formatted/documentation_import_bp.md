**Tags:** #Flask, #API, #Database, #Documentation, #World Management, #Card Import, #Subprocess Execution, #JWT Authentication
**Created:** 2026-01-13
**Type:** documentation

# documentation_import_bp

## Summary

```
Flask blueprint for importing and tracking documentation cards from a specified world using enhanced import scripts.
```

## Details

> This code defines a Flask blueprint (`documentation_import`) that handles importing documentation cards into a database from a designated `Documentation` folder. It uses a subprocess to execute an external Python script (`import_documentation_cards_enhanced.py`) to generate cards, leveraging database communication boxes (`WorldReadBox`, `CardReadBox`) for validation and querying. The API includes endpoints for importing documentation (`/import`) and checking import status (`/status`), both secured with JWT authentication.
> 
> The system validates the user’s world ownership before execution, counts created cards post-import, and logs errors. The `/status` endpoint aggregates card counts per world for the authenticated user.

## Key Functions

### ``DocumentationImportAPIBox``

Main class initializing the Flask blueprint and routes.

### ``_register_routes()``

Registers two routes: `/import` (POST) and `/status` (GET).

### ``import_documentation()``

Handles importing documentation cards for a given world ID.

### ``import_status()``

Returns card counts per world for the authenticated user.

## Usage

1. **Import Endpoint (`POST /api/documentation/import`)**:
   - Send a JSON payload with `world_id` (required).
   - Example: `{"world_id": "123"}`
   - Returns success status, card count, and script output on success; errors on failure.

2. **Status Endpoint (`GET /api/documentation/status`)**:
   - Returns a list of user worlds with their respective card counts.

## Dependencies

> ``flask``
> ``flask-jwt-extended``
> ``subprocess``
> ``logging``
> ``request``
> ``jsonify``
> ``models.db``
> ``World``
> ``Card``
> ``WorldReadBox``
> ``CardReadBox``
> ``BoxInput`.`

## Related

- [[backend_database_schema]]
- [[world_card_relationships]]

>[!INFO] External Script Dependency
> The `/import` endpoint relies on `scripts/import_documentation_cards_enhanced.py`. Ensure this script exists and is executable in the `backend` directory.

>[!WARNING] Error Logging
> Critical errors are logged with `exc_info=True`, which may expose stack traces in production. Consider sanitizing logs for sensitive data.
