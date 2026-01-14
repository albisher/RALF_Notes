**Tags:** #UI-Verification, #Automated-Testing, #Puppeteer, #Frontend-Testing, #Screenshots
**Created:** 2026-01-13
**Type:** test-reference

# test-ui-verification

## Summary

```
Automated UI verification script using Puppeteer to test a web application's login flow and stage navigation with screenshot capture.
```

## Details

> This script automates UI verification for a web application running on `http://localhost:5174`. It uses Puppeteer to launch a browser, navigate through the application, and capture screenshots at key stages. The script verifies login functionality, checks world selection, and tests navigation through multiple stages (Generate, Link, Card, Timeline, Story) by examining URL hashes and visual elements. It includes error handling for failed login attempts and logs the number of found UI elements (e.g., cards, timeline markers).

## Key Functions

### `takeScreenshot(page, name, description)`

Captures a screenshot of the current page and saves it to a directory with a specified filename and description.

### `wait(ms)`

Pauses execution for a given milliseconds using `setTimeout`.

### `verifyUI()`

Orchestrates the entire UI verification workflow:

## Usage

1. Install dependencies: `npm install puppeteer fs path`.
2. Run the script: `node test-ui-verification.js`.
3. Ensure the application is running on `http://localhost:5174` before execution.
4. The script creates a `ui-verification-screenshots` directory to store screenshots.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the application has a `world` selector after login. If not found, it logs a failure and exits early.
>

>[!WARNING] Caution
> The script uses `headless: 'new'` in Puppeteer, which may not work in all environments. Ensure the browser flags (`--no-sandbox`, `--disable-setuid-sandbox`) are compatible with your system.
> The script does not handle dynamic content loading beyond what is explicitly waited for (e.g., `waitForSelector`). For complex pages, additional waits may be needed.
