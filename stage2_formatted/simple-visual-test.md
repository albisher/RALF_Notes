**Tags:** #visual-testing, #puppeteer, #web-automation, #api-testing, #responsive-design
**Created:** 2026-01-13
**Type:** code-notes

# simple-visual-test

## Summary

```
Automated visual and functional testing framework for web applications using Puppeteer.
```

## Details

> This script implements a `SimpleVisualTest` class that automates visual and functional testing of a web application running on `localhost:8443`. It uses Puppeteer to launch a browser, navigate to specified URLs, and capture screenshots for verification. The class includes methods to test health checks, login pages, public routes, error handling, and responsive design across different viewports. It logs test results with timestamps and success/failure indicators.

## Key Functions

### ``init()``

Initializes browser, directory, and sets up Puppeteer configuration.

### ``takeScreenshot(name, description)``

Captures a full-page screenshot with a timestamped filename.

### ``logResult(testName, success, details)``

Records test outcomes in an array and logs them to console.

### ``testHealthCheck()``

Verifies API health endpoint response by checking for "healthy" status.

### ``testLoginPage()``

Checks if login form elements (form, username, password, submit) exist on the login page.

### ``testPublicPages()``

Tests multiple public routes (login, debug, webauthn) for proper loading and content presence.

### ``testErrorHandling()``

Tests 404 error page display by navigating to a non-existent route.

### ``testResponsiveDesign()``

(Incomplete) Tests rendering across different viewports (desktop, tablet).

## Usage

1. Instantiate `SimpleVisualTest` class.
2. Call `init()` to launch browser and prepare environment.
3. Execute test methods sequentially (e.g., `await testClass.testHealthCheck()`).
4. Review `testResults` array for outcomes or console logs for real-time feedback.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[Visual Testing Framework Documentation]]
- [[Puppeteer API Reference]]

>[!INFO] Important Note
> Missing `testResponsiveDesign()` implementation for viewports (e.g., mobile). Add viewport switching logic using `this.page.setViewport()` before testing.

>[!WARNING] Caution
> Disable `--disable-web-security` in production for security compliance. Use HTTPS in production environments.
