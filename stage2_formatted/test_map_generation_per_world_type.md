**Tags:** #playwright-testing, #map-generation, #world-types, #ui-testing, #automated-testing
**Created:** 2026-01-13
**Type:** code-test

# test_map_generation_per_world_type

## Summary

```
Automated test suite for map generation across different world types (Planet, Galaxy, Cloud) using Playwright.
```

## Details

> This script tests map generation functionality by navigating to a game’s generate tab, selecting a world type, inputting a hash, and verifying the generated map. It uses Playwright to interact with a web UI, captures screenshots at key stages, and logs progress. The test runs separately for each world type (Planet, Galaxy, Cloud) and records screenshots in a timestamped directory for debugging.
> 
> The script handles Playwright availability, validates selectors for dropdowns and inputs, and waits for map generation completion via visual indicators (e.g., map preview elements, progress bars). It includes fallback selectors for robustness and logs errors gracefully.

## Key Functions

### `take_screenshot(page, filename, description)`

Captures a screenshot of the current page state and saves it to a structured directory.

### `test_world_type(page, world_name, hash_input, expected_type)`

Orchestrates the full workflow for a single world type, including navigation, input, generation, and verification.

### `create_screenshot_directory`

Dynamically constructs a timestamped directory for storing screenshots (e.g., `YYYYMMDD/HHMM/`).

## Usage

1. Install dependencies: `pip install playwright && playwright install chromium`.
2. Run the script directly or integrate it into a test suite (e.g., pytest).
3. Customize `BASE_URL` and `hash_input` for testing different scenarios.
4. The script logs progress and saves screenshots to `screenshots/map_generation_ui_tests/YYYYMMDD/HHMM/`.

## Dependencies

> `playwright`
> `playwright-chromium`
> `pytest (if run as a test suite)`
> `requests (implicitly via Playwright’s browser automation).`

## Related

- [[Test Map Generation UI]]
- [[World Type Configuration]]
- [[Playwright Browser Automation Guide]]

>[!INFO] Important Note
> The script assumes the target application is running locally at `http://localhost:5174`. Adjust `BASE_URL` if the endpoint differs.
>

>[!WARNING] Caution
> If Playwright fails to locate elements (e.g., dropdowns or buttons), the test may proceed with fallback selectors or exit silently. For critical tests, add explicit error handling or retry logic.
