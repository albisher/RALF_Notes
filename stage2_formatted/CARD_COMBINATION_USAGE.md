**Tags:** #programmatic-api, #vue-js, #local-storage, #card-management, #data-structures, #workflow-integration
**Created:** 2026-01-13
**Type:** documentation

# CARD_COMBINATION_USAGE

## Summary

```
Explains how to programmatically use hidden card combination features (page and history book creation) via browser console or integration into workflows.
```

## Details

> This document details the programmatic usage of hidden card combination features in a card viewer application, allowing users to combine cards into pages and pages into history books without direct UI interaction. The features are exposed via a Vue.js application instance, enabling dynamic selection, creation, and management of pages and history books stored in `localStorage`. The workflow supports exporting history books as JSON files and integrates with other applications like timeline-story workflows.

## Key Functions

### ``toggleCardForPage(cardId)``

Toggles card selection for page creation.

### ``createPage()``

Creates a named page from selected cards.

### ``createHistoryBook()``

Creates a named history book from selected pages.

### ``selectedCardsForPage``

Stores IDs of selected cards for page creation.

### ``pages``

Array of all created pages, stored in `localStorage`.

### ``historyBooks``

Array of all created history books, stored in `localStorage`.

### ``exportHistoryBook(book)``

Exports a history book as a JSON file.

## Usage

1. Access the Vue app instance via `#app` or `window` (if exposed).
2. Select cards using `toggleCardForPage()` or set `selectedCardsForPage` directly.
3. Define a page name (`currentPageName`) and call `createPage()`.
4. Select pages for a history book, set a name (`currentHistoryBookName`), and call `createHistoryBook()`.
5. Export history books using `exportHistoryBook()` or auto-export on creation.

## Dependencies

> `Vue.js`
> `browser DOM APIs (for console access)`
> ``localStorage` (for persistence).`

## Related

- [[Card Viewer Implementation]]
- [[Timeline-Story Workflow Integration]]

>[!INFO] Persistence Note
> Pages and history books are automatically saved to `localStorage` under keys `cardview-pages` and `cardview-history-books`, respectively. This ensures data retention across sessions.

>[!WARNING] UI Disabled
> The UI for page and history book creation is intentionally hidden. Users must rely on programmatic calls to `createPage()` and `createHistoryBook()` for functionality.
