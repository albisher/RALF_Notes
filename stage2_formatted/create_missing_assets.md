**Tags:** #asset-generation, #robot-creation, #world-management, #api-integration, #space-colony
**Created:** 2026-01-13
**Type:** code-script

# create_missing_assets

## Summary

```
Script automates creation of missing assets (X-Series robots, plants, and buildings) to reach a total of 26 assets for a space colony system.
```

## Details

> This script interacts with a local API (`https://localhost:8443/api`) to programmatically generate missing elements for a virtual space colony called Space Peral. It first authenticates via a test account, then iterates through predefined lists of missing robots, plants, and buildings, creating each via a standardized API endpoint. The script handles error reporting for failed requests while tracking progress through print statements.
> 
> The logic follows a modular approach: authentication is handled separately, while asset creation is organized by element type (robots, plants, buildings). Each asset definition includes metadata like name, description, and custom capabilities, which are formatted into the API request payload.

## Key Functions

### `login()`

Authenticates with the API using hardcoded credentials and returns an access token.

### `generate_element(token, world_id, element_type, name, description, additional_data)`

Creates a single asset (robot/plant/building) using the provided token and world ID.

### `create_missing_assets(token, world_id)`

Orchestrates the entire asset creation process by:

## Usage

1. Run the script after ensuring the API server (`localhost:8443`) is accessible
2. The script automatically:
   - Logs in with test credentials
   - Creates all missing assets in sequence
   - Prints progress/output for each operation
3. Requires a valid `world_id` parameter to be passed to `create_missing_assets()`

## Dependencies

> `requests`
> `json`
> `datetime`
> `requests (via `import requests`)`
> ``verify_SSL=False` (for self-signed certificate handling)`

## Related

- [[Space Peral API Documentation]]
- [[World Asset Management Guide]]

>[!INFO] Important Note
> This script uses hardcoded credentials ("test"/"passtest") for authentication. In production, replace these with secure credentials from a configuration file or environment variables.
>

>[!WARNING] Caution
> The script bypasses SSL verification (`VERIFY_SSL=False`). Only use this with the actual API server you intend to deploy. Running with this setting against an untrusted server could expose your system to security risks.
>

>[!WARNING] Caution
> The script assumes the API endpoint structure matches exactly what's shown in the code. Changes to the API may break this script without modification.
