**Tags:** #automated-web-testing, #puppeteer, #user-simulation, #web-scraping, #interactive-web-app
**Created:** 2026-01-13
**Type:** code-notes

# user-simulation-demo

## Summary

```
Automated user simulation for testing a web application (likely "ملاحم") by interacting with it programmatically via Puppeteer.
```

## Details

> This script uses Puppeteer to simulate a user interacting with a web application hosted locally (likely a frontend framework like React). It follows a structured workflow:
> 1. **Browser Launch**: Opens a browser in non-headless mode with customizable viewport settings.
> 2. **Screenshot Capture**: Automatically creates a directory for screenshots and takes snapshots at key steps.
> 3. **User Flow**: Navigates through the app by clicking buttons, filling input fields, and saving data, with fallback logic for missing elements.
> 4. **Error Handling**: Logs missing elements gracefully and retries with alternative selectors.
> 
> The script is designed to test user interactions (e.g., creating a "world" and character) and captures visual feedback via screenshots.

## Key Functions

### `userSimulationDemo`

Orchestrates the full user simulation workflow.

### `takeScreenshot`

Captures a screenshot at a given step with timestamped filename.

### `createWorldButton`

Locates and clicks the "Create World" button (with fallback logic).

### `fillInputFields`

Dynamically identifies and populates input fields (name/description) based on placeholder/text content.

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Run the script (`node user-simulation-demo.js`).
3. Ensure the target app (`http://localhost:5173`) is running.
4. Modify selectors (e.g., `button:has-text`) if the UI changes.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[None]]

>[!INFO] Important Note
> The script uses `--disable-web-security` and `--disable-sandbox` flags, which may expose the browser to security risks. Use only in controlled environments (e.g., testing).

>[!WARNING] Caution
> Localhost navigation assumes the app is running on port 5173. If the URL changes, update the `page.goto()` calls accordingly.
