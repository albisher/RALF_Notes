**Tags:** #Bash Scripting, #Task Management, #Project Tracking, #Command-Line Tools
**Created:** 2026-01-13
**Type:** code-notes

# show-all-tag-reports

## Summary

```
Automates display of all task reports for available tags in a Space Pearl Project environment.
```

## Details

> This script leverages the `task-master` CLI tool to aggregate and visualize task progress across multiple tags. It extracts tag names, processes task outputs, and generates colored visualizations for task progress, subtask progress, priority breakdowns, and summary statistics. The script includes functions to display individual tag reports, a comprehensive summary of all tags, and a comparison matrix of task statuses across tags.
> 
> The script uses `task-master` commands to fetch task lists, processes raw output with regex and awk for parsing, and formats results with colored headers and progress bars. It handles error cases gracefully (e.g., missing tags/tasks) and provides visual feedback via ANSI color codes.

## Key Functions

### `get_tags`

Extracts and cleans a list of available tags from `task-master tags` output.

### `show_tag_report`

Displays detailed progress metrics for a single tag (tasks, subtasks, priorities, next task recommendations).

### `show_comprehensive_summary`

Aggregates statistics (total tags, tasks, completion rates) across all tags.

### `show_tag_comparison`

Generates a tabular comparison of task statuses (done/pending) across all tags.

## Usage

1. Save as `show-all-tag-reports` and make executable (`chmod +x`).
2. Run with `./show-all-tag-reports` in a directory where `task-master` is configured.
3. Outputs colored visualizations for all tags in the current Space Pearl Project.

## Dependencies

> `task-master (CLI tool for task management)`
> `sed`
> `awk`
> `grep`
> `bash (standard utilities).`

## Related

- [[Space Pearl Project Documentation]]
- [[task-master CLI Reference]]

>[!INFO] Color Usage
> ANSI color codes (`\033[0;31m`, etc.) are used for visual distinction of sections (e.g., headers, progress bars). Ensure terminal supports colors.

>[!WARNING] Error Handling
> Silent failures (e.g., `task-master` errors) are suppressed with `2>/dev/null`; missing tags/tasks show "No tasks found" instead of crashing.
