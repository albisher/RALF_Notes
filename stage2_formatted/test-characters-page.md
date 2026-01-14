**Tags:** #automated-testing, #puppeteer, #web-scraping, #frontend-validation, #error-handling
**Created:** 2026-01-13
**Type:** code-test

# test-characters-page

## Summary

```
Automated test script using Puppeteer to validate the Characters page functionality of a web application.
```

## Details

> This script launches a headless Chrome browser, navigates to the Characters page (`http://localhost:5173/characters`), and performs a series of checks to verify the page's structure and content. It captures screenshots, logs console errors, and validates the presence of key elements like the page title, loading indicators, empty states, character grids, and add buttons. The test also checks for specific text (e.g., "Characters," "Search") and error messages. If errors occur, it attempts to save an error screenshot before closing the browser.

## Key Functions

### `testCharactersPage()`

Main async function that orchestrates browser launch, page navigation, and validation checks.

### `console.log()`

Used for logging test progress, element existence, and error details.

### `page.goto()`

Navigates to the Characters page with configurable wait and timeout settings.

### `page.screenshot()`

Captures screenshots of the page (success or error state).

### `page.$eval() and page.$()`

Locates and extracts text/content from DOM elements.

### `page.evaluate()`

Executes JavaScript in the context of the page to check for dynamic content.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-characters-page.js`.
3. The script logs results to the console and saves screenshots to `checks/screenshots/`.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[None]]

>[!INFO] Important Note
> The script uses a headless browser with aggressive security flags (`--no-sandbox`, `--disable-web-security`) for stability, which may not be suitable for production environments. Consider using a non-headless mode or a more secure sandbox for real-world testing.


>[!WARNING] Caution
> If the target page (`http://localhost:5173/characters`) is not accessible or the browser fails to launch, the test will fail. Ensure the server is running and the port is correct before execution. The script does not handle network timeouts gracefully beyond the `timeout` parameter in `page.goto()`.
