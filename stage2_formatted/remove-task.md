**Tags:** #task-management, #deletion, #dependency-handling, #confirmation, #impact-assessment
**Created:** 2026-01-13
**Type:** code-notes

# remove-task

## Summary

```
A script to permanently remove tasks from a project while preserving project integrity through dependency checks and user confirmation.
```

## Details

> This script removes a task by its ID while analyzing its current status, dependencies, and subtasks. It ensures proper cleanup of relationships, warns about potential cascading effects, and provides alternatives like marking tasks as cancelled or archiving data. The process includes a confirmation step and logs the removal for auditing.

## Key Functions

### ``remove-task``

Core function to delete a task with ID validation and impact analysis.

### ``pre-removal-analysis``

Evaluates task status, dependencies, and subtasks before deletion.

### ``confirmation-handling``

Requires user input unless `-y` flag is used for auto-confirmation.

### ``dependency-updates``

Adjusts references for dependent tasks and subtasks post-deletion.

### ``impact-assessment``

Displays a visual impact report before deletion.

### ``alternative-actions``

Suggests non-deletion alternatives (e.g., marking as cancelled).

## Usage

```bash
task-master remove-task --id=<task_id> [-y]
```
- Replace `<task_id>` with the task number (e.g., `5`).
- Use `-y` to auto-confirm deletion (skips interactive prompts).

## Dependencies

> ``bash``
> ``task-master` CLI tool (internal dependency)`
> `optional `-y` flag for auto-confirmation.`

## Related

- [[task-master-cli]]
- [[dependency-management]]
- [[audit-logging]]

>[!INFO] **Critical Path Warning**
> If the task is part of the critical path, deletion may disrupt project timelines. Review dependent tasks carefully before proceeding.

>[!WARNING] **Data Loss Risk**
> Completed work and subtasks are permanently removed. Use `-y` only if absolutely necessary; consider archiving first.
