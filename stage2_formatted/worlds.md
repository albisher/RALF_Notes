**Tags:** #Vue.js, #Pinia, #State Management, #API Service, #World Management
**Created:** 2026-01-13
**Type:** documentation

# worlds

## Summary

```
Manages world data and state for a multi-world application using Pinia and Vue.
```

## Details

> This Pinia store handles CRUD operations for world entities, including fetching, creating, updating, and deleting worlds. It maintains state for all worlds, the currently active world, loading status, and error handling. The store interacts with an API service (`apiService`) and persists the active world ID in `localStorage` for persistence across sessions. It also includes computed properties to track the count and existence of worlds.

## Key Functions

### ``fetchWorlds``

Asynchronously retrieves all worlds from the API, updates the store state, and loads the active world.

### ``fetchWorld``

Fetches a single world by ID and updates the `currentWorld` reference.

### ``createWorld``

Creates a new world via the API and appends it to the `worlds` array.

### ``updateWorld``

Updates an existing world by ID, modifies the store state, and updates the active world if applicable.

### ``deleteWorld``

Removes a world by ID from the store and clears the active world reference if needed.

### ``setCurrentWorld``

Sets a world as active, updates its status, and persists the ID in `localStorage`.

### ``loadActiveWorld``

Loads the previously saved active world from `localStorage` if available.

### ``clearError``

Resets the error state to `null`.

## Usage

1. **Initialize the store**: Import and use `useWorldsStore` in a Vue component.
2. **Fetch worlds**: Call `fetchWorlds()` to load all worlds.
3. **Fetch a single world**: Use `fetchWorld(id)` to load a specific world.
4. **Manage state**: Access `worlds`, `currentWorld`, `loading`, and `error` for reactivity.
5. **CRUD operations**: Use `createWorld`, `updateWorld`, `deleteWorld` for dynamic updates.
6. **Set active world**: Use `setCurrentWorld(world)` to mark a world as active.

## Dependencies

> ``pinia``
> ``vue``
> ``vuex-compat``
> ``@/services/api` (custom `apiService` for HTTP requests).`

## Related

- [[Pinia Documentation]]
- [[Vue]]
- [[API Service Reference]]

>[!INFO] Authentication Handling
> The store checks for an `auth_token` in `localStorage` before making API calls. If absent, it briefly waits (2 seconds) to allow auto-login logic to complete before proceeding.


>[!WARNING] Error Handling
> Errors are caught and stored in `error.value`, but the `worlds` array is always reset to an empty array to prevent undefined behavior. Always call `clearError()` to reset errors explicitly.
