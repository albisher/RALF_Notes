**Tags:** #automation, #web-scraping, #puppeteer, #ui-testing, #game-dev, #world-building
**Created:** 2026-01-13
**Type:** code-notes

# ui-space-peral-creation

## Summary

```
Automates UI-based creation of a Space Peral virtual world via Puppeteer, including world setup, robots, ecosystems, and story elements.
```

## Details

> This script uses Puppeteer to automate interactions with a Space Peral application (likely a game or simulation) via its web UI. It launches a browser, navigates through the application, and performs sequential UI actions to create a fully functional world. The script includes error handling, screenshot capture at key steps, and modular functions for each creation phase (e.g., world setup, robot deployment, plant/animal/building creation).
> 
> The workflow follows a structured sequence:
> 1. **Launch browser** and set up screenshots directory.
> 2. **Load the application** (e.g., Space Peral) and wait for auto-login.
> 3. **Create a world** by filling in a name and description, then clicking "Create."
> 4. **Proceed through subsequent steps** (workspace navigation, robot creation, ecosystem elements, story writing, and saving) using predefined UI selectors and inputs.

## Key Functions

### `createSpacePeralWorldViaUI`

Orchestrates the entire automation workflow.

### `createWorld(page, takeScreenshot)`

Finds and interacts with the "Create World" button, fills the form, and submits it.

### `navigateToWorkspace(page, takeScreenshot)`

Locates and clicks the workspace link.

### `createXSeriesRobots(page, takeScreenshot)`

Iterates through a predefined list of X-Series robots, likely using seed values or predefined inputs.

### `createPlantsAndAnimals(page, takeScreenshot)`

*(Incomplete in snippet; assumes similar logic for filling form fields.)*

### `createBuildings(page, takeScreenshot)`

*(Incomplete; likely follows a similar pattern.)*

### `writeStory(page, takeScreenshot)`

*(Incomplete; likely fills a text area with a predefined story.)*

### `saveEverything(page, takeScreenshot)`

*(Incomplete; likely saves progress or triggers final actions.)*

## Usage

1. Install dependencies (`npm install puppeteer fs path`).
2. Modify the `robots` array or other inputs (e.g., world name, story text) as needed.
3. Run the script (`node ui-space-peral-creation.js`).
4. Ensure the Space Peral application is running locally on `http://localhost:5173`.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Space Peral Application Documentation]]
- [[Puppeteer Automation Guide]]

>[!INFO] Important Note
> The script assumes the UI structure (e.g., button/textarea selectors) remains consistent. If the application updates its DOM, selectors may break. Consider using dynamic waits or error handling for robustness.


>[!WARNING] Caution
> Running Puppeteer in non-headless mode (`--no-sandbox`) may expose security risks if not used in a controlled environment. Avoid executing this script on systems without proper sandboxing or user permissions.
