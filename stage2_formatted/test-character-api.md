**Tags:** #API-Testing, #Authentication, #Character-Management, #Axios, #Node.js
**Created:** 2026-01-13
**Type:** test-reference

# test-character-api

## Summary

```
Tests the character API endpoints for creation, update, and retrieval of characters with authentication.
```

## Details

> This script performs a comprehensive test of a character API by:
> 1. Authenticating via a login endpoint to obtain an access token.
> 2. Creating an Axios instance with the token for authenticated requests.
> 3. Fetching existing characters or creating a test character if none exist.
> 4. Updating either the newly created character or the first existing character.
> 5. Verifying the update by retrieving all characters and checking for the updated record.
> The test handles both success and failure cases, logging detailed results.

## Key Functions

### ``authenticate()``

Authenticates the user with hardcoded credentials and returns an access token.

### ``testCharacterAPI()``

Orchestrates the full test workflow, including authentication, character operations, and verification.

### `Axios Instance Creation`

Two instances are created—one for initial authentication (ignoring SSL) and another for authenticated API calls.

## Usage

1. Run the script directly in a Node.js environment.
2. Ensure the API (`https://localhost:8443/api`) is accessible and running.
3. The script logs detailed progress and final results, including success/failure status.

## Dependencies

> ``axios``
> ``https` (Node.js built-in modules)`

## Related

- [[Character API Documentation]]
- [[Authentication Guide]]

>[!INFO] Important Note
> The script uses `rejectUnauthorized: false` for SSL verification, which may be insecure in production. Use a valid certificate in production environments.

>[!WARNING] Caution
> Hardcoded credentials (`username: 'test'`, `password: 'passtest'`) are used for testing. Avoid committing credentials to version control. Use environment variables or a config file for production.
