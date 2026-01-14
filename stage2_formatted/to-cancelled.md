**Tags:** #task-management, #workflow, #process-automation, #status-updates, #dependency-management
**Created:** 2026-01-13
**Type:** documentation

# to-cancelled

## Summary

```
Explains the process and command for permanently cancelling a task in a structured workflow system.
```

## Details

> This document outlines the procedure for cancelling a task permanently, detailing reasons, pre-checks, execution, and post-cancellation impacts. It emphasizes ensuring no critical dependencies remain, verifying rationale, and documenting lessons learned before applying the `task-master` command to set the task status to `cancelled`. The process includes dependency updates, cleanup actions, and historical preservation to maintain transparency and learning.

## Key Functions

### ``task-master set-status``

Executes the command to update a task’s status to `cancelled`.

### `Pre-Cancellation Checks`

Validates dependencies, partial implementations, and rationale before cancellation.

### `Cancellation Impact Analysis`

Manages dependency notifications, scope updates, and cleanup tasks post-cancellation.

## Usage

1. **Identify Task**: Locate the task ID to cancel.
2. **Pre-Checks**: Confirm no critical dependencies, verify partial work, and document rationale.
3. **Execute**: Run `task-master set-status --id=<TASK_ID> --status=cancelled`.
4. **Post-Process**: Notify dependencies, archive work, update documentation, and preserve historical context.

## Dependencies

> ``task-master` CLI tool (command-line interface for task management).`

## Related

- [[Task Management Workflow]]
- [[Dependency Resolution Guide]]

>[!INFO] Important Note
> Ensure all pre-cancellation checks are completed before executing the command to avoid unintended consequences.

>[!WARNING] Caution
> Avoid cancelling tasks with active dependencies or partial implementations without updating affected teams.
