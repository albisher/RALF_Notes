**Tags:** #browser-console-script, #card-generation, #programmatic-ui, #api-integration, #world-management
**Created:** 2026-01-13
**Type:** code-notes

# create_100_cards_complete

## Summary

```
Generates 100 cards (95 programmatically + 5 via UI-style) for a world in a browser console using an API client.
```

## Details

> This script automates the creation of fantasy-themed cards by dynamically selecting types (e.g., plants, robots) and combining them with adjectives/nouns for names. It uses an API client (`window.app?.apiClient`) to batch-create cards with metadata like coordinates (every 3rd card) and structured references. The script splits work into two phases: 95 programmatic cards (with chapter tracking) and 5 UI-style cards (simulating manual UI generation). Error handling logs failures, and delays prevent API overload.

## Key Functions

### `create100CardsComplete`

Orchestrates the full 100-card generation workflow.

### `CARD_TYPES`

Defines predefined categories (e.g., `plants`, `robots`) with sub-types (e.g., `tree`, `combat-robot`).

### `ADJECTIVES/NOUNS`

Dynamic name components for card titles (e.g., `ancient tree`).

### `cardData construction`

Builds structured API payloads with metadata like `hash_value`, `liked_hash_references`, and `coordinates`.

## Usage

1. Open browser console on `http://localhost:5174` after logging in.
2. Run `create100CardsComplete()`.
3. Verify success via console logs (e.g., `✅ Created 95/95 programmatic cards`).

## Dependencies

> ``window.app?.apiClient``
> ``window.app?.currentWorldId``
> ``window.app?.currentUser?.id` (browser context dependencies).`

## Related

- [[None]]

>[!INFO] Preconditions Check
> Ensure `window.app` exists and has `apiClient`, `currentWorldId`, and `currentUser?.id` populated.

>[!WARNING] Rate Limiting
> Delays (100ms every 10 cards) mitigate API overload; avoid rapid execution.
