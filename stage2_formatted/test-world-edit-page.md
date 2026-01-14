**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #world-edit-page
**Created:** 2026-01-13
**Type:** code-test

# test-world-edit-page

## Summary

```
Automated UI test suite for verifying the World Edit Page functionality in a web application using Puppeteer.
```

## Details

> This script automates interactions with a web application’s World Edit Page, including login, navigation, section verification, form field manipulation, and button interactions. It captures screenshots at key stages to document the UI state and validates the presence of expected elements (e.g., "Advanced Edit" button, time system fields). The test sequence covers basic workflows like editing a world, adding configurations (time periods, biomes, planets), and handling save/cancel actions.
> 
> The script uses Puppeteer to control a browser instance, interacts with the frontend via selectors, and logs progress via console output. It also saves screenshots to a `checks/screenshots` directory for visual verification.

## Key Functions

### `testWorldEditPage`

Orchestrates the full test workflow, from login to form interactions and screenshot capture.

### `puppeteer.launch`

Initializes a browser instance with customizable settings (headless mode disabled, sandbox bypass).

### `page.goto`

Navigates to the application’s landing page (`http://localhost:5173`).

### `page.screenshot`

Captures full-page screenshots at predefined steps.

### `page.$/page.$$('.world-card')`

Locates and interacts with UI elements (e.g., buttons, input fields) using CSS selectors.

### `page.type/click`

Simulates user input and clicks for login, form edits, and navigation.

### `page.waitForTimeout`

Introduces delays to ensure page states stabilize (e.g., after login or button clicks).

## Usage

1. Install dependencies: `npm install puppeteer fs path`.
2. Run the script: `node test-world-edit-page.js`.
3. Ensure the web app is running locally at `http://localhost:5173` before execution.
4. Verify credentials (`test@spacepearl.com`, `testpass`) match the target system.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the target application uses specific selectors (e.g., `button[type="submit"]`, `.world-card`) and section names (e.g., "Basic Information"). Adjust selectors if the UI structure changes.

>[!WARNING] Caution
> Avoid running this in production environments without proper sandboxing (e.g., `--disable-setuid-sandbox` may be unsafe in restricted contexts). Test in a controlled environment first.
