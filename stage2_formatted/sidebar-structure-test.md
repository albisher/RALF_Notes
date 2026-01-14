**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #sidebar-validation
**Created:** 2026-01-13
**Type:** code-notes

# sidebar-structure-test

## Summary

```
Automated UI test suite for verifying the structure and navigation of a sidebar menu in a web application.
```

## Details

> This script uses Puppeteer to automate browser interactions and validate the sidebar structure of a local web application running on `localhost:8443`. It performs tests on login, menu expansion, and submenu validation, capturing screenshots for verification. The test checks for the presence of specific menu items (e.g., "World Management," "Plant," "Building," "Character," and "Robot") and ensures proper navigation flow.
> 
> The test follows a structured approach:
> 1. **Login** to the application and capture a screenshot of the main page.
> 2. **Expand the Assets menu**, verify submenu items, and capture a screenshot.
> 3. **Expand the Character submenu**, check for nested items (e.g., "Robot"), and capture another screenshot.
> 4. **Validate navigation functionality** for deeper menu structures.

## Key Functions

### ``SidebarStructureTest``

Main class encapsulating the test logic.

### ``constructor()``

Initializes the base URL and screenshot directory.

### ``runTest()``

Orchestrates the entire test workflow (login, menu validation, screenshot capture).

### ``page.goto()``

Navigates to the login page.

### ``page.type()``

Simulates typing in login fields.

### ``page.click()``

Expands menu items (e.g., `.menu-header`, `.character-submenu`).

### ``page.screenshot()``

Captures UI snapshots for debugging.

### ``page.evaluate()``

Extracts dynamic text content from submenus (e.g., `.submenu-item`, `.nested-submenu-item`).

## Usage

1. Install dependencies:
   ```bash
   npm install puppeteer fs path
   ```
2. Run the script:
   ```bash
   node sidebar-structure-test.js
   ```
3. Verify screenshots in `./screenshots/ui-checks` and console logs for test results.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[UI Automation Framework]]
- [[Web Application Testing Guide]]

>[!INFO] Important Note
> The script assumes the target application uses CSS classes like `.sidebar-item`, `.menu-header`, `.submenu-item`, and `.nested-submenu-item`. Adjust selectors if the UI structure differs.

>[!WARNING] Caution
> Avoid running in headless mode (`headless: true`) if debugging UI layout issues. The script explicitly disables sandboxing (`--no-sandbox`) for compatibility with local development environments.
