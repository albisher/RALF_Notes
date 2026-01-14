**Tags:** #data-processing, #filtering, #sorting, #search, #card-management
**Created:** 2026-01-13
**Type:** code-library-module

# card_filtering_box

## Summary

```
Handles card filtering, sorting, and search operations for a card-based system.
```

## Details

> This module extends a `Box` class to provide functionality for filtering, sorting, and searching card data. It processes input parameters like `operation`, `cards`, `filters`, `sortBy`, `sortOrder`, and `searchQuery` to return filtered, sorted, or searched card arrays along with a count. The core logic is encapsulated in private methods like `_filterCards`, `_sortCards`, and `_searchCards`, which handle specific filtering/sorting/search criteria. The `_executeInternal` method orchestrates the workflow based on the requested operation.

## Key Functions

### ``_executeInternal(inputData)``

Orchestrates execution of filtering, sorting, or search operations based on input parameters.

### ``_filterCards(cards, filters)``

Filters cards by type, stage, date range, coordinates, or world ID.

### ``_sortCards(cards, sortBy, sortOrder)``

Sorts cards by date, name, or type in ascending/descending order.

### ``_searchCards(cards, searchQuery, searchFields)``

Performs fuzzy or exact search across specified card fields.

### ``_filterAndSortCards()``

Combines filtering and sorting logic for complex operations.

### ``_parseCardDate(card)``

Helper method to extract and parse card dates (e.g., `created_at` or `date`).

## Usage

1. Instantiate `CardFilteringBox` and call `_executeInternal` with an input object containing:
   - `operation`: `'filter'`, `'sort'`, `'search'`, or `'filterAndSort'`.
   - `cards`: Array of card objects to process.
   - Optional: `filters`, `sortBy`, `sortOrder`, `searchQuery`, `searchFields`.
2. Example:
   ```javascript
   const box = new CardFilteringBox();
   const input = { operation: 'filter', cards: [...], filters: { type: 'A' } };
   const result = await box._executeInternal(input);
   ```

## Dependencies

> ``../core/box_interface.js` (Box class and related utilities like `BoxOutput``
> ``BoxErrorCode``
> `etc.)`

## Related

- [[Card Management System Architecture]]
- [[Data Processing Pipeline]]

>[!INFO] Date Parsing Assumption
> `_parseCardDate` assumes card objects have date fields like `created_at` or `date` (e.g., ISO strings). If parsing fails, the filter/sort logic may return incorrect results.

>[!WARNING] Parallel Execution Risk
> `supportsParallel: true` enables concurrent operations, but unsynchronized calls could lead to race conditions if not managed externally. Validate thread safety in multi-threaded environments.
