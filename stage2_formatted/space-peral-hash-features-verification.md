**Tags:** #automated-testing, #web-scraping, #puppeteer, #functional-verification, #hash-feature-validation
**Created:** 2026-01-13
**Type:** code-notes

# space-peral-hash-features-verification

## Summary

```
Verifies the implementation of hash-related features in a Space Peral application by automating browser interactions, screenshot capture, and DOM inspection.
```

## Details

> This script uses Puppeteer to automate browser interactions for verifying hash feature functionality in a Space Peral application. It launches a headless browser, navigates to the application, handles login, and proceeds to the Writing Workspace. The script captures screenshots of the workspace and asset creation interface, then evaluates the DOM for hash-related UI elements (e.g., asset types, hash generation sections, seed inputs, and preview buttons). It logs progress and checks for specific UI patterns like the presence of "+" buttons or Arabic/English text indicating hash-related actions.

## Key Functions

### `verifySpacePeralHashFeatures`

Orchestrates the entire verification workflow, including browser setup, navigation, DOM inspection, and screenshot capture.

### `login logic`

Detects and automates login via `page.evaluateHandle` to locate and click login buttons, fill credentials, and submit the form.

### `workspace navigation`

Finds and clicks the Writing Workspace link using `page.evaluateHandle`.

### `DOM inspection`

Extracts hash-related features via `page.evaluate` to identify asset types, hash generation sections, seed inputs, and preview buttons.

### `screenshot capture`

Records visual verification of the workspace and asset creation interface.

## Usage

1. Install Puppeteer: `npm install puppeteer`.
2. Run the script: `node space-peral-hash-features-verification.js`.
3. Ensure the application is running locally at `https://localhost:8443` and accessible from the script’s network context.
4. Verify screenshots are saved in `checks/screenshots/` (adjust paths if needed).

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Space Peral Application Architecture]]
- [[Puppeteer Test Framework]]

>[!INFO] Important Note
> The script assumes the application uses a Material Design-like UI (e.g., `.v-select`, `.character-generation-section`). If the DOM structure differs, adjust selectors in `page.evaluateHandle` or `page.evaluate` calls.
>

>[!WARNING] Caution
> Headless browser flags (`--no-sandbox`, `--disable-web-security`) may bypass security checks. Use cautiously in production environments. The script ignores HTTPS errors (`ignoreHTTPSErrors: true`), which could expose security risks if misconfigured.
