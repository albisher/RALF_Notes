**Tags:** #browser-console-script, #programmatic-card-generation, #api-integration, #world-building, #randomized-content
**Created:** 2026-01-13
**Type:** code-notes

# create_95_cards_browser

## Summary

```
Generates 95 randomized cards programmatically via browser API for a game world.
```

## Details

> This script dynamically creates 95 unique cards across predefined categories (e.g., plants, robots, locations) by combining random adjectives, nouns, and subtypes. It uses the game’s API to batch-create entries, tracks success/failure, and logs progress. Cards include metadata like coordinates, chapter references, and tags for organization.

## Key Functions

### `create95CardsProgrammatic`

Orchestrates the full card generation loop, validating inputs, batching API calls, and reporting results.

### `CARD_TYPES`

Defines structured categories (e.g., `plants`, `robots`) with subtype lists.

### `ADJECTIVES/NOUNS`

Random word pools for descriptive naming (e.g., "mystical tree").

### `cardData construction`

Builds API payloads with dynamic fields like `card_name`, `description`, and `coordinates`.

## Usage

1. Open browser console on `http://localhost:5174` after logging in.
2. Run `create95CardsProgrammatic()`.
3. Check the Cards tab for generated entries.

## Dependencies

> `window.app?.apiClient`
> `window.app?.currentWorldId (browser environment dependencies)`

## Related

- [[Game API Documentation]]
- [[World-Building Cheat Scripts]]

>[!INFO] Input Validation
> The script checks for `apiClient` and `worldId` existence before proceeding, preventing crashes.

>[!WARNING] Rate Limiting
> Delays (`setTimeout`) between API calls avoid overwhelming the server (20ms per card).

>[!INFO] Error Handling
> Failed cards increment `failed` counter and log errors without halting the loop.
