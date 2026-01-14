**Tags:** #automation, #web-scraping, #puppeteer, #ui-testing, #session-management
**Created:** 2026-01-13
**Type:** code-notes

# user-session-1-create-world

## Summary

```
Automates UI-based creation of a world session in a web application using Puppeteer.
```

## Details

> This script automates the process of navigating to a web dashboard, locating and interacting with UI elements (buttons and input fields) to create a new world. It uses Puppeteer to launch a headless browser, interact with the UI, and capture screenshots at each step. The script logs actions and errors, ensuring debugging and verification of UI interactions.
> 
> The workflow involves:
> 1. Launching a browser and navigating to the dashboard.
> 2. Locating and clicking the "Create World" button.
> 3. Filling input fields for world name and description.
> 4. Finding and clicking a save/submit button.
> 5. Verifying the creation of the world (though partial due to truncation in the snippet).

## Key Functions

### `createWorldSession`

Orchestrates the entire UI automation workflow.

### `takeScreenshot`

Captures full-page screenshots with timestamps for debugging.

### `page.goto`

Navigates to the web application URL with configurable wait times.

### `page.$$ and page.evaluate`

Locates and inspects UI elements dynamically.

## Usage

1. Install dependencies: `npm install puppeteer fs path`.
2. Run the script: `node user-session-1-create-world.js`.
3. Ensure the web application is running locally at `http://localhost:5173/`.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[None]]

>[!INFO] Important Note
> The script assumes the web application is running on `localhost:5173`. Adjust the URL if needed.

>[!WARNING] Caution
> Running Puppeteer in headless mode with disabled security flags (`--disable-web-security`) may expose the browser to security risks. Use cautiously in production environments.
