**Tags:** #world-building, #asset-generation, #space-colony, #api-integration, #time-tracking
**Created:** 2026-01-13
**Type:** code-script

# generate_story_with_assets

## Summary

```
Generates a space colony world with detailed assets (characters, buildings, robots) linked by location and historical time.
```

## Details

> This script interacts with a backend API (`http://backend:5000`) to create a structured space colony world. It first authenticates via a test user, then constructs a world with a timestamped name. The script populates the world with:
> - **Characters** (e.g., Captain Sarah Chen) with roles, descriptions, and historical timestamps.
> - **Buildings** (e.g., Central Command Hub) tied to specific locations and functions.
> - **Robots** (e.g., Maintenance Bot Delta-7) with assigned tasks and creation dates.
> Time-based asset creation simulates progression over days, while locations define spatial relationships. Outputs are logged but not persisted to disk.

## Key Functions

### `create_test_user()`

Authenticates with a hardcoded test account to obtain an API token.

### `create_world_with_detailed_assets(token)`

Orchestrates world creation and populates assets with metadata (location, time, type).

### `Character/Building/Robot data arrays`

Predefined lists of assets with standardized fields (name, element_type, location, time_created, etc.).

## Usage

1. Run the script to authenticate and generate a world.
2. Modify `BACKEND_URL` or `STORY_OUTPUT_DIR` for customization.
3. Extend the `characters`, `buildings`, or `robots` lists for additional assets.
4. Ensure the backend API is running and accessible.

## Dependencies

> `requests`
> `urllib3`
> `datetime`
> `pathlib (Python standard libraries)`
> `backend API (custom service at `http://backend:5000`).`

## Related

- [[None]]

>[!INFO] Test Authentication
> Uses hardcoded credentials (`test/passtest`) for simplicity; replace with production credentials in production.

>[!WARNING] Insecure API Calls
> Disables SSL verification (`session.verify = False`) for testing; restrict in production to avoid security risks.

>[!CAUTION] Backend Dependency
> Fails silently if the backend API is unreachable; add retry logic for production use.
