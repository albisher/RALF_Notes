**Tags:** #authentication, #jwt, #flask, #jwt_required, #token-management, #security, #database, #api-endpoints
**Created:** 2026-01-13
**Type:** documentation

# login_authentication_working

## Summary

```
Documentation for a functional login authentication system using JWT, test credentials, and protected API endpoints.
```

## Details

> This file outlines the working implementation of a login authentication system with pre-configured test credentials (`test/testpass`). The system uses Flask-JWT-Extended for JWT-based authentication, ensuring secure token handling with access tokens expiring in 24 hours and refresh tokens valid for 30 days. The system includes protected endpoints requiring valid JWT tokens, tested with endpoints like `/api/dashboard`, `/api/worlds`, and `/api/characters`. Security features include password hashing with bcrypt and automatic token validation via `@jwt_required()` decorator.

## Key Functions

### `login(username, password)`

Sends credentials to `/api/auth/login`, stores tokens in `localStorage`, and returns user data.

### `authenticatedRequest(url, options)`

Adds `Authorization: Bearer <token>` header to requests; refreshes token if expired via `refreshToken()`.

### `refreshToken()`

Calls `/api/auth/refresh` to generate a new access token from a refresh token; logs out if refresh fails.

### `Test credentials (test/testpass)`

Pre-configured user in the database for testing purposes.

### `JWT token system`

Implements secure token generation, expiration, and validation for authenticated requests.

## Usage

1. **Login**: Use `login(username, password)` to authenticate and store tokens.
2. **Access Protected Endpoints**: Use `authenticatedRequest()` with a valid token.
3. **Refresh Token**: Call `refreshToken()` if the access token expires.
4. **Frontend Integration**: Submit credentials via a form to trigger `login()` and redirect to `/dashboard` on success.

## Dependencies

> `Flask-JWT-Extended`
> `Flask`
> `Werkzeug (for password hashing)`
> `SQLAlchemy (for database interactions)`
> `and a frontend framework (likely React or vanilla JS for frontend integration).`

## Related

- [[Security Best Practices for JWT Authentication]]
- [[Flask JWT-Extended Documentation]]
- [[Password Hashing with Werkzeug]]
- [[Database Schema for User Authentication]]

>[!INFO] Important Note
> The test credentials (`test/testpass`) are hardcoded for testing and should **not** be used in production. Always use secure password policies and hashed credentials in real applications.


>[!WARNING] Caution
> Never expose refresh tokens in client-side storage (e.g., `localStorage`) without additional security measures like token binding or short-lived refresh tokens. The current implementation uses long-lived refresh tokens (30 days), which is a security risk if compromised. Consider implementing token binding or a shorter refresh token expiry.
