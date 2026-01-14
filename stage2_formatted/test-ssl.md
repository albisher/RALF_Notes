**Tags:** #SSL, #Security, #WebServer, #APITesting, #BashScript
**Created:** 2026-01-13
**Type:** code-test

# test-ssl

## Summary

```
Validates SSL/TLS configuration, HTTP/HTTPS redirects, security headers, and certificate integrity for a web application.
```

## Details

> This script performs automated checks for SSL/TLS security in the Space Pearl application by verifying:
> 1. HTTP-to-HTTPS redirect (301 status code).
> 2. HTTPS connection success (200 status).
> 3. API endpoint accessibility (200 status).
> 4. Presence of security headers (e.g., `X-Frame-Options`, `X-XSS-Protection`).
> 5. CORS headers for API compatibility.
> 6. Valid SSL certificate details (subject, expiration).
> 
> It uses `curl` and `openssl` to inspect responses and headers, with strict validation logic.

## Key Functions

### `HTTP-to-HTTPS Redirect Check`

Ensures proper redirection from HTTP to HTTPS.

### `HTTPS Connection Test`

Validates secure port (8443) and TLS encryption.

### `API Endpoint Validation`

Checks `/api/health` endpoint for correct HTTP status.

### `Security Headers Audit`

Detects critical headers like CSP, XSS protection, and frame options.

### `CORS Header Validation`

Confirms API supports cross-origin requests.

### `Certificate Validation`

Extracts and verifies SSL certificate metadata.

## Usage

Run as:
```bash
./scripts/test-ssl.sh
```
- Tests run sequentially; exits on first failure.
- Requires `localhost:8443` to be accessible (self-signed certs ignored with `-k` flag).

## Dependencies

> ``curl``
> ``openssl``
> ``bash` (standard libraries).`

## Related

- [[Space Pearl Application Documentation]]
- [[Security Hardening Guide]]

>[!INFO] Important Note
> Script skips certificate verification (`-k` flag) for testing self-signed certs. Use with trusted certs in production.

>[!WARNING] Caution
> Failing any test exits immediately. Ensure all dependencies (`curl`, `openssl`) are installed.
