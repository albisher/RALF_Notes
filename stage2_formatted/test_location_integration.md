**Tags:** #location-integration, #maps-api, #coordinate-generation, #biome-detection, #testing-framework
**Created:** 2026-01-13
**Type:** test-reference

# test_location_integration

## Summary

```
Test script validates location services for coordinate generation, biome detection, and cluster-based location generation.
```

## Details

> This script performs integration tests for a backend location service, verifying:
> 1. Service health and available generators
> 2. Hash-based location generation across different zones (industrial, residential, military, etc.)
> 3. Coordinate parsing from various input formats (including latitude/longitude with zone hints)
> 4. Cluster generation of multiple locations within a specified radius
> 
> The tests use a mock authentication system with hardcoded credentials and make HTTP requests to a local backend API at `https://localhost:8443`.

## Key Functions

### ``get_auth_token()``

Authenticates with the backend API to obtain an access token.

### ``test_location_integration()``

Orchestrates all test cases, collecting results in a structured format.

### `Location generation tests`

Evaluates seed-based location creation with biome classification.

### `Coordinate parsing tests`

Validates conversion of string inputs to structured coordinates.

### `Cluster generation test`

Checks ability to generate multiple locations within a specified radius.

## Usage

1. Run the script directly to execute all integration tests
2. Output includes console progress and structured test results
3. Results are stored in `test_results` dictionary with timestamps and pass/fail statuses
4. Requires SSL verification disabled (insecure for production use)

## Dependencies

> `requests`
> `urllib3`
> `datetime`
> `json (standard Python libraries)
External backend API at `https://localhost:8443` (non-production)`

## Related

- [[Backend API Documentation]]
- [[Location Service Specifications]]

>[!INFO] Important Note
> This script uses hardcoded credentials ('test', 'passtest') for authentication. In production, use environment variables or secure credential storage.
> The backend URL (`https://localhost:8443`) is hardcoded for local testing only. Replace with production endpoint for deployment.

>[!WARNING] Caution
> Disabling SSL verification (`verify=False`) makes this script vulnerable to man-in-the-middle attacks. Only use in trusted local environments.
> Test results are collected in memory and not persisted to disk. For long-running tests, implement proper result storage.
