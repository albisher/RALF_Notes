**Tags:** #automated-testing, #web-ui-testing, #puppeteer, #ui-functional-test, #world-deletion
**Created:** 2026-01-13
**Type:** code-notes

# test-ui-world-delete

## Summary

```
Automated UI test for deleting a world from a web application using Puppeteer.
```

## Details

> This script automates the process of testing the deletion functionality of a world in a web application. It launches a headless browser, navigates to the worlds page, identifies a world to delete (excluding a predefined name), triggers the deletion process, and verifies the deletion via screenshots and UI checks. The test logs each step and captures visual evidence of the process.
> 
> The script uses Puppeteer to interact with a web application running on `localhost:8443`, specifically targeting the worlds page. It handles SSL errors, bypasses CSP, and captures screenshots at key stages (initial page, confirmation dialog, and post-deletion). The test ensures the UI correctly displays a delete confirmation dialog and verifies the world is removed from the list.

## Key Functions

### `testUIWorldDelete`

Orchestrates the entire deletion test workflow, including browser launch, UI interaction, and screenshot capture.

### `puppeteer.launch`

Configures and starts a headless Chrome browser with security and performance tweaks.

### `page.evaluateHandle`

Dynamically queries the DOM for delete buttons and world names to identify targets for deletion.

### `page.goto`

Navigates to the worlds page endpoint (`/worlds`).

### `page.screenshot`

Captures visual snapshots at critical stages for debugging and verification.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node test-ui-world-delete.js`.
3. Ensure the web application is running on `localhost:8443` and accessible via the specified endpoint.
4. The script will:
   - Launch a browser, navigate to the worlds page, and take initial screenshots.
   - Identify a world to delete (excluding "Space Peral").
   - Trigger the delete process, confirm deletion, and capture post-deletion screenshots.
   - Log results and exit if any step fails.

## Dependencies

> `puppeteer`
> `https (built-in Node.js module)`

## Related

- [[None]]

>[!INFO] Important Note
> This script assumes the web application uses Arabic text for delete buttons (e.g., "حذف"). Adjust the filter logic (`btn.textContent.includes('حذف')`) if the UI uses different text.
>

>[!WARNING] Caution
> Running in headless mode with `--disable-web-security` may expose the application to security risks if not used in a controlled environment. Ensure the target application is secure before executing this script.
