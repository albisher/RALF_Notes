**Tags:** #API-integration, #data-processing, #world-generation, #mock-to-real-conversion
**Created:** 2026-01-13
**Type:** code-script

# create_world_and_convert_cards

## Summary

```
Script automates world creation and converts mock card data into API-compatible cards for a game/environment system.
```

## Details

> This script orchestrates two primary tasks: creating a new world in an API backend and converting mock card data (from `cards-data.js`) into API-compatible formats. It first attempts to authenticate via a test user, then creates a world with configurable metadata (e.g., `WORLD_NAME`). Mock cards are parsed from a JSON array in `cards-data.js`, transformed into API-standard formats, and sent to the backend to generate real cards. Error handling is included for authentication, file loading, and API requests.

## Key Functions

### `create_test_user()`

Attempts to register/login a test user to obtain an auth token for API access.

### `create_world(token)`

Creates a new world in the API using the provided token, or retrieves an existing one by name.

### `load_mock_cards()`

Extracts and parses JSON data from `cards-data.js` to load mock card definitions.

### `convert_card_to_api_format(mock_card)`

Maps mock card attributes (e.g., `name`, `image`) to API-compatible fields (e.g., `card_name`, `image_url`).

### `create_card(world_id, card_data, token)`

Sends a card payload to the API to create a new card entry in the specified world.

## Usage

1. Set `API_BASE_URL` and `WORLD_NAME` via environment variables (defaults to `localhost:5001` and `Space Peral`).
2. Run the script to:
   - Authenticate (register/login a test user).
   - Create a world (or retrieve an existing one).
   - Load mock cards from `ui-beta/data/cards-data.js`.
   - Convert each mock card to API format and create corresponding cards in the world.
3. Handle failures gracefully (e.g., missing files, API errors).

## Dependencies

> `requests`
> `json`
> `sys`
> `os`
> `pathlib`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes `cards-data.js` contains a `CARDS_DATA` array in JSON format. If the file structure differs, parsing may fail.

>[!WARNING] Caution
> Hardcoded credentials (`testuser/testpass123`) are used for testing. Avoid committing credentials in production. The script does not validate API responses for critical fields (e.g., `success` status).
