**Tags:** #Vue.js, #Composable, #WorldManagement, #GameDev, #API-Integration, #StateManagement
**Created:** 2026-01-13
**Type:** code-notes

# useWorldOperations

## Summary

```
Manages world-related operations, state, and API interactions for a game or simulation system.
```

## Details

> This composable (`useWorldOperations`) handles core world management tasks, including fetching, creating, and updating world data (e.g., names, descriptions, time systems). It relies on a `boxOrchestrator` for backend operations and an `api` client for authentication. State is tracked via Vue’s `ref`, and error handling is centralized via a logger. The system initializes with default values (e.g., `Space Peral`) and validates prerequisites (e.g., authenticated API, selected world) before proceeding.
> 
> Key logic:
> - **Asynchronous operations** (e.g., `loadWorlds`, `createWorld`) use `try/catch` to manage failures.
> - **State synchronization**: Updates to `worldInfo`, `worldTimeSystem`, or `worldRules` trigger backend calls via `boxOrchestrator`.
> - **Default behavior**: Automatically selects the first world after loading if none is set.

## Key Functions

### ``loadWorlds()``

Fetches and caches all worlds from the backend API.

### ``createWorld(worldData)``

Creates a new world with provided metadata and refreshes the list.

### ``saveTimeSystem()``

Updates the time system (e.g., hours/day) for the current world.

### ``saveWorldInfo()``

Updates world attributes (e.g., description, type).

### ``saveRules()``

Applies custom rules for the selected world.

### ``currentWorldId`/`worlds``

Reactive state tracking the active world and its list.

## Usage

1. **Import and inject**:
   ```js
   import { useWorldOperations } from './composables/useWorldOperations';
   const worldOps = useWorldOperations(boxOrchestrator, api);
   ```
2. **Trigger operations**:
   ```js
   await worldOps.loadWorlds(); // Load existing worlds
   await worldOps.createWorld({ name: "New World", description: "..." });
   await worldOps.saveTimeSystem(); // Update time system
   ```
3. **Access state**:
   ```js
   const currentWorld = worldOps.worlds[0];
   ```

## Dependencies

> ``vue``
> ``boxOrchestrator``
> ``api` (custom client)`
> ``logger` (utility module).`

## Related

- [[WorldDataSchema]]
- [[BoxOrchestratorAPI]]
- [[GameWorldConfiguration]]

>[!INFO] Default World Selection
> If no world is selected initially, the first world in `worlds.value` is auto-assigned as the default (`currentWorldId.value = worlds.value[0].id`). This ensures a fallback for empty state.

>[!WARNING] Error Handling
> Uncaught errors in `createWorld`/`save*` methods are caught and logged, but the caller must handle retries or UI feedback explicitly. Silent failures may occur if `logger.error` is not configured.
