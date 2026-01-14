**Tags:** #axios, #REST-API, #interceptors, #authentication, #CRUD-operations, #generation-functions
**Created:** 2026-01-13
**Type:** code-library

# api

## Summary

```
Manages HTTP requests for a game/world-building API with authentication, CRUD operations, and generation utilities.
```

## Details

> This code defines an Axios-based API client with:
> 1. **Axios instance** configured with base URL (`/api`), timeout (10s), and JSON headers.
> 2. **Interceptors** for request/response handling, including auth token injection via `localStorage`.
> 3. **Endpoint routing** for CRUD operations across entities (worlds, elements, characters).
> 4. **Generation methods** for random/seed-based character/element creation.
> 5. **Hash management** for deterministic generation via Python-backed endpoints.
> 
> The client abstracts API calls into reusable methods (e.g., `getWorlds()`, `generateRandomElement()`), with error handling logged but not redirected.

## Key Functions

### `api`

Axios instance with interceptors.

### `endpoints`

Dynamic URL routing for API endpoints.

### `getWorlds()`

Fetches all worlds or aggregates elements across worlds.

### `generateRandomElement(worldId, elementType)`

Creates a random element in a world using a seed or randomness.

### `saveHashDetails(hashData)`

Stores metadata for deterministic generation.

### `getHashDetails(seed, assetType)`

Retrieves pre-generated asset details.

## Usage

```javascript
// Initialize and use the API
import { apiService } from './api';

// Fetch a world
const world = await apiService.getWorld(1);

// Create a world
const newWorld = await apiService.createWorld({ name: "New World" });

// Generate a random element
const element = await apiService.generateRandomElement(1, "treasure");
```

## Dependencies

> `axios`
> `localStorage (browser-only)`

## Related

- [[API-Endpoints-Reference]]
- [[Auth-Implementation-Guide]]

>[!INFO] Token Handling
> Uses `localStorage` for auth tokens (not secure for production; consider `httpOnly` cookies or JWT).
> Token presence is logged but not validated for personal use.


>[!WARNING] Error Handling
> Silent rejection of errors (e.g., network failures) without user feedback. Add retry logic for production.
