**Tags:** #programmatic-card-generation, #ui-card-creation, #automation-script, #data-entry, #workflow-integration
**Created:** 2026-01-13
**Type:** documentation

# CARD_CREATION_INSTRUCTIONS

## Summary

```
Instructions for creating 100 cards via a mix of automated script and manual UI input.
```

## Details

> This document outlines a two-step process to generate 100 cards: 95 programmatically via a JavaScript script executed in the browser console, and 5 manually through the UI’s Generate Stage feature. The script automates the creation of diverse card types with metadata, while the manual step allows customization via a UI interface. The workflow ensures all cards are verified in the Cards tab, confirming correct functionality and representation.

## Key Functions

### `create95CardsProgrammatic()`

Executes the automated script to generate 95 cards with predefined attributes (types, names, descriptions, coordinates, tags).

### `Generate Stage UI`

Manually creates 5 cards via a UI workflow with hash-based generation and dropdown selection.

### `Browser Console Script (create_95_cards_browser.js)`

Contains logic to programmatically fetch/create cards with structured metadata.

## Usage

1. **Programmatic Step**:
   - Access `http://localhost:5174`, log in, open console, paste `create_95_cards_browser.js`, and run `create95CardsProgrammatic()`.
   - Wait for completion (~2-3 minutes) and verify progress in console.

2. **Manual Step**:
   - Navigate to Generate Stage, select a world, and manually generate 5 cards using the recommended generator types.
   - Save each card and verify success messages.

3. **Verification**:
   - Check the Cards tab for 100 cards, verify counts/types, and test UI functionality (search, filters, modal, edit/delete).

## Dependencies

> `- Browser-based frontend application (React-based`
> `running on `localhost:5174`).
- JavaScript runtime environment (Chrome/Firefox console).
- UI components: Login credentials (`a/spq8`)`
> `Generate Stage button`
> `Cards tab.`

## Related

- [[Card_Management_System_Architecture]]
- [[UI_Workflow_Documentation]]

>[!INFO] Important Note
> The script assumes the backend API supports dynamic card creation with metadata fields (e.g., coordinates, tags). If missing, adjust script to match API constraints.


>[!WARNING] Caution
> Manual card creation may conflict with programmatically generated cards if hashes overlap. Ensure unique hashes are used for UI-generated cards to avoid duplicates.
