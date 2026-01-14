**Tags:** #Vue.js, #Pinia, #State Management, #API Service, #Computed Properties, #Filtering & Sorting, #CRUD Operations
**Created:** 2026-01-13
**Type:** documentation

# elements

## Summary

```
Manages element data with filtering, sorting, and CRUD operations using Pinia and Vue.
```

## Details

> This Pinia store handles a collection of elements, including state management for elements, filters, loading states, and errors. It provides computed properties for filtered results, available types, and basic element metadata. The store interacts with an external API service (`apiService`) for fetching, creating, updating, and deleting elements, while maintaining a `currentElement` reference and dynamic filtering/sorting capabilities.

## Key Functions

### ``fetchElements``

Asynchronously retrieves all elements from the API and updates the store.

### ``fetchElement``

Asynchronously fetches a single element by ID and updates `currentElement`.

### ``createElement``

Asynchronously creates a new element via the API and appends it to `elements`.

### ``updateElement``

Asynchronously updates an existing element, modifies the local store, and updates `currentElement` if applicable.

### ``deleteElement``

Asynchronously deletes an element by ID and removes it from `elements`.

### ``filteredElements``

Computed property applying search, type, and sorting filters to `elements`.

### ``elementTypes``

Computed property returning a sorted list of unique element types.

### ``setFilters``

Updates filter settings (e.g., search term, sort order) immutably.

### ``clearFilters``

Resets all filters to defaults.

### ``setCurrentElement``

Sets the `currentElement` reference to a specific element.

### ``clearError``

Resets the error state.

## Usage

1. **Initialize**: Import and use the store in a Vue component:
   ```js
   import { useElementsStore } from '@/stores/elements';
   const store = useElementsStore();
   ```
2. **Fetch Elements**: Call `store.fetchElements()` to load data.
3. **Filter/Sort**: Use `store.setFilters()` to apply dynamic filters.
4. **CRUD Operations**: Use actions like `store.createElement()` or `store.updateElement()`.
5. **Access Data**: Use computed properties like `store.filteredElements` or `store.elementTypes`.

## Dependencies

> ``pinia``
> ``vue``
> ``@/services/api` (custom `apiService` for HTTP requests).`

## Related

- [[Vue Pinia Guide]]
- [[Vue API Service Patterns]]

>[!INFO] Error Handling
> The store ensures `elements` is always an array, even after API failures, by defaulting to an empty array (`[]`). Errors are logged but do not disrupt state immutability.

>[!WARNING] Local vs. API State
> Local state (`elements`) may diverge from the API if updates are not synced (e.g., manual edits). Use `updateElement` to reconcile changes.
