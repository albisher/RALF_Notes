**Tags:** #task-management, #markdown-processing, #automation, #documentation, #ai-integration
**Created:** 2026-01-13
**Type:** code-notes

# generate-tasks

## Summary

```
Generates individual markdown task files from a consolidated `tasks.json` for structured documentation and AI agent use.
```

## Details

> This script processes a central `tasks.json` file to produce standalone `.txt`/markdown files (e.g., `task_001.txt`) for each task. Each file follows a standardized format with sections like **Task ID**, **Title**, **Status**, **Dependencies**, **Description**, **Test Strategy**, and **Subtasks**. The output organizes tasks in a nested `.taskmaster/tasks/` directory, enabling incremental updates and filtering by status (e.g., `pending`/`completed`). Features include AI-readability, version control compatibility, and support for custom templates.

## Key Functions

### `generate-tasks`

Orchestrates the conversion of `tasks.json` into individual task files.

### `filter-by-status`

Dynamically excludes/includes tasks based on metadata (e.g., `status: pending`).

### `incremental-update`

Skips unchanged tasks to optimize performance.

### `timestamp-tracking`

Logs generation timestamps for auditability.

### `template-support`

Allows customization via user-provided templates.

## Usage

1. Run from command line:
   ```bash
   task-master generate [--status=pending] [--output=./custom-path]
   ```
2. Example flags:
   - `--status=pending`: Only generate tasks marked as `pending`.
   - `--template=custom.md`: Override default template format.
3. Outputs files in `.taskmaster/tasks/` by default.

## Dependencies

> ``python``
> ``markdown` (e.g.`
> ``python-markdown` for formatting)`
> ``json` (built-in)`
> ``argparse` (for CLI argument parsing).`

## Related

- [[`tasks]]
- [[`task-master` CLI Guide]]

>[!INFO] **Incremental Mode**
> Skips unchanged tasks to reduce processing time; check `--dry-run` for preview.

>[!WARNING] **Status Filtering**
> Explicitly filter tasks (e.g., `--status=high`) to avoid generating all tasks.
