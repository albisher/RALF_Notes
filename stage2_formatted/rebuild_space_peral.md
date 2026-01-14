**Tags:** #database, #world-management, #documentation-import, #scripting, #OOP
**Created:** 2026-01-13
**Type:** code-script

# rebuild_space_peral

## Summary

```
Script automates rebuilding a Space Peral world by deleting existing data, recreating it, and importing documentation cards.
```

## Details

> This script leverages an application context to interact with a database-driven world management system. It first locates a test user, checks for an existing "Space Peral" world, and deletes it if present. After creating a new world with specified attributes (colony type, active status), it imports all documentation cards into the newly created world. The script uses a modular approach with custom boxes (e.g., `WorldCreationBox`, `WorldDeletionBox`) for database operations and dynamically imports a separate module for importing documentation cards.

## Key Functions

### ``rebuild_space_peral()``

Orchestrates the entire workflow: deletion, recreation, and documentation import.

### ``WorldCreationBox.execute()``

Creates a new world with configurable metadata (name, description, type, etc.).

### ``WorldDeletionBox.execute()``

Safely removes an existing world and its associated data (cards, elements, timelines).

### ``import_docs.import_documentation()``

Dynamically imported module function to batch-import documentation cards into the world.

### ``BoxInput``

Container class for passing structured data to box operations.

## Usage

1. Run the script directly (`python rebuild_space_peral.py`).
2. It assumes a test user (`testuser`) exists in the system.
3. The script will:
   - Delete the existing "Space Peral" world (if found).
   - Create a new one with default settings.
   - Import all documentation cards from a separate module.
4. Outputs success/failure messages and final card counts.

## Dependencies

> ``app``
> ``db``
> ``World``
> ``User``
> ``Card` (SQLAlchemy models)`
> ``WorldCreationBox``
> ``WorldDeletionBox``
> ``BoxInput` (custom modules)`
> ``importlib` (Python standard library).`

## Related

- [[`app]]
- [[`models]]
- [[`import_documentation_cards_enhanced]]
- [[`boxes.worlds]]
- [[`boxes.worlds.world_deletion_box`.]]

>[!INFO] Important Note
> The script uses `app.app_context()` to ensure database operations run in a transactional context. If the user or world does not exist, it exits early with an error.
>

>[!WARNING] Caution
> Force deletion (`force=False`) is used to avoid accidental data loss. If the import fails, the script logs the error and exits, preserving the world state.
