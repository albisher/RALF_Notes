**Tags:** #data-processing, #api-integration, #database-migration, #mock-to-real-conversion
**Created:** 2026-01-13
**Type:** code-script

# convert_mock_cards_to_real

## Summary

```
Script converts mock card data from `cards-data.js` into real database entries via API.
```

## Details

> This script reads JSON mock card data from `cards-data.js`, validates it, and sends it to a backend API to create persistent card entries. It checks for existing cards by name before submission to avoid duplicates. The process handles optional fields gracefully and logs progress with success/error counts.

## Key Functions

### `load_mock_cards()`

Extracts and parses the `CARDS_DATA` array from `cards-data.js`.

### `get_world_id()`

Retrieves the world ID from environment variables or API if not provided.

### `convert_card_to_api_format()`

Maps mock card fields (e.g., `name`, `type`, `image`) to API-compatible structures.

### `create_card(world_id, card_data)`

Submits a card to the API and returns success/error status with result ID.

### `main()`

Orchestrates the workflow: loads cards, checks for duplicates, converts, and submits via API.

## Usage

1. Set `API_BASE_URL` and optionally `WORLD_ID` in environment variables.
2. Run the script: `python convert_mock_cards_to_real.py`.
3. Monitor progress in console (skips existing cards, logs errors).

## Dependencies

> ``requests``
> ``json``
> ``os``
> ``sys``
> ``pathlib` (standard libraries)
External: Backend API (`API_BASE_URL` environment variable`
> `typically `http://localhost:5001/api`).`

## Related

- [[cards-data]]
- [[backend-api-docs]]
- [[data-migration-guide]]

>[!INFO] Environment Variables
> Ensure `API_BASE_URL` and `WORLD_ID` are set before execution. If `WORLD_ID` is missing, the script fetches it from the API.

>[!WARNING] Duplicate Handling
> The script skips cards with matching names in the database but does not handle partial name matches or case sensitivity. Verify existing cards manually if duplicates persist.

>[!INFO] Timeout Handling
> API requests have timeouts (10s for checks, 30s for submissions). Adjust if network latency is high.
