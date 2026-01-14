**Tags:** #status-management, #task-tracking, #review-process, #workflow-automation
**Created:** 2026-01-13
**Type:** tutorial

# to-review

## Summary

```
A script to automate setting a task’s status to "review," marking work as complete but requiring verification before finalization.
```

## Details

> This script configures a task’s status to "review," indicating the work is finished but awaiting peer review, testing, or approval. It is used when code, documentation, or design is complete but requires validation before finalization. The workflow includes generating a checklist, documenting review notes, and optionally automating reminders or expert-based reviewer assignments.

## Key Functions

### ``task-master set-status``

Sets task status to "review" with provided task ID.

### `Review Checklist Generation`

Links to PR/MR, highlights key changes, and notes areas needing attention.

### `Documentation Updates`

Adds review notes, links artifacts, and specifies reviewers.

### `Smart Actions`

Tracks review duration, creates reminders, and suggests reviewers based on expertise.

## Usage

1. Run the command:
   ```bash
   task-master set-status --id=<TASK_ID> --status=review
   ```
2. Follow the checklist steps (generate, document, and automate reminders).
3. Ensure reviewers are assigned and review duration is tracked.

## Dependencies

> ``task-master` CLI tool (assumed to be a custom or third-party tool for task management).`

## Related

- [[Task Management Workflow]]
- [[Peer Review Best Practices]]

>[!INFO] Important Note
> Ensure the task ID is valid and the `task-master` CLI is properly configured before executing the command.
>

>[!WARNING] Caution
> If the task involves sensitive data, validate review artifacts thoroughly to avoid unintended exposure.
