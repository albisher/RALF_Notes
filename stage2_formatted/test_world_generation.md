**Tags:** #testing, #api-integration, #world-generation, #hash-based-creation, #backend-validation
**Created:** 2026-01-13
**Type:** test-reference

# test_world_generation

## Summary

```
Validates backend generator integration by creating and verifying hash-based elements in a test world via API.
```

## Details

> This script tests the integration between a world generation system and hash-based element creation. It authenticates with a backend API, locates a predefined test world, and populates it with predefined elements (trees, buildings, robots, characters) using SHA-256-generated seeds. After creation, it retrieves all elements to verify consistency and generates a detailed report.
> 
> The test uses a mock API endpoint (`localhost:8443`) with insecure SSL verification disabled for testing. It creates four predefined elements with deterministic hash-based identifiers to ensure reproducibility.

## Key Functions

### `get_auth_token()`

Authenticates with the backend API using hardcoded credentials.

### `test_world_generators()`

Orchestrates the entire test workflow:

### `generate_hash(seed)`

Uses SHA-256 to generate deterministic hashes for element seeds.

## Usage

1. Run the script directly (`python test_world_generation.py`).
2. Ensure the backend API (`localhost:8443`) is running and accessible.
3. The script will:
   - Print progress and errors in console.
   - Generate a Markdown report in `generated_stories/` with timestamped filename.
4. Verify the report contains all expected elements and their IDs.

## Dependencies

> `requests`
> `urllib3`
> `json`
> `datetime`
> `os`

## Related

- [[World Generation System Design]]
- [[Backend API Specifications]]

>[!INFO] Important Note
> The script uses `verify=False` for HTTPS requests, which may expose it to man-in-the-middle attacks in production. Use with caution in non-test environments.

>[!WARNING] Caution
> Hardcoded credentials (`test`/`passtest`) are used for authentication. In production, replace with secure environment variables or OAuth tokens.
