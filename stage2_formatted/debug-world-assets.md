**Tags:** #automated-testing, #puppeteer, #web-scraping, #debugging, #frontend-analysis, #localhost, #chrome-headless
**Created:** 2026-01-13
**Type:** code-notes

# debug-world-assets

## Summary

```
Automated debugging tool for inspecting a local web application's World Assets page after login.
```

## Details

> This script uses Puppeteer to automate browser interaction with a local web application (running on `localhost:8443`). It logs into the system using predefined test credentials, navigates to the World Assets page, and performs a structured inspection of the rendered HTML elements. The script evaluates asset cards, badges, key features, and checks for raw JSON data within the page content to extract debugging insights.

## Key Functions

### `DebugWorldAssets.runDebug()`

Orchestrates the entire debugging workflow—browser launch, login, navigation, and page inspection.

### `page.evaluate()`

Executes JavaScript in the browser context to dynamically query and analyze DOM elements.

### `page.goto()`

Navigates to specified URLs with network idle waits for reliability.

### `page.type()`

Simulates typing into input fields with controlled delays.

### `page.click()`

Simulates button submissions for login.

## Usage

1. Install dependencies (`npm install puppeteer`).
2. Run the script directly (`node debug-world-assets.js`).
3. Ensure the target application (`localhost:8443`) is running and accessible.

## Dependencies

> `puppeteer`
> `Google Chrome (local executable path specified).`

## Related

- [[Debugging Framework Notes]]
- [[Puppeteer Best Practices]]

>[!INFO] Important Note
> The script uses Chrome’s local executable path (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`) for cross-platform compatibility. Adjust this path if running on a non-Mac system.

>[!WARNING] Caution
> Avoid running this in production environments. The `--disable-web-security` flag bypasses security checks and may expose vulnerabilities. Use only in controlled test environments.
