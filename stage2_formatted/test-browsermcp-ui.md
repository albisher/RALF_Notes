**Tags:** #Playwright, #Browser Automation, #UI Testing, #Frontend Verification, #Localhost Testing
**Created:** 2026-01-13
**Type:** code-notes

# test-browsermcp-ui

## Summary

```
Automated UI verification script for a local web application using Playwright's Chromium browser.
```

## Details

> This script launches a Playwright Chromium browser instance, navigates to `http://localhost:5174`, and performs automated UI verification. It handles optional login, checks world selection, and tests interactive tabs (Link, Card, Timeline, Story, Generate). The script captures screenshots at key steps and logs progress, with error handling and cleanup.

## Key Functions

### ``testUI()``

Main async function that orchestrates browser launch, navigation, UI interactions, and verification.

### ``page.goto()``

Navigates to the target URL with network idle wait.

### ``page.$()``

Locates elements by CSS selector (e.g., login button, stage tabs).

### ``page.selectOption()``

Selects a dropdown option (e.g., "Zephyros Prime").

### ``page.screenshot()``

Captures page state as PNG files for debugging.

## Usage

1. Install dependencies: `npm install playwright`.
2. Run script: `node test-browsermcp-ui.js`.
3. Verify UI behavior by checking logs and screenshots (e.g., `browsermcp-01-login.png`).

## Dependencies

> `playwright`
> `playwright/chromium`

## Related

- [[Playwright Documentation]]
- [[Localhost Testing Guide]]

>[!INFO] Important Note
> The script assumes the target app (`http://localhost:5174`) is running. If not, it will fail with a network error. Ensure credentials (`'a'`/`'spq8'`) match the app’s login requirements.

>[!WARNING] Caution
> Headless mode is disabled (`headless: false`). Close the browser manually after execution to avoid resource leaks. Use `headless: true` for CI/CD environments.
