**Tags:** #automated-testing, #frontend-verification, #puppeteer, #modular-components, #ui-testing
**Created:** 2026-01-13
**Type:** code-test

# modular-verification-test

## Summary

```
Automated modular UI component verification using Puppeteer to test a local web application's structure, content, and navigation.
```

## Details

> This script uses Puppeteer to launch a browser, interact with a local web application (running on `localhost:8443`), and perform modular verification tests. It checks for the existence of UI elements (e.g., sidebar, page content), content loading, navigation groups, icons, and functional navigation. Screenshots are saved to a directory for debugging. The test logs console messages, errors, and results in real-time.
> 
> The script includes error handling for screenshot failures and page navigation issues. It also logs console messages and page errors for debugging purposes.

## Key Functions

### ``init()``

Creates the directory for screenshots if it doesn’t exist.

### ``takeScreenshot(page, filename)``

Captures a full-page screenshot and saves it to a specified directory.

### ``testModularComponents()``

Orchestrates the entire test suite, including:

## Usage

1. Install dependencies: `npm install puppeteer`.
2. Run the script: `node modular-verification-test.js`.
3. Configure `baseUrl` and `screenshotDir` in the constructor if needed.
4. Extend `testModularComponents()` with additional test cases as required.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses Puppeteer’s `headless: 'new'` mode, which may behave differently than the default `headless: true`. Ensure the target application is running locally on `localhost:8443` before execution.

>[!WARNING] Caution
> If the application fails to load or crashes, the test will terminate early. Always check console logs for errors during execution. Avoid running in a sandboxed environment (e.g., Docker) unless necessary, as Puppeteer’s `--no-sandbox` flag may not work reliably in restricted contexts.
