**Tags:** #browser-automation, #drone-flight-test, #playwright, #asyncio, #gps-simulation
**Created:** 2026-01-13
**Type:** code-notes

# test_home_flight_browser

## Summary

```
Automates drone flight testing at a predefined home location using browser automation.
```

## Details

> This script uses Playwright’s async API to simulate drone flight operations, specifically testing the "Home" GPS location for a drone application running on `localhost:5007`. It performs two main actions: setting the GPS coordinates to the home location (either via dropdown or manual input) and navigating to the drone’s master controls. The script logs findings (successes/errors) in a structured dictionary and prints status updates. It relies on asynchronous browser automation to interact with a web-based drone control interface.

## Key Functions

### `test_home_flight()`

Orchestrates the entire test workflow, initializing browser context, navigating to the app, and handling GPS/controls setup.

### `findings dictionary`

Tracks test results (timestamp, location, issues, successes) for reporting.

## Usage

1. Run with `python3 test_home_flight_browser.py`.
2. The script launches Chrome in non-headless mode, interacts with a local drone app at `http://localhost:5007`, and logs test outcomes.
3. Modify `HOME_LAT`/`HOME_LON` or add custom error handling for app-specific UI elements.

## Dependencies

> `playwright (async_playwright)`
> `asyncio`
> `datetime`

## Related

- [[test_drone_flight_api]]
- [[drone_control_webapp]]

>[!INFO] Important Note
> The script assumes the drone app is running on `localhost:5007` and uses Playwright’s async API for browser automation. Headless mode is disabled (`headless=False`) for debugging visibility.

>[!WARNING] Caution
> If the app’s UI changes (e.g., GPS dropdown or controls text), update the `page.locator()` selectors to avoid failures. Timeout values (e.g., `wait_for_timeout`) may need adjustment for latency.
