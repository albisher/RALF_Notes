**Tags:** #screenshot, #automation, #ui-testing, #map-generation, #verification, #playwright
**Created:** 2026-01-13
**Type:** code-script

# take_map_verification_screenshots

## Summary

```
Generates and saves UI verification screenshots for map generation workflows.
```

## Details

> This script dynamically creates a timestamped directory structure (`YYYYMMDD/HHMM`) under `screenshots/map_generation_ui_tests/` to store screenshots of map generation UI elements. It relies on Playwright for browser automation and verifies UI consistency by capturing screenshots at predefined intervals. The script provides fallback instructions for manual screenshot handling if Playwright is unavailable.

## Key Functions

### ``SCREENSHOT_DIR``

Creates a structured path for saving screenshots using current date/time.

### `Directory creation`

Automatically generates and ensures the screenshot directory exists.

### `Playwright dependency check`

Displays installation instructions for Playwright.

## Usage

1. Run the script in a directory with Playwright installed.
2. It will create a timestamped folder under `screenshots/map_generation_ui_tests/`.
3. For manual use, copy screenshots into the generated folder structure.

## Dependencies

> `playwright`
> `chromium (via `playwright install chromium`)`

## Related

- [[Manual Screenshot Instructions]]
- [[Playwright Installation Guide]]

>[!INFO] Important Note
> The script assumes Playwright is installed and configured. If not, it provides alternative manual workflows.

>[!WARNING] Caution
> Ensure the target browser (default: Chromium) is running before executing the script to avoid empty screenshots.
