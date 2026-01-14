**Tags:** #task-management, #workflow-automation, #status-updates, #project-tracking
**Created:** 2026-01-13
**Type:** code-notes

# to-done

## Summary

```
Marks a task as completed with validation and post-processing workflows for dependencies, documentation, and next steps.
```

## Details

> This script marks a task as completed by executing a validation pipeline before updating its status. It checks prerequisites (test strategy, subtasks, acceptance criteria, and code commits) before calling `task-master` to set the status to `done`. Post-completion, it triggers updates to dependencies (unblocking tasks), sprint progress, and timeline recalculation. Documentation includes generating summaries, updating `CLAUDE.md`, and logging implementation details. Finally, it highlights newly available tasks, suggests logical next steps, and tracks velocity metrics.

## Key Functions

### ``task-master set-status``

Updates task status to `done` after validation.

### `Pre-completion checks`

Validates test strategy, subtasks, acceptance criteria, and code commits.

### `Post-processing workflows`

Updates dependencies, sprint progress, and documentation (e.g., `CLAUDE.md`).

### `Next steps & celebration`

Displays unblocked tasks, suggests follow-up actions, and recognizes completion.

## Usage

Run via command-line argument:
```bash
./to-done.sh <task_id>
```
- **Input**: Task ID (passed as `$ARGUMENTS`).
- **Output**: Automated status update, dependency recalculation, and documentation updates.

## Dependencies

> ``task-master` CLI tool`
> `bash script execution environment.`

## Related

- [[`task-master` documentation]]
- [[`CLAUDE]]

>[!INFO] Important Note
> This script assumes `task-master` is installed and configured to handle `--id` and `--status=done` flags. Ensure the task ID is valid before execution.

>[!WARNING] Caution
> Skipping pre-completion checks may lead to incorrect status updates or missed dependencies. Always validate all conditions before calling `task-master`.
