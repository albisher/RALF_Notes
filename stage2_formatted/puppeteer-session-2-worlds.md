**Tags:** #automated-web-testing, #puppeteer, #web-scraping, #worlds-page-analysis, #cyberpunk-game
**Created:** 2026-01-13
**Type:** code-test

# puppeteer-session-2-worlds

## Summary

```
Automated Puppeteer test to analyze and validate a "Worlds" page for a game, checking for specific worlds, counts, and interactive elements.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a "Worlds" page (likely for a game like *Cyberpunk*), and perform automated checks for:
> 1. **Text content** (e.g., presence of demo worlds like *Cyberpunk Neo-Tokyo 2087*).
> 2. **World-related metadata** (e.g., world count or list).
> 3. **Interactive elements** (e.g., clicking a world link).
> The script captures screenshots at key steps and returns structured validation results.

## Key Functions

### `testWorldsPage()`

Orchestrates the entire session, including browser launch, page navigation, analysis, and cleanup.

### `takeScreenshot(name)`

Captures a screenshot with a timestamped filename and logs success/failure.

### `Page navigation & content extraction`

Uses `page.evaluate()` to fetch `document.body.innerText` for text-based checks.

## Usage

1. Run the script directly (`node puppeteer-session-2-worlds.js`).
2. Ensure the target URL (`http://localhost:5173/worlds`) is accessible.
3. Outputs:
   - Console logs (status updates, errors, screenshots).
   - Screenshots saved in `screenshots/session-2-worlds/`.
   - Structured results object (e.g., `demoWorldFound`, `worldCount`).

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Puppeteer Test Suite]]
- [[Game World Data Validation]]

>[!INFO] Important Note
> The script assumes the target page contains Arabic text (e.g., "عالم" for "world"), but partial matches (e.g., "Cyberpunk Neo-Tokyo 2087") are case-insensitive. Adjust regex/string checks if the page structure varies.


>[!WARNING] Caution
> **Headless mode (`--headless: true`)** may fail if the page relies on non-headless-specific features. Test in non-headless mode first for debugging. Also, disable security flags (`--disable-web-security`) at your own risk for local development.
