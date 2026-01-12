**Tags:** #automated-testing, #web-verification, #browser-automation, #osm-integration, #plotly-sync
**Created:** 2026-01-12
**Type:** code-notes

# verify_osm_plotly_sync

## Summary

```
Script verifies synchronization between OpenStreetMap (OSM) and Plotly visualizations via browser automation.
```

## Details

> This script uses Selenium to automate browser testing, comparing OSM data layers with Plotly-generated visualizations. It captures screenshots, logs console errors, and validates UI consistency between the two systems. The verification includes headless Chrome execution, element presence checks, and error handling for critical issues (e.g., Cesium-related warnings).

## Key Functions

### `take_screenshot(driver, filename)`

Saves browser snapshots to a timestamped directory.

### `get_console_errors(driver)`

Extracts severe browser console logs (e.g., Cesium errors).

### `wait_for_element(driver, by, value, timeout)`

Polls for DOM elements with configurable timeout.

### `verify_osm_plotly_sync()`

Orchestrates the full synchronization test workflow:

### `(Incomplete`

Missing Plotly/OSM-specific validation logic.)

## Usage

1. Run as standalone script (e.g., `python verify_osm_plotly_sync.py`).
2. Configure `base_url` to point to the OSM-Plotly backend.
3. Extend `verify_osm_plotly_sync()` with custom assertions (e.g., comparing layer visibility).
4. Ensure ChromeDriver matches the Chrome version in `--version` argument.

## Dependencies

> `requests`
> `time`
> `os`
> `json`
> `datetime`
> `selenium-webdriver (ChromeDriver)`
> `pytest (implicitly via `time.sleep` and `try/except`)`

## Related

- [[osm-dashboard-backend]]
- [[plotly]]

>[!INFO] Critical Error Filtering
> The script filters for errors containing `'cesium'` (e.g., WebGL/performance issues in Cesium-based rendering). Add custom regex to detect OSM/Plotly-specific warnings.

>[!WARNING] Headless Mode Risks
> `--disable-web-security` and `--allow-running-insecure-content` may expose security vulnerabilities. Use only in trusted environments.
