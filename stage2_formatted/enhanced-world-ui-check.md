**Tags:** #automated-testing, #ui-testing, #puppeteer, #web-scraping, #lore-management, #ui-checks
**Created:** 2026-01-13
**Type:** code-notes

# enhanced-world-ui-check

## Summary

```
Automated UI testing tool for a lore management system using Puppeteer to validate and capture screenshots of UI interactions with predefined world data.
```

## Details

> This script automates UI checks for a lore management application, leveraging Puppeteer to interact with web pages, validate login, and test lore setup functionality. It uses predefined world data (e.g., historical events, characters, and technologies) to simulate user interactions, captures screenshots of UI states, and logs success/failure outcomes. The tool initializes a screenshot directory, handles credential-based login, and systematically tests lore categories (e.g., history, culture) by adding and saving entries.

## Key Functions

### `constructor`

Initializes configuration (base URL, credentials, world data, and screenshot settings).

### `init`

Sets up the screenshot directory and logs initialization details.

### `getScreenshotName`

Generates timestamped filenames for screenshots with sanitized descriptions.

### `takeScreenshot`

Captures a full-page screenshot of a given page and logs its path.

### `login`

Authenticates with test credentials and verifies successful login via URL change.

### `testLoreSetupWithWorldData`

Tests lore setup by navigating to lore categories, adding entries (e.g., historical events), and saving them.

## Usage

1. Initialize the class: `const checker = new EnhancedWorldUICheck();`
2. Call `checker.init()` to set up the screenshot directory.
3. Use `checker.login(page)` to authenticate.
4. Execute `checker.testLoreSetupWithWorldData(page)` to test lore functionality with predefined data.
5. Ensure the target application (e.g., `localhost:8443`) is running and accessible.

## Dependencies

> `puppeteer`
> `fs`
> `path`

## Related

- [[World Data Documentation]]
- [[Puppeteer Test Framework Guide]]

>[!INFO] Important Note
> The script assumes the target application has form fields matching `input[type="text"], input[type="password"]` and buttons with text like "Manage History" or "Add." Customize selectors (e.g., `page.$()`) if UI elements differ.

>[!WARNING] Caution
> Use test credentials (`test/testpass`) only in controlled environments. Avoid hardcoding credentials in production. The script may fail if the target URL or UI structure deviates from expectations. Validate selectors dynamically if possible.
