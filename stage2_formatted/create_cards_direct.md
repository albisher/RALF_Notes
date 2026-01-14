**Tags:** #database-director, #card-creation, #backend-script, #mock-data-processing, #api-bypass
**Created:** 2026-01-13
**Type:** code-notes

# create_cards_direct

## Summary

```
Script directly imports and inserts mock card data into a database, bypassing API authentication.
```

## Details

> This script loads predefined card data from `cards-data.js` and converts it into a database-friendly format. It skips existing cards to avoid duplicates and logs processing progress. The script uses environment variables to fetch a `WORLD_ID` and interacts with a Flask-based backend, leveraging SQLAlchemy for database operations. It handles errors gracefully with rollbacks and exits on failures.

## Key Functions

### `load_mock_cards()`

Extracts and parses JSON data from `cards-data.js` into a Python list of mock cards.

### `convert_card_to_db_format(mock_card, world_id, user_id)`

Transforms mock card data into a `Card` model object with fields like `card_name`, `description`, and `coordinates`.

### `main()`

Orchestrates the workflow: retrieves world/user data, loads cards, checks for duplicates, and inserts valid cards into the database with transaction management.

## Usage

1. Set `WORLD_ID` via environment variable (defaults to `38`).
2. Run the script: `python create_cards_direct.py`.
3. Verify successful insertion in the database by checking the `Card` table for new entries.

## Dependencies

> `Flask (`app`)`
> `SQLAlchemy (`db`)`
> ``models.Card``
> ``models.World``
> ``models.User``
> ``json``
> ``sys``
> ``os``
> ``pathlib.Path`.`

## Related

- [[backend-flask-app]]
- [[cards-data-processing]]
- [[SQLAlchemy-data-model]]

>[!INFO] Environment Dependency
> The script relies on `WORLD_ID` from `os.environ`. Ensure it is set before execution or adjust the default value in the script.

>[!WARNING] Duplicate Handling
> Skipped cards are logged but not removed from the database. If duplicates are critical, modify the script to delete existing records before insertion.
