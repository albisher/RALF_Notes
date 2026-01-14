**Tags:** #authentication, #debugging, #puppeteer, #testing, #frontend
**Created:** 2026-01-13
**Type:** code-notes

# auth-debug-check

## Summary

```
Debugs authentication workflow by testing login, capturing screenshots, and verifying token state across pages.
```

## Details

> This script uses Puppeteer to automate a debugging workflow for authentication in a frontend application. It launches a browser in non-headless mode, navigates through login, captures screenshots at key stages, and evaluates localStorage tokens before/after login. The workflow includes:
> 1. Logging in with predefined credentials
> 2. Capturing UI screenshots at login, before/after submission, and on target pages
> 3. Evaluating token state via `localStorage` at multiple stages
> 4. Testing a direct API call with the extracted token
> 
> The script relies on a `CheckHelper` utility for result tracking and screenshot management, and uses Puppeteer's event listeners for console/network logging.

## Key Functions

### ``runAuthDebugCheck()``

Main async function orchestrating the entire debugging workflow.

### ``CheckHelper``

Utility class for result logging and screenshot capture.

### ``page.evaluate()``

Executes JavaScript in the browser context to inspect localStorage.

### ``page.goto()``

Navigates to specified URLs with configurable wait times.

### ``page.$()``

Selects DOM elements for interaction (email/password fields, login button).

## Usage

1. Install dependencies: `npm install puppeteer chalk`
2. Configure `./config` with frontend URLs and timeout settings
3. Run script: `node auth-debug-check.js`
4. Observe console output and screenshots for debugging insights

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `utils/check-helper (local)`

## Related

- [[Authentication Debugging Workflow]]
- [[Puppeteer Automation Guide]]

>[!INFO] Important Note
> The script uses hardcoded credentials (`user@spacepearl.com`, `password123`) for testing. In production, replace with dynamic inputs or environment variables.

>[!WARNING] Caution
> Running in non-headless mode may expose browser UI to manual inspection. Ensure proper security context when debugging production systems.

>[!INFO] Debug Tip
> The `page.on('console', msg => ...)` listener captures all browser console output, which can reveal hidden errors or warnings during authentication flow.

>[!WARNING] Token Exposure
> The script logs truncated tokens (first 50 chars) but does not securely handle them. Avoid logging full tokens in production environments.
