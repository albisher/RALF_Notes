**Tags:** #card-system, #game-design, #data-structure, #configuration, #type-definition
**Created:** 2026-01-13
**Type:** code-notes

# card-types

## Summary

```
Defines and organizes card types with metadata for a game/application, ensuring consistent categorization and visual representation.
```

## Details

> This file centralizes all card types in a structured object (`CARD_TYPES`), defining properties like `id`, `label`, `icon`, `color`, and `category` for each type. The configuration ensures consistency across the application by standardizing how cards are identified, displayed, and categorized. The file also provides utility functions to retrieve, validate, and group card types by their predefined categories.

## Key Functions

### `getAllCardTypeIds()`

Returns an array of all card type IDs and plural forms.

### `getCardType(typeId)`

Retrieves a card type object by its ID (supports both singular and plural matches).

### `getCardIcon(typeId)`

Returns the icon associated with a card type ID.

### `getCardColor(typeId)`

Returns the color associated with a card type ID.

### `isValidCardType(typeId)`

Checks if a provided ID corresponds to a valid card type.

### `getCardTypesByCategory()`

Groups card types into their predefined categories (e.g., `entity`, `creature`, `object`).

## Usage

1. Import `CARD_TYPES` to access predefined card definitions.
2. Use utility functions like `getCardType()`, `getCardIcon()`, or `getCardTypesByCategory()` to dynamically fetch or categorize card data.
3. Validate IDs with `isValidCardType()` before processing.

## Dependencies

> `React icons (for icon rendering)`
> `none explicitly listed in this file.`

## Related

- [[game-card-system-config]]
- [[card-display-components]]

>[!INFO] **Category Consistency**
> Card types are grouped into logical categories (e.g., `entity`, `creature`, `object`) to facilitate filtering and UI organization. Overlapping categories (e.g., `HUMAN` and `CHARACTER` share the same `id` and `icon`) are intentionally designed for thematic clarity.

>[!WARNING] **ID Normalization**
> The `getCardType()` function normalizes IDs to lowercase for case-insensitive matching. Ensure IDs are lowercase when passed to avoid mismatches.
