**Tags:** #automated-web-testing, #puppeteer, #web-scraping, #character-analysis, #session-testing
**Created:** 2026-01-13
**Type:** code-test

# puppeteer-session-3-characters

## Summary

```
Automated Puppeteer test script to verify and analyze a characters page for specific characters and content.
```

## Details

> This script uses Puppeteer to launch a browser, navigate to a characters page (likely a web application), and perform automated checks for the presence of specific characters (e.g., "Cyber-Samurai Kaito" and "Mr. Ha Bee"). It captures screenshots at key stages, extracts page content via `page.evaluate()`, and logs findings. The script also attempts to programmatically locate and click a character element if found. The results are returned as an object with boolean flags and extracted data.

## Key Functions

### `testCharactersPage()`

Main async function that orchestrates the entire session, including browser launch, page navigation, content analysis, and screenshot capture.

### `takeScreenshot(name)`

Helper function to capture a screenshot with a timestamped filename and save it to a directory.

### `page.evaluate()`

Extracts the inner text of the page body for analysis.

### `page.$$('*')`

Attempts to find all elements on the page to locate clickable character elements.

## Usage

1. Run the script directly (e.g., `node puppeteer-session-3-characters.js`).
2. The script will:
   - Launch a headless browser with custom Puppeteer options.
   - Navigate to `http://localhost:5173/characters`.
   - Capture screenshots at three stages: page load, analysis, and character click attempt.
   - Log results for character presence, count, and content.
   - Return an object with findings (e.g., `cyberSamuraiFound`, `characterCount`).
3. Screenshots are saved in a `screenshots/session-3-characters` directory.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[puppeteer-testing-guide]]
- [[web-scraping-best-practices]]

>[!INFO] Important Note
> The script assumes the target URL (`http://localhost:5173/characters`) is correct and accessible. If the page dynamically loads content, the `waitForTimeout` may not suffice—consider using `page.waitForSelector()` or `page.waitForFunction()` instead.


>[!WARNING] Caution
> Running Puppeteer in headless mode with `--disable-web-security` and `--disable-features=VizDisplayCompositor` may expose the browser to security risks. Use only in controlled environments with trusted sources. Always validate the target website’s terms of service before scraping.
