**Tags:** #testing, #redirect, #api, #frontend, #axios
**Created:** 2026-01-13
**Type:** test-reference

# test-character-redirect

## Summary

```
Validates character asset redirect functionality and route accessibility for a frontend application.
```

## Details

> This script performs a series of HTTP GET requests using Axios to verify:
> 1. Frontend accessibility at `http://localhost:5173`.
> 2. Accessibility of the assets route (`/assets`).
> 3. Accessibility of the characters route (`/characters`).
> 4. Handling of character detail routes (e.g., `/characters/{id}`) and asset detail routes (e.g., `/assets/{id}`).
> The test logs success/failure for each endpoint, including expected 404 responses for non-existent routes. It concludes with a summary of expected redirect behavior for character assets (redirecting to `/characters/{id}`) and asset routes (remaining on `/assets/{id}`).

## Key Functions

### `testCharacterRedirect()`

Orchestrates all route accessibility tests and logs results.

### `Axios GET requests`

Individual HTTP calls to test endpoints (frontend, assets, characters, and detail routes).

## Usage

1. Run the script in a Node.js environment with an accessible frontend (e.g., running on `http://localhost:5173`).
2. Execute via command line: `node test-character-redirect.js`.
3. Observe console logs for test outcomes and summary of expected redirect logic.

## Dependencies

> `axios`
> `Node.js runtime`

## Related

- [[none]]

>[!INFO] Important Note
> This test assumes the frontend is running on `http://localhost:5173`. Ensure the server is active before execution.

>[!WARNING] Caution
> Non-existent routes (e.g., `/characters/319` or `/assets/289`) may return 404 errors, which are expected and logged as warnings. Avoid hardcoding non-existent IDs to prevent misleading results.
