**Tags:** #automated-testing, #web-scraping, #puppeteer, #visual-verification, #database-validation, #frontend-testing
**Created:** 2026-01-13
**Type:** code-notes

# visual-database-proof

## Summary

```
Automated visual database proofing tool for verifying a web application's database content via Puppeteer.
```

## Details

> This script uses Puppeteer to interact with a local web application (likely a frontend built with Vite) and performs automated visual validation of database-related content. It captures screenshots at key steps to confirm the application displays expected data (e.g., worlds, characters) and logs findings. The tool checks for specific text patterns (e.g., "Cyberpunk Neo-Tokyo") and navigates through dashboard, worlds, and characters pages.

## Key Functions

### `visualDatabaseProof`

Orchestrates the entire workflow, including browser launch, navigation, and screenshot capture.

### `takeScreenshot`

Captures full-page screenshots with timestamped filenames.

### `page.goto()`

Navigates to specified URLs with configurable wait times.

### `page.$$()`

Selects multiple elements by CSS selectors (e.g., stats/cards).

### `page.evaluate()`

Executes JavaScript in the context of the page to extract text content.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Run the script (`node visual-database-proof.js`).
3. The script logs findings and saves screenshots to a `screenshots/database-proof` directory.
4. Modify `page.goto()` URLs or selectors to target specific application paths.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Visual Testing Framework]]
- [[Web Application Debugging Guide]]

>[!INFO] Important Note
> The script assumes the application is running on `http://localhost:5173`. Adjust paths if the app uses a different endpoint.
>

>[!WARNING] Caution
> Disabling security flags (`--disable-web-security`) may expose the browser to security risks. Use only in controlled environments.
