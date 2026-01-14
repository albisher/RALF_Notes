**Tags:** #automated-testing, #web-scraping, #puppeteer, #tailwindcss, #frontend-verification
**Created:** 2026-01-13
**Type:** code-test

# style-verification-test

## Summary

```
Automated UI style verification for Tailwind CSS components using Puppeteer to check computed styles and detect overrides.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a local dashboard, and verify Tailwind CSS styling by inspecting computed styles of key elements. It checks for padding, card borders, text formatting, grid layouts, and detects potential Vuetify interference. The test captures screenshots and logs style discrepancies for debugging.

## Key Functions

### `testTailwindStyling()`

Core async function that launches a browser, verifies Tailwind classes, and logs style results.

### `uiChecksDir creation`

Dynamically creates `ui-checks` directory for storing screenshots.

### `Error handling`

Catches and logs Puppeteer/Node.js exceptions with exit codes.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Run script (`node style-verification-test.js`).
3. Verify Tailwind styles in console output and screenshots in `ui-checks/`.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Tailwind CSS Documentation]]
- [[Puppeteer API Reference]]

>[!INFO] Important Note
> The script assumes the dashboard runs on `localhost:8443` and uses placeholder credentials (`test/testpass`). Adjust URLs/credentials for your environment.

>[!WARNING] Caution
> Headless mode is disabled (`--no-sandbox` flags may require elevated permissions on Linux. Use `--headless: true` for CI environments.
