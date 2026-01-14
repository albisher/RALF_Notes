**Tags:** #API-Integration, #World-Generation, #Robot-Simulation, #Data-Processing
**Created:** 2026-01-13
**Type:** code-notes

# populate_space_peral

## Summary

```
Script automates the creation of a fictional robotic colony world ("Space Peral") and populates it with predefined characters, robots, and elements via a local API.
```

## Details

> This script interacts with a backend API (`https://localhost:8443/api`) to:
> 1. Authenticate via hardcoded credentials (`test/testpass`).
> 2. Create a new world with a custom description.
> 3. Generate elements (characters/robots) by calling `/worlds/{world_id}/generate`, passing structured data (e.g., traits, relationships).
> The script uses a **seed-based naming system** (e.g., `name.lower().replace(" ", "_")`) to ensure uniqueness in API responses.

## Key Functions

### `login()`

Authenticates with the API and returns an access token.

### `create_world(token, name, description)`

Creates a new world with the provided token and metadata.

### `generate_element(token, world_id, element_type, name, description, data)`

Generates a customizable element (e.g., a robot or character) within a world.

### `main()`

Orchestrates the workflow: login → world creation → population with predefined entities.

## Usage

1. Run the script directly (`python populate_space_peral.py`).
2. Ensure the API is running locally at `https://localhost:8443/api`.
3. Modify `BASE_URL` or credentials if needed (though hardcoded for simplicity).

## Dependencies

> `requests`
> `json`
> `datetime`

## Related

- [[Space Peral API Documentation]]
- [[Robotic Colony Design Notes]]

>[!INFO] Security Note
> The script uses `verify=False` for HTTPS requests, disabling SSL certificate validation. **Risk:** Unsafe for production; use only in trusted local environments.

>[!WARNING] Hardcoded Credentials
> Hardcoded `test/testpass` may fail in real-world deployments. **Recommendation:** Use environment variables or a config file for credentials.
