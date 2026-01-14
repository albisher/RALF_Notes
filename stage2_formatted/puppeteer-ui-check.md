**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-validation, #database-testing
**Created:** 2026-01-13
**Type:** code-notes

# puppeteer-ui-check

## Summary

```
Automated UI validation script using Puppeteer to test login, page navigation, content extraction, and database functionality.
```

## Details

> This script automates UI checks for a web application using Puppeteer to:
> 1. Launch a browser, navigate to the application, and capture initial screenshots.
> 2. Attempt a login with predefined credentials and verify navigation.
> 3. Check multiple pages (Dashboard, Timeline, Characters, Elements) for content, taking screenshots and extracting metadata (title, headings, text, element count).
> 4. Validate expected content in specific pages (e.g., Timeline for historical events, Characters for robot data).
> 5. Test database functionality by generating and saving test data via a modal.
> 
> The script logs progress and errors, storing results in a structured `results` object for analysis.

## Key Functions

### ``performUICheck()``

Orchestrates the entire UI validation workflow.

### ``page.goto()``

Navigates to specified URLs with `networkidle2` wait strategy.

### ``page.screenshot()``

Captures full-page screenshots for debugging.

### ``page.evaluate()``

Extracts dynamic page content (title, headings, text, element count).

### ``expectedEvents.filter()``

Compares extracted content against predefined expected values (e.g., timeline events, characters).

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run the script: `node puppeteer-ui-check.js`.
3. Ensure the target application is running at `https://localhost:8443`.
4. Modify `expectedEvents`/`expectedCharacters` or `pagesToCheck` arrays as needed.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Documentation for Puppeteer API]]
- [[Example UI Automation Scripts]]

>[!INFO] Important Note
> The script assumes the target application uses `input[name="username"]`/`input[name="password"]` for login. Adjust selectors if the form structure differs.

>[!WARNING] Caution
> Running in headless mode (`--no-sandbox`) may expose security risks. Use only in trusted environments. The script logs all actions to console; avoid sensitive data in test credentials.
