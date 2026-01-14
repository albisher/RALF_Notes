**Tags:** #automated-testing, #web-scraping, #puppeteer, #ui-testing, #content-validation
**Created:** 2026-01-13
**Type:** code-notes

# generator-content-check

## Summary

```
Automated UI content validation for a generator application using Puppeteer to simulate user interactions and capture screenshots.
```

## Details

> This script automates checks for a content generation application by simulating user workflows—login, navigation, and world creation. It uses Puppeteer to launch a browser, interact with the frontend, and capture screenshots at key stages. The `CheckHelper` class handles result logging, including success/failure statuses and screenshot metadata. The workflow includes logging user arrival at the login page, attempting to log in, navigating to an elements page, and creating a new world, with screenshots taken before/after critical actions.

## Key Functions

### `runGeneratorContentChecks`

Orchestrates the entire automated content validation workflow.

### `CheckHelper.takeScreenshot`

Captures UI screenshots and returns metadata (success status, folder, filename).

### `page.goto`

Navigates to specified URLs with configurable wait times.

### `page.$/page.evaluate`

Selects and interacts with DOM elements dynamically.

### `helper.addResult`

Logs test results (pass/fail) with descriptive messages and details.

## Usage

1. Require dependencies and initialize the script.
2. Call `runGeneratorContentChecks()` to execute the automated checks.
3. Review `helper.addResult` logs for pass/fail outcomes and screenshot paths.
4. Extend selectors or actions in `page.$`/`page.evaluate` for customization.

## Dependencies

> `puppeteer`
> `chalk`
> `config (local)`
> `utils/check-helper (local)`

## Related

- [[puppeteer-testing-guide]]
- [[ui-automation-patterns]]

>[!INFO] Important Note
> The script uses placeholder credentials (`user@spacepearl.com`, `password123`) and generic selectors. Replace these with actual values or refine selectors for accurate testing.

>[!WARNING] Caution
> Network delays or timeouts may cause failures. Adjust `config.timeouts.pageLoad` or add retries for critical steps to improve reliability.
