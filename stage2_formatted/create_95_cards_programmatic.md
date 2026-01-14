**Tags:** #backend-api, #programmatic-card-generation, #game-dev, #data-structures, #randomization
**Created:** 2026-01-13
**Type:** code-notes

# create_95_cards_programmatic

## Summary

```
Generates 95 unique cards programmatically via backend API using predefined categories, adjectives, and nouns.
```

## Details

> This script programmatically creates 95 unique cards by combining random adjectives, nouns, and predefined card subtypes (e.g., "tree," "temple") from structured data arrays (`CARD_TYPES`, `ADJECTIVES`, `NOUNS`). It first authenticates with a backend API, selects or creates a world, then iterates to generate each card with metadata like `power_level`, `rarity`, and `chapter`. The `generateHash` function ensures uniqueness via timestamp and randomness. The script logs success/failure for each card creation and tracks progress.

## Key Functions

### `login`

Authenticates with the backend API using provided credentials.

### `getOrCreateWorld`

Finds or creates a world (defaulting to "Zephyros Prime" or a new world named "Story World - 95 Cards").

### `createCard`

Sends a POST request to the backend API to create a single card with structured payload.

### `create95Cards`

Orchestrates the full process: authentication, world setup, and iterative card generation (95 total), with error handling and progress tracking.

### `getRandomElement`

Helper to randomly select an element from an array.

### `generateHash`

Generates a unique identifier for each card using timestamp, index, and randomness.

## Usage

1. Set `BACKEND_URL`, `USERNAME`, and `PASSWORD` in environment variables or override defaults.
2. Run the script to authenticate, create a world, and generate 95 cards programmatically.
3. Cards are stored in the backend API under the selected world.

## Dependencies

> `axios`
> `process.env (Node.js environment variables)`

## Related

- [[None]]

>[!INFO] Authentication Fallback
> If environment variables are not set, defaults (`USERNAME: 'a'`, `PASSWORD: 'spq8'`) are used. Hardcoded credentials are insecure; use environment variables in production.

>[!WARNING] Backend Dependency
> The script assumes the backend API exists at `http://localhost:5000` and supports `/api/auth/login`, `/api/worlds`, and `/api/cards` endpoints. Verify API compatibility before use.
