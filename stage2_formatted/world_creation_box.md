**Tags:** #database, #world-generation, #hierarchy-validation, #user-authentication, #error-handling
**Created:** 2026-01-13
**Type:** code-notes

# world_creation_box

## Summary

```
Handles creation of new worlds with validation, hierarchy checks, and metadata support.
```

## Details

> This `WorldCreationBox` class implements a modular box for creating new worlds within a system. It validates inputs (e.g., required fields like `name` and `user_id`), enforces hierarchical relationships between world types (e.g., a `planet` can only be a child of a `solar_system`), and ensures uniqueness by checking for duplicate names per user. It also manages default world selection by unsetting existing defaults when a new one is set. The box interacts with a database (`World` model) to persist created worlds.

## Key Functions

### ``execute(input_data`

BoxInput) -> BoxOutput`**: Orchestrates world creation, validation, and database operations.

### ``World` model`

Database class representing a world entity with attributes like `name`, `world_type`, `parent_world_id`, and metadata.

### ``hierarchy_rules` dictionary`

Defines allowed child world types for each parent type (e.g., `universe` can only contain `solar_system`).

### ``db.session``

SQLAlchemy session for database operations (add/commit).

## Usage

1. Instantiate `WorldCreationBox` (e.g., `box = WorldCreationBox()`).
2. Pass input data (e.g., `{'name': "Earth", 'user_id': 123}`) via `box.execute()`.
3. Handle output (`BoxOutput`) to check success/failure and retrieve the created world.

## Dependencies

> ``..core.box_interface``
> ``models.db``
> ``models.World``
> ``logging``
> ``typing``

## Related

- [[`core]]
- [[`models]]
- [[`models]]

>[!INFO] Required Fields
> Mandatory fields (`name`, `user_id`) must be provided; omitting them returns an error.

>[!WARNING] Hierarchy Validation
> If `parent_world_id` is set, the `world_type` must match the allowed children for that parent type; otherwise, validation fails.

>[!INFO] Default World Logic
> Setting `is_default=True` automatically deactivates other default worlds for the same user.
