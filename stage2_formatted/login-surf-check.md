**Tags:** #automated-testing, #puppeteer, #ui-automation, #login-verification, #screenshot-capture
**Created:** 2026-01-13
**Type:** code-test

# login-surf-check

## Summary

```
Automated login verification and authenticated UI feature testing tool using Puppeteer.
```

## Details

> This script automates login verification for a web application using Puppeteer, capturing screenshots at key stages. It tests the login process with predefined credentials and validates successful navigation to authenticated pages. The tool also records screenshots of authenticated UI elements for debugging and auditing purposes.

## Key Functions

### ``constructor()``

Initializes the class with base URL, screenshot directory, and test credentials.

### ``init()``

Sets up the screenshot directory and logs initialization details.

### ``getScreenshotName(feature, description)``

Generates a timestamped filename for screenshots with sanitized descriptions.

### ``takeScreenshot(page, feature, description)``

Captures a full-page screenshot and saves it to a directory.

### ``login(page)``

Executes the login workflow, validates success, and captures screenshots at each step.

### ``testAuthenticatedFeatures(page)``

Navigates to and screenshots multiple authenticated pages (dashboard, elements, etc.).

## Usage

1. Initialize the class: `const checker = new LoginSurfCheck();`
2. Call `checker.init()` to set up screenshots.
3. Use `checker.login(page)` to test login functionality.
4. Use `checker.testAuthenticatedFeatures(page)` to verify authenticated UI navigation.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[none]]

>[!INFO] Important Note
> This script assumes the target application is running on `https://localhost:8443`. Adjust `baseUrl` if needed.

>[!WARNING] Caution
> Always validate credentials securely in production. Hardcoded test credentials (`test/testpass`) are used here for testing only.
