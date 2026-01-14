**Tags:** #bash-script, #world-generation, #manual-testing, #url-generation, #map-testing
**Created:** 2026-01-13
**Type:** test-reference

# test_all_world_types

## Summary

```
Generates and documents test URLs for manual validation of world type rendering in a map generator system.
```

## Details

> This script automates the creation of URLs for testing different world types (e.g., "Planet," "Galaxy") with a predefined hash (`ew`) and map type (`full`). It iterates through a predefined list of world types, encodes spaces in names, and constructs URLs using a base endpoint (`http://localhost:5174/#map-generator`). Users manually test each URL by opening it in a browser, observing map generation, and recording results.

## Key Functions

### `URL Generation`

Constructs URLs with encoded world type names, hash, and map type parameters.

### `Manual Testing Guide`

Provides step-by-step instructions for testing and documentation (e.g., screenshot naming conventions).

## Usage

1. Run the script in a terminal to generate test URLs.
2. Copy each URL and paste it into a browser to test the corresponding world type.
3. Follow the test procedure (e.g., wait for generation, zoom out, take screenshots).
4. Document observations and statistics for each test case.

## Related

- [[none]]

>[!INFO] Important Note
> The script assumes the base URL (`http://localhost:5174/#map-generator`) is accessible and the backend API supports the `generate=true` parameter for manual testing.
> If spaces appear in world type names, they are URL-encoded as `%20` to ensure compatibility with the API.

>[!WARNING] Caution
> Manual testing may take 30–60 seconds per URL. Ensure the system has sufficient resources to avoid delays or crashes during generation. Always verify the correct hash (`ew`) and map type (`full`) are used.
