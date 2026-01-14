**Tags:** #script, #automation, #nodejs, #world-building, #session-management
**Created:** 2026-01-13
**Type:** code-script

# run-space-peral-sessions

## Summary

```
Automates execution of multiple JavaScript session files for a fictional "Space Peral" world creation project.
```

## Details

> This script orchestrates running five predefined JavaScript files (world creation, robots, plants/animals, buildings, and story) in sequence. It uses Node.js's `child_process.execSync` to execute each file, tracks execution time, logs progress, and records results. After completion, it generates a structured JSON summary file detailing success/failure statuses and durations of each session.

## Key Functions

### `runSpacePeralSessions()`

Orchestrates execution of all session files with progress logging and timing.

### `File existence check`

Verifies all required session files exist before execution.

### `Summary generation`

Creates a detailed JSON report of execution results.

## Usage

1. Place all session files (e.g., `space-peral-session-1-world.js`) in the same directory as this script.
2. Run the script with `node run-space-peral-sessions.js`.
3. Review the console output and generated `space-peral-sessions-summary.json`.

## Dependencies

> ``child_process``
> ``fs``
> ``path` (Node.js core modules)`

## Related

- [[World Creation Documentation]]
- [[Space Peral Project Overview]]

>[!INFO] Important Note
> This script assumes all session files are JavaScript modules in the same directory. Missing files will cause the script to exit with an error.

>[!WARNING] Caution
> Running in parallel could cause race conditions. The script intentionally waits 5 seconds between sessions to prevent concurrent execution.
