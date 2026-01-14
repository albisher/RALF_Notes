**Tags:** #automated-testing, #puppeteer, #web-scraping, #character-editing, #ui-testing
**Created:** 2026-01-13
**Type:** code-test

# test-character-editing

## Summary

```
Automated test script to verify character editing functionality in a web application using Puppeteer.
```

## Details

> This script uses Puppeteer to launch a headless browser, navigate to a characters page, and verify the presence of edit buttons and an editing dialog. It captures screenshots before and after clicking an edit button, checks for form fields (name, description, role), and logs the findings. The test handles cases where no characters or edit buttons are found gracefully.
> 
> The script logs detailed progress via console output, including counts of character cards and edit buttons, and evaluates UI elements dynamically using `page.evaluateHandle()`. It captures network requests and console errors for debugging.

## Key Functions

### `testCharacterEditing`

Orchestrates the entire test workflow, including browser launch, navigation, UI interaction, and screenshot capture.

### `page.on('request')`

Tracks API calls made during the test.

### `page.on('console')`

Captures console errors for debugging.

### `page.evaluateHandle()`

Dynamically queries and interacts with the DOM to locate edit buttons and form fields.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-character-editing.js`.
3. Ensure the target application is running at `https://localhost:8443/characters`.
4. Adjust screenshot paths (`checks/screenshots/...`) as needed.

## Dependencies

> `puppeteer`
> `fs (Node.js built-in for file operations like screenshot paths).`

## Related

- [[Character Editing Documentation]]
- [[Puppeteer Test Framework Guide]]

>[!INFO] Important Note
> The script assumes the target application uses Material Design components (e.g., `.v-card`, `.v-dialog`). If the UI differs, adjust selectors (e.g., `button` or `input` classes) accordingly.
>

>[!WARNING] Caution
> Running in headless mode with `--disable-web-security` may expose the browser to security risks. Use only in controlled environments with HTTPS validation disabled for testing purposes.
