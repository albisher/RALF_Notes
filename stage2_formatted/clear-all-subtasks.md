**Tags:** #destructive-operation, #global-clear, #task-management, #subtask-deletion, #backup-and-recovery
**Created:** 2026-01-13
**Type:** documentation

# clear-all-subtasks

## Summary

```
A script to globally clear all subtasks from all tasks in a project with safeguards and confirmation steps.
```

## Details

> This script is designed to remove all subtasks (47 total) from 12 parent tasks across an entire project. It includes a multi-step process: analyzing the project, creating a backup, showing detailed impact warnings, requiring explicit confirmation, executing deletion, and generating a summary report. The operation is highly destructive, affecting in-progress and completed subtasks, and includes safeguards like backup logging and export options.

## Key Functions

### ``task-master clear-subtasks --all``

Executes the global subtask deletion command.

### `Backup creation`

Automatically saves subtasks to a JSON file (e.g., `.taskmaster/backup/subtasks-YYYYMMDD.json`).

### `Confirmation prompt`

Requires user input (`CLEAR ALL SUBTASKS`) before execution.

### `Impact analysis`

Displays statistics on total tasks, subtasks, and work at risk.

### `Report generation`

Provides a summary of removed subtasks, backup location, and adjustments to task estimates.

## Usage

1. Run the command in the terminal:
   ```bash
   task-master clear-subtasks --all
   ```
2. Review the pre-clear analysis for warnings and statistics.
3. Confirm with the exact phrase: `CLEAR ALL SUBTASKS`.
4. The script will execute, backup subtasks, and generate a post-clear report.

## Dependencies

> ``task-master` CLI tool (likely a custom or third-party task management utility).`

## Related

- [[Task Management Backup Guide]]
- [[Task Master CLI Documentation]]

>[!INFO] Important Note
> **Backup is mandatory**: The script automatically creates a backup file in `.taskmaster/backup/` before deletion. Ensure this location is safe and accessible.
>

>[!WARNING] Caution
> **Irreversible action**: This operation cannot be undone. Review subtask history and dependencies carefully before proceeding. Consider alternatives like exporting subtasks or clearing only pending tasks if possible.
