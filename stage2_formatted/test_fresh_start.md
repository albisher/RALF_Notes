**Tags:** #test-script, #backend-api, #data-reset, #authentication, #rest-api
**Created:** 2026-01-13
**Type:** test-reference

# test_fresh_start

## Summary

```
Tests backend API functionality for fresh start/reset operations, including backup and partial cache/database reset.
```

## Details

> This script verifies all available reset options and their execution through HTTP requests to a backend API. It authenticates using a test user, then tests:
> 1. Retrieving available reset options and current data counts
> 2. Checking current reset status (total items, data presence)
> 3. Creating a named backup of existing data
> 4. Executing partial resets (files only) with specific file type filtering
> 5. Performing a complete cache reset
> 
> The test uses a local backend at `https://localhost:8443` with disabled SSL verification for testing purposes.

## Key Functions

### ``get_auth_token()``

Authenticates with backend API to obtain an access token for authenticated requests.

### ``test_fresh_start_functionality()``

Orchestrates all reset-related tests with detailed logging and result tracking.

## Usage

1. Run as Python script to execute all reset functionality tests
2. Requires backend server running at localhost:8443 with test credentials
3. Outputs test results in structured format to `test_results` dictionary

## Dependencies

> `requests`
> `urllib3`
> `datetime`
> `os`

## Related

- [[backend_api_documentation]]
- [[fresh_start_implementation]]

>[!INFO] Important Note
> This script uses insecure HTTP requests (SSL verification disabled) for testing purposes only. Production use should enable proper SSL verification.

>[!WARNING] Caution
> The test uses hardcoded credentials ('test', 'passtest') which may expose sensitive data if not properly secured. Always validate credentials in production environments.
