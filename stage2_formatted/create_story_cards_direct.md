**Tags:** #database-script, #story-generation, #bulk-data-creation, #world-building, #card-game
**Created:** 2026-01-13
**Type:** code-script

# create_story_cards_direct

## Summary

```
Generates 100+ randomized story cards directly in a database for a world-building system, bypassing API for efficiency.
```

## Details

> This script creates a predefined number of story cards (default: 105) with randomized attributes such as type, subtype, name, description, and metadata. It interacts with a database to store cards in a structured `Card` model, linking them to a pre-existing or dynamically created `World` and `User`. The script leverages predefined lists of adjectives, nouns, and card subtypes to generate varied content. It batches commits every 20 cards for efficiency and provides a summary of created cards by type.

## Key Functions

### `generate_hash(prefix)`

Generates a random 16-character hash string prefixed with a given value.

### `create_story_cards(count=105)`

Core function that:

## Usage

1. Run the script directly (`python create_story_cards_direct.py`).
2. Ensure the backend directory is in the Python path.
3. The script will:
   - Check/create a user with username 'a'.
   - Check/create a world named "Story World - 100 Cards Test".
   - Generate and commit 105 story cards with randomized attributes.
   - Print a summary of created cards by type.

## Dependencies

> ``app``
> ``db``
> ``User``
> ``World``
> ``Card` (SQLAlchemy models)`
> ``random``
> ``string``
> ``datetime``
> ``sys``
> ``os` (standard libraries).`

## Related

- [[app]]
- [[models]]

>[!INFO] Important Note
> The script uses a hardcoded user (`username='a'`) and world name. Modify these values if needed for integration with other systems.

>[!WARNING] Caution
> Direct database operations may cause conflicts if the world or user already exists. The script checks for existence but does not handle concurrent modifications gracefully. Consider transaction rollback logic for production use.
