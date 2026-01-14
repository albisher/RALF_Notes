**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-verification, #localhost-testing
**Created:** 2026-01-13
**Type:** code-test

# test-new-app-name

## Summary

```
Automated UI verification script for a local web application using Puppeteer to test app name rendering and language switching.
```

## Details

> This script uses Puppeteer to launch a headless browser, navigate to a local Vue.js/Vite application (running on `localhost:5173`), and verify:
> - The rendered page title and app bar title (in the current language, Arabic in this case: "ملاحم").
> - The presence of a subtitle element (using multiple selectors as fallback).
> - Language switching functionality (clicking an Arabic/English button and verifying title updates).
> The script captures screenshots of both the original and language-switched views, then returns structured results or errors.

## Key Functions

### `testNewAppName()`

Orchestrates the entire test workflow (browser launch, UI checks, language switch, cleanup).

### `page.goto()`

Navigates to the local app URL with timeout and idle-network checks.

### `page.evaluate()`

Extracts text from DOM elements (title/subtitle) via CSS selectors.

### `page.screenshot()`

Captures full-page screenshots for debugging.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-new-app-name.js`.
3. Ensure the app is running locally at `http://localhost:5173`.
4. The script logs results to console and saves screenshots in a `screenshots/` folder.

## Dependencies

> `puppeteer`
> `node.js`

## Related

- [[Vue]]
- [[Puppeteer Best Practices]]

>[!INFO] Important Note
> The script assumes the app uses Vuetify (due to selectors like `.v-toolbar-title`). If the UI differs, adjust selectors accordingly.

>[!WARNING] Caution
> Headless mode (`--no-sandbox`) may not work on all systems. Test in a controlled environment with proper permissions.
