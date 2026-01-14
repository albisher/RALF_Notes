**Tags:** #automated-testing, #web-scraping, #puppeteer, #hash-algorithms, #asset-management
**Created:** 2026-01-13
**Type:** code-test

# space-peral-comprehensive-hash-test

## Summary

```
Automated Puppeteer test suite for verifying hash and asset creation features in Space Peral’s Writing Workspace.
```

## Details

> This script uses Puppeteer to automate browser interactions with Space Peral’s application, focusing on:
> 1. Launching a headless browser with security bypass flags.
> 2. Logging in (if required) and navigating to the Writing Workspace.
> 3. Testing asset creation workflows and hash validation for different asset types.
> 4. Capturing screenshots at key stages for debugging/verification.
> 
> The test logs progress via `console.log` and captures screenshots of critical pages (initial login, workspace, and asset creator UI). It also monitors network requests and console errors for debugging.

## Key Functions

### ``testSpacePeralComprehensiveHashFeatures()``

Main async function orchestrating the entire test workflow.

### ``puppeteer.launch()``

Configures and starts a headless Chrome browser with security overrides.

### ``page.evaluateHandle()``

Executes JavaScript in the browser context to locate UI elements dynamically.

### ``page.screenshot()``

Captures full-page screenshots at predefined steps.

### ``page.on('request')`/`page.on('console')``

Listens for API calls and error logs for debugging.

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run the script: `node space-peral-comprehensive-hash-test.js`.
3. Ensure Space Peral is running locally at `https://localhost:8443/` with credentials (`test`/`passtest`).
4. Outputs screenshots in `checks/screenshots/` and logs progress to console.

## Dependencies

> `puppeteer`
> `Node.js runtime`

## Related

- [[Space Peral API Documentation]]
- [[Puppeteer Test Framework Guide]]

>[!INFO] Important Note
> The script uses `--disable-web-security` and ignores HTTPS errors for local testing. **Do not use this in production** without proper security hardening.
>

>[!WARNING] Caution
> Hardcoded credentials (`test`/`passtest`) may expose the application to unauthorized access. **Use environment variables** for production use.
