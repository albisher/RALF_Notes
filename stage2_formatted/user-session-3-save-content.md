**Tags:** #automation, #web-scraping, #puppeteer, #session-testing, #content-persistence
**Created:** 2026-01-13
**Type:** code-test

# user-session-3-save-content

## Summary

```
Automated test script to verify content persistence in a user session using Puppeteer, checking if filled data (story and location) is saved and retrievable across pages.
```

## Details

> This script automates a user session workflow to test content saving functionality in a web application. It launches a headless browser, navigates through the workspace, fills a story and location input, triggers a save action, and verifies persistence across multiple pages (workspace, dashboard, and worlds). The script captures screenshots at key steps and logs results for validation. It uses Puppeteer for browser automation and Node.js for file operations.

## Key Functions

### `saveContentSession`

Orchestrates the entire session workflow, including browser setup, page navigation, content input, save action, and persistence checks.

### `takeScreenshot`

Captures a screenshot of the current page with a timestamped filename and logs success/failure.

### `page.goto()`

Navigates to specified URLs with configurable wait times.

### `page.evaluate()`

Executes JavaScript in the context of the page to extract content dynamically.

## Usage

1. Run the script in a Node.js environment.
2. Ensure the target web application (running on `http://localhost:5173`) is accessible.
3. The script creates a `screenshots/user-session-3-save-content` directory to store visual logs.
4. Modify placeholder text (e.g., story content) as needed for testing.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[User Session Test Framework]]
- [[Web Application API Documentation]]

>[!INFO] Important Note
> The script assumes the target application uses Arabic placeholders (`قصتك`, `إحداثيات`) for story and location inputs. Adjust selectors if the UI differs.

>[!WARNING] Caution
> Running in headless mode with disabled security flags (`--disable-web-security`) may expose the browser to security risks. Use only in controlled environments for testing.
