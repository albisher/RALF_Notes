**Tags:** #automated-testing, #puppeteer, #login-test, #ui-automation, #screenshot-capture
**Created:** 2026-01-13
**Type:** code-notes

# fixed-login-test

## Summary

```
Automated login and UI verification test suite using Puppeteer to validate login functionality and authenticated page navigation.
```

## Details

> This script implements a `FixedLoginTest` class that automates a login flow and verifies subsequent authenticated page navigation. It uses Puppeteer to interact with a web application, captures screenshots for debugging, and logs test progress. The test employs predefined credentials (`test/testpass`) and systematically checks connection, login success, and access to multiple authenticated routes.

## Key Functions

### ``constructor()``

Initializes test configurations (base URL, credentials, screenshot directory).

### ``init()``

Sets up directory for screenshots and logs initialization details.

### ``getScreenshotName(feature, description)``

Generates timestamped filenames for screenshots.

### ``takeScreenshot(page, feature, description)``

Captures page snapshots with error handling.

### ``testBasicConnection(page)``

Validates connection to the base URL and checks page title.

### ``testLoginFlow(page)``

Executes login with credential validation and checks redirect success.

### ``testAuthenticatedPages(page)``

Navigates to a list of authenticated routes, verifying each page loads.

## Usage

1. Initialize the test with `new FixedLoginTest()`.
2. Call `init()` to prepare screenshots directory.
3. Use `testBasicConnection()` and `testLoginFlow()` to run specific tests.
4. For authenticated pages, call `testAuthenticatedPages()` to verify all routes.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses `test/testpass` credentials, which may not reflect production security policies. Always validate credentials in staging environments.

>[!WARNING] Caution
> Screenshot filenames include timestamps and counters, which could generate many files. Consider limiting test runs or adding cleanup logic to avoid cluttering directories.
