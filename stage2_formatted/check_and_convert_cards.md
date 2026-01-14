**Tags:** #card-conversion, #data-migration, #api-integration, #mock-to-real
**Created:** 2026-01-13
**Type:** code-notes

# check_and_convert_cards

## Summary

```
Checks existing game cards against mock data and flags missing cards for conversion.
```

## Details

> This script compares real cards in a database with mock cards stored in `cards-data.js`. It retrieves all worlds and their associated cards from an API, then loads mock card data from a JavaScript file. If the count of real cards is less than the mock count, it identifies missing cards and suggests running a separate conversion script.
> 
> The workflow involves:
> 1. Fetching all worlds from the API.
> 2. For each world, fetching its cards.
> 3. Loading mock cards from `cards-data.js`.
> 4. Comparing counts to detect missing cards.
> 5. Outputting results and suggesting conversion if needed.

## Key Functions

### `get_worlds()`

Fetches all available worlds from the API.

### `get_cards(world_id)`

Retrieves cards for a specific world using the API.

### `load_mock_cards()`

Parses mock card data from `cards-data.js` and returns it as a JSON array.

### `main()`

Orchestrates the comparison logic, prints results, and guides the user on conversion.

## Usage

1. Run the script to check for missing cards:
   ```bash
   python3 check_and_convert_cards.py
   ```
2. If missing cards are detected, execute the conversion script with the first world ID:
   ```bash
   WORLD_ID=<world_id> python3 scripts/convert_mock_cards_to_real.py
   ```

## Dependencies

> `requests`
> `json`
> `sys`
> `os`
> `pathlib`

## Related

- [[convert_mock_cards_to_real]]
- [[API Documentation]]

>[!INFO] Important Note
> The script assumes `cards-data.js` is located at `ui-beta/data/cards-data.js`. If the path is incorrect, it will fail to load mock cards.
>

>[!WARNING] Caution
> If the API or `cards-data.js` is modified, the script may produce incorrect results. Always verify the data before running conversion.
