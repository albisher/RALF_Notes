**Tags:** #card-generation, #random-data-creation, #api-integration, #testing-script, #world-management
**Created:** 2026-01-13
**Type:** code-notes

# create_100_cards

## Summary

```
Generates 100+ randomized narrative cards for testing purposes in a game/application API.
```

## Details

> This script dynamically creates 100+ unique cards (e.g., plants, buildings, characters) with randomized names, descriptions, attributes, and coordinates. It uses predefined lists of adjectives, nouns, and card types to craft varied entries. Each card is sent to an API (`cards.create`) with structured metadata, including rarity, power level, and chapter association. The script includes error handling and progress logging to track success/failure rates.

## Key Functions

### `create100Cards`

Main async function that loops 100 times, generating and submitting cards via API.

### `cardData construction`

Combines randomized adjectives/nouns into names and populates attributes (e.g., `power_level`, `rarity`) with randomized values.

### `Progress tracking`

Logs every 10 cards and reports final success/failure counts.

## Usage

1. Run in browser console on `http://localhost:5174` (or similar).
2. Replace `currentWorldId` (default: 42) if testing a different world.
3. Refresh the "cards" tab to view results.

## Dependencies

> `window.app.apiClient`
> `window.api (browser-based API client)`
> `Node.js module system (for export).`

## Related

- [[Card API Documentation]]
- [[Game World Setup Guide]]

>[!INFO] Default World
> Uses `42` (Zephyros Prime) as the default `currentWorldId`. Override this value if testing a different world.

>[!WARNING] Rate Limiting
> A 50ms delay between submissions avoids server overload. Adjust if needed for high-volume testing.
