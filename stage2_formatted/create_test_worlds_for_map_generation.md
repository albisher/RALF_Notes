**Tags:** #test-script, #map-generation, #world-creation, #backend-integration, #authentication
**Created:** 2026-01-13
**Type:** code-script

# create_test_worlds_for_map_generation

## Summary

```
Generates predefined test worlds for map generation verification in a game or application backend.
```

## Details

> This script automates the creation of three distinct test worlds—**Clouds World**, **Galaxy World**, and **Random General World**—using a backend API. It handles authentication via test credentials or manual input, then iterates through predefined configurations to create each world. The script logs success/failure and provides a summary of created worlds, including their IDs and types. It integrates with a RESTful backend API to ensure map generation systems can verify functionality against these predefined environments.

## Key Functions

### `get_auth_token()`

Attempts to log in with test credentials (`test@example.com`/`testpassword`) and falls back to manual token input.

### `create_world(token, name, description, world_type)`

Creates a world in the backend API with the given parameters, checks for existing worlds, and returns the ID and metadata if successful.

### `main()`

Orchestrates the script execution—authenticates, defines world configurations, iterates through creation, and displays results.

## Usage

1. Run the script (`python create_test_worlds_for_map_generation.py`).
2. If auto-login fails, manually input a JWT token when prompted.
3. The script outputs creation status and a summary of created worlds.
4. Post-creation, navigate to the frontend map generator (e.g., `http://localhost:5174/#generate`) to test map generation against these worlds.

## Dependencies

> `requests`
> `json`
> `sys`
> `os (standard libraries)
`os.getenv('BACKEND_URL')` (environment variable for backend URL`
> `defaults to `http://localhost:8000`)`

## Related

- [[backend-api-documentation]]
- [[map-generation-testing-guide]]

>[!INFO] Important Note
> The script uses hardcoded test credentials (`test@example.com`/`testpassword`). In production, replace these with secure credentials or disable auto-login to enforce manual token input.
>

>[!WARNING] Caution
> If the backend API fails during creation, the script may exit silently. Check logs for errors or retry manually with the provided IDs. The `world_type` values (`'Cloud World'`, `'Universe'`, `'Planet'`) are placeholders—adjust if the backend expects different keys.
