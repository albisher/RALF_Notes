**Tags:** #Node.js, #Automated Testing, #Command-Line Interface, #Modular Check Execution, #Health Checks, #UI Validation, #API Testing
**Created:** 2026-01-13
**Type:** code-notes

# index

## Summary

```
A modular Node.js CLI tool for executing automated system checks (health, UI, API) with a flexible command-line interface.
```

## Details

> This script acts as a CLI entry point for a modular automated check system, delegating execution to specialized modules (`run-all-checks`, `health-check`, `ui-check`, `api-check`). It parses command-line arguments to determine which checks to run (`health`, `ui`, `api`, or `all`), using `chalk` for colored console output. The `main()` function orchestrates execution, wrapping calls in error handling. Help documentation is displayed if `--help` or `-h` is provided.

## Key Functions

### ``main()``

Orchestrates check execution based on command-line input.

### ``runAllChecks()``

Executes all predefined check modules sequentially.

### ``runHealthChecks()``

Runs system health validation routines.

### ``runUIChecks()``

Validates UI components and responsiveness.

### ``runAPIChecks()``

Tests API endpoints and functionality.

### ``chalk``

Provides colored terminal output for user feedback.

## Usage

1. Run with default (`all`) checks:
   ```bash
   node index.js
   ```
2. Specify a single check type:
   ```bash
   node index.js health
   node index.js ui
   node index.js api
   ```
3. Show help:
   ```bash
   node index.js --help
   ```

## Dependencies

> ``./run-all-checks``
> ``./health-check``
> ``./ui-check``
> ``./api-check``
> ``chalk``

## Related

- [[Space Pearl World Builder Documentation]]
- [[Modular Check System Architecture]]

>[!INFO] Command Default
> If no command is provided, `all` is assumed, executing every check module.

>[!WARNING] Error Handling
> Uncaught errors halt execution, printing the error message in red and exiting with code `1`.
