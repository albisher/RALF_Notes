**Tags:** #authentication, #secure-storage, #multi-user-single-user, #api-service
**Created:** 2026-01-13
**Type:** code-notes

# auth-service

## Summary

```
Handles user authentication with environment-specific modes (single-user/dev or multi-user/production).
```

## Details

> This `AuthService` class manages user authentication, dynamically detecting the environment mode (single-user for dev via `config.isDevelopment()` or hostname check, multi-user for production). It supports manual login, registration, and logout, with secure token storage. The service validates existing tokens on initialization and enforces explicit authentication in production. Secure storage (`secureStorage`) retrieves tokens, and `AuthAPIBox` handles backend operations.

## Key Functions

### ``initialize()``

Checks for existing valid tokens, auto-authenticates in single-user mode, or prompts login in multi-user mode.

### ``login(username, password)``

Authenticates a user in multi-user mode via API, returning a token and user object.

### ``register(username, email, password)``

Creates a new user account in multi-user mode using `AuthAPIBox`.

### ``logout()``

Clears tokens, resets auth state, and reloads page in multi-user mode.

### ``_getStoredToken()``

Securely retrieves the stored authentication token from `secureStorage`.

### ``_clearStoredToken()``

(Inferred) Clears the stored token (not explicitly defined but implied by usage).

## Usage

1. Initialize with an `apiClient` (e.g., a fetch-based client).
2. Call `initialize()` to check existing auth or auto-login in dev mode.
3. Use `login()` or `register()` for manual auth/registration.
4. Call `logout()` to end session.

## Dependencies

> ``config.js``
> ``logger.js``
> ``AuthAPIBox``
> ``BoxInput``
> ``secure-storage.js``

## Related

- [[`config]]
- [[`secure-storage]]
- [[`AuthAPIBox`]]

>[!INFO] Lazy-Loaded Auth Mode
> The `authMode` property is lazily initialized via `_detectAuthMode()` to avoid circular dependencies or early config checks. This ensures the service adapts to environment changes dynamically.


>[!WARNING] Security Note
> Auto-authentication is disabled in production (`autoAuthenticate()` is removed). Users must explicitly log in via `login()` or `register()`. Always validate tokens in production to prevent replay attacks.
