**Tags:** #debugging, #puppeteer, #web-scraping, #automation, #world-creation, #test-inputs, #api-interaction
**Created:** 2026-01-13
**Type:** code-notes

# debug-world-creation

## Summary

```
Debugs and automates the creation of a virtual world in a web application using Puppeteer for browser automation.
```

## Details

> This script automates the process of creating a new world in a web application by:
> 1. Launching a headless browser with Puppeteer.
> 2. Capturing console logs, network requests, and API interactions.
> 3. Taking screenshots at key steps for debugging.
> 4. Navigating through the dashboard, locating and clicking the "Create World" button.
> 5. Filling form fields (world name and description) using test IDs.
> 6. Submitting the form and verifying the creation via UI confirmation.
> 7. Logging completion status and saving screenshots to a directory.
> 
> The script includes error handling for missing elements and logs detailed debugging information.

## Key Functions

### `debugWorldCreation()`

Orchestrates the entire world-creation workflow.

### `takeScreenshot(name)`

Captures a screenshot at a specified step with timestamped filename.

### `page.on('console', msg)`

Logs browser console messages for debugging.

### `page.on('request')/page.on('response')`

Monitors and logs API requests/responses.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Run the script (`node debug-world-creation.js`).
3. Ensure the web app is running locally at `http://localhost:5173/`.
4. Verify test IDs (`data-testid`) match the target application.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Debugging UI Elements]]
- [[World Creation API Spec]]

>[!INFO] Important Note
> The script assumes the target UI uses `data-testid` attributes for form elements. If these IDs differ, update selectors in the script.

>[!WARNING] Caution
> Disable browser security flags (`--disable-web-security`) only for development/testing. Avoid running in production environments.
