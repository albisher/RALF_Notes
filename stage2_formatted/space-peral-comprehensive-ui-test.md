**Tags:** #automated-testing, #ui-testing, #puppeteer, #web-testing, #space-peral, #e2e-test
**Created:** 2026-01-13
**Type:** code-notes

# space-peral-comprehensive-ui-test

## Summary

```
Automated UI test suite for Space Peral application using Puppeteer to validate user interface functionality, including login, workspace navigation, and world management.
```

## Details

> This script performs a comprehensive end-to-end (E2E) UI test for the Space Peral application using Puppeteer. It launches a headless browser, navigates to the application, handles potential login, and verifies key UI elements such as world selection and workspace navigation. The test captures screenshots at critical points and logs network requests and console errors for debugging. It dynamically checks for UI elements like login buttons, workspace links, and world selectors, with fallback logic to create missing worlds if necessary.
> 
> The script includes conditional logic to detect and interact with UI components based on text content, ensuring robustness across different UI states. It logs detailed progress and issues, such as missing elements or failed operations, and captures visual evidence via screenshots.

## Key Functions

### `testSpacePeralComprehensiveUI`

Orchestrates the entire test workflow, including browser launch, navigation, UI interaction, and screenshot capture.

### `login workflow`

Automates login by detecting login buttons, filling credentials, and submitting the form.

### `workspace navigation`

Attempts to navigate to the Writing Workspace and captures its screenshot if the link is found.

### `world selection/creation`

Checks for the Space Peral world in dropdowns, and creates it if missing by navigating to the worlds page and clicking the "Add World" button.

### `screenshot capture`

Takes full-page screenshots at key stages (initial page and workspace) for visual verification.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node space-peral-comprehensive-ui-test.js`.
3. Ensure the Space Peral application is running locally on `https://localhost:8443`.
4. The script will log progress and save screenshots to `checks/screenshots/`.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Space Peral API Documentation]]
- [[Puppeteer Test Framework Guide]]

>[!INFO] Important Note
> The script uses a hardcoded username/password (`test`/`passtest`) for login. In production, replace these with environment variables or a secure credential provider to avoid hardcoding sensitive data.


>[!WARNING] Caution
> The browser launch configuration includes disabling security features (`--disable-web-security`, `--ignore-ssl-errors`), which may not be suitable for production environments. Use only in controlled test environments.
