**Tags:** #flask, #api, #world-management, #database-operations, #jwt-authentication, #blueprint
**Created:** 2026-01-13
**Type:** documentation

# world_management_bp

## Summary

```
Manages world creation, deletion, listing, and loading via Flask blueprint with JWT authentication.
```

## Details

> This Flask blueprint (`world_management_bp`) encapsulates world management endpoints using a modular design with specialized boxes (`WorldDeletionBox`, `WorldCreationBox`, etc.). It handles CRUD operations for worlds, leveraging a database layer via `BoxInput` for abstraction. Routes include deletion, creation, listing, and loading of worlds, with JWT authentication enforced for security. Error handling and logging are integrated to manage failures gracefully.
> 
> The system processes requests through predefined boxes, ensuring separation of concerns. Each box (`WorldReadBox`, `WorldLoadBox`) abstracts database interactions, simplifying maintenance and extensibility.

## Key Functions

### `WorldManagementAPIBox`

Initializes the blueprint and registers routes for world operations.

### `delete_world`

Deletes a world with optional force flag, returning success/error status.

### `create_world`

Creates a new world with configurable metadata (e.g., `name`, `description`, `user_id`).

### `list_worlds`

Lists worlds filtered by `user_id`, ordered by `created_at`.

### `load_world`

Loads a world’s content (e.g., `cards`, `elements`) with pagination support.

## Usage

1. **Initialize**: Create an instance of `WorldManagementAPIBox`.
2. **Register**: Mount the blueprint in Flask (`app.register_blueprint(box.blueprint)`).
3. **Call Endpoints**:
   - **POST `/create`**: Send JSON payload (e.g., `{"name": "New World"}`).
   - **GET `/<world_id>`**: Delete a world (e.g., `/1`).
   - **GET `/`**: List worlds (authenticated).
   - **GET `/<world_id>/load`**: Load world data (e.g., `/1/load?include=cards`).

## Dependencies

> ``flask``
> ``flask_jwt_extended``
> ``db``
> ``World``
> ``WorldDeletionBox``
> ``WorldCreationBox``
> ``WorldLoadBox``
> ``WorldReadBox``
> ``BoxInput`.`

## Related

- [[`world_deletion_box`]]
- [[`world_creation_box`]]
- [[`world_load_box`]]
- [[`world_read_box`]]
- [[`box_interface`.]]

>[!INFO] JWT Handling
> User identity is extracted via `get_jwt_identity()` and converted to an integer for consistency. Force deletion requires `?force=true`.

>[!WARNING] Database Rollback
> On errors, `db.session.rollback()` is called to undo partial transactions, ensuring data integrity. Always handle exceptions explicitly.
