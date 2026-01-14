**Tags:** #test-script, #api-integration, #deletion-test, #authentication, #async-await
**Created:** 2026-01-13
**Type:** code-test

# test-world-delete

## Summary

```
Tests deletion of a world from an API endpoint after authentication.
```

## Details

> This script uses Axios to interact with a local API running on `https://localhost:8443/api`. It first authenticates using a hardcoded test user (`test`/`passtest`), then retrieves a list of worlds. It selects a world (excluding "Space Peral") for deletion, sends a DELETE request, and verifies the deletion by checking if the world remains in the list. The script logs each step and handles errors, including server-side failures (e.g., 500 errors).

## Key Functions

### ``authenticate()``

Authenticates with the API using hardcoded credentials and returns an access token.

### ``testWorldDelete()``

Orchestrates the full workflow: fetching worlds, selecting a test world, deleting it, and verifying deletion.

## Usage

1. Run the script directly in a Node.js environment.
2. Ensure the API is running at `https://localhost:8443/api` with the expected endpoints (`/auth/login`, `/worlds`).
3. The script ignores SSL certificate errors for testing purposes.

## Dependencies

> ``axios``
> ``https` (Node.js built-in modules)`

## Related

- [[`test-authentication`]]
- [[`api-worlds-endpoint`]]

>[!INFO] Important Note
> The script uses `rejectUnauthorized: false` for HTTPS requests, which may expose it to security risks in production. Use this only for testing.

>[!WARNING] Caution
> Hardcoded credentials (`test`/`passtest`) are insecure. Replace with environment variables or a secure config in production.
