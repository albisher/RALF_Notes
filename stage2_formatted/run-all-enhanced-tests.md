**Tags:** #test-automation, #ui-testing, #javascript, #nodejs, #error-handling, #reporting
**Created:** 2026-01-13
**Type:** code-notes

# run-all-enhanced-tests

## Summary

```
Runs enhanced UI tests for a Space Pearl application, logs results, and generates detailed reports.
```

## Details

> This script orchestrates the execution of multiple UI tests (e.g., `enhanced-ui-test.js` and `error-detection-test.js`) for a web application, capturing their outcomes (pass/fail) and metadata like errors, warnings, and performance metrics. It dynamically creates a `screenshots` directory, executes each test file via Node.js, and aggregates results into structured JSON and HTML reports. The script includes error handling for missing files and enforces a 5-minute timeout for test execution.

## Key Functions

### `runAllEnhancedTests()`

Orchestrates the execution of all predefined tests, logs progress, aggregates results, and generates reports.

### `runTest(testFile)`

Executes a single test script using Node’s `child_process.exec`, captures stdout/stderr, and resolves with test metadata (success/failure, errors, etc.).

### `generateHTMLReport(testResults)`

(Incomplete snippet; assumes a missing function to render results in HTML format.)

## Usage

1. Call `runAllEnhancedTests()` to execute all tests.
2. Results are saved to `comprehensive-test-results.json` and an HTML report (if `generateHTMLReport` is implemented).
3. Logs are printed to console for real-time monitoring.

## Dependencies

> ``child_process``
> ``fs``
> ``path` (Node.js core modules).`

## Related

- [[Space Pearl Application Test Suite Documentation]]
- [[Node]]

>[!INFO] Timeout Handling
> The script enforces a **5-minute timeout** (`300000ms`) for each test to prevent indefinite hangs, though this may not cover all edge cases (e.g., flaky tests).

>[!WARNING] Missing Function
> `generateHTMLReport()` is referenced but not fully implemented. Ensure this function is defined to render results in HTML format for visual inspection.
