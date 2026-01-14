**Tags:** #automation, #storytelling, #api-integration, #browser-script, #data-generation
**Created:** 2026-01-13
**Type:** code-script

# BROWSER_CARD_CREATION_SCRIPT

## Summary

```
Generates 100+ randomized story cards via browser console for a narrative-driven application.
```

## Details

> This script dynamically creates 105 story cards (100+ core) using predefined categories (e.g., plants, robots, locations) and combines them with random adjectives/nouns. It fetches an API client and world ID from the app context, then batches card creation with progress logging every 20 cards. Each card includes metadata like power level, rarity, coordinates, and chapter references. Failures are tracked for debugging.

## Key Functions

### `create100StoryCards`

Orchestrates the entire card generation loop, validating inputs, processing 105 iterations, and logging progress.

### `CARD_TYPES`

Structured object mapping card categories (e.g., `plants: ['tree', 'flower']`) to generate subtype diversity.

### `ADJECTIVES/NOUNS`

Random word pools for generating descriptive card names (e.g., "Ancient Temple").

### `cardData construction`

Builds a standardized payload for API submission with dynamic attributes like `power_level` or `significance`.

## Usage

1. Run in browser console after logging into the app (localhost:5174).
2. Paste and execute the script; it logs progress every 20 cards.
3. Verify results in the "Cards" tab after completion.

## Dependencies

> ``window.app?.apiClient``
> ``window.app?.currentWorldId` (browser context)`
> `no external libraries.`

## Related

- [[Storycard API Documentation]]
- [[World Management Guide]]

>[!INFO] Input Validation
> The script checks for `apiClient` and `worldId` existence before proceeding, preventing runtime errors.

>[!WARNING] Rate Limiting
> A 30ms delay between requests mitigates server overload, but excessive delays may impact performance.
