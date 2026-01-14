**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #api-integration, #console-logging, #screenshot-capture
**Created:** 2026-01-13
**Type:** code-notes

# comprehensive-user-test

## Summary

```
Automated UI and API test suite for a web application using Puppeteer to validate user workflows.
```

## Details

> This script performs a comprehensive user test for a web application (likely a game or creative platform) by:
> 1. Launching a headless browser with Puppeteer
> 2. Capturing console logs, network requests, and API interactions
> 3. Automating a multi-step workflow:
>    - Dashboard navigation
>    - Creating a new world with name/description
>    - Verifying world creation
>    - Testing workspace functionality
> 4. Taking screenshots at each step for debugging
> The test focuses on UI interaction and data validation without requiring manual user input.

## Key Functions

### ``comprehensiveUserTest()``

Main async function orchestrating the entire test workflow.

### ``takeScreenshot(name)``

Helper function to capture page snapshots with timestamps.

### ``page.on('console', ...)``

Listener for browser console messages.

### ``page.on('request/response', ...)``

Intercepts and logs API traffic.

## Usage

```bash
node comprehensive-user-test.js
```
Run from project directory where screenshots directory is created automatically.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Test-Suite-Setup]]
- [[API-Endpoints-Reference]]

>[!INFO] Important Note
> The script uses aggressive Puppeteer launch options (`--disable-web-security`) that may break security in production environments. Use only in controlled test environments.

>[!WARNING] Caution
> Network requests are logged but not validated against expected responses. Verify API responses match test expectations for full reliability.
