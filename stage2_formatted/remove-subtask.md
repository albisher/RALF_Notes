**Tags:** #task-management, #subtask-handling, #workflow-automation, #bash-scripting, #data-conversion
**Created:** 2026-01-13
**Type:** code-notes

# remove-subtask

## Summary

```
Script to remove subtasks from parent tasks, with optional conversion to standalone tasks, including validation and impact analysis.
```

## Details

> This script processes subtask removal from a parent task in a task management system. It supports parsing subtask IDs (e.g., `5.1`) and provides two modes: deletion (removing subtask data entirely) or conversion (extracting subtask data into a standalone task). The script includes pre-removal checks (e.g., verifying subtask existence, checking completion status) and smart features like warnings for in-progress subtasks and dependency updates. It handles workflow transitions, preserves task history, and updates parent task estimates.

## Key Functions

### ``remove-subtask``

Core function to delete or convert a subtask based on parsed arguments.

### ``validate-subtask``

Checks subtask existence, completion status, and dependencies before removal.

### ``analyze-impact``

Evaluates effects on parent task and dependent subtasks.

### ``convert-to-standalone``

Extracts subtask data into a new standalone task with preserved metadata.

### ``update-parent-task``

Adjusts parent task status, estimates, and hierarchy post-removal.

## Usage

1. **Delete Subtask**:
   ```bash
   task-master remove-subtask --id=<parentId.subtaskId>
   ```
   Example: `task-master remove-subtask --id=5.1`

2. **Convert Subtask to Standalone**:
   ```bash
   task-master remove-subtask --id=<parentId.subtaskId> --convert
   ```
   Example: `task-master remove-subtask --id=5.1 --convert`

3. **Manual Conversion via Alias**:
   ```bash
   task-master remove-subtask 5.1 standalone
   ```

## Dependencies

> ``task-master` CLI tool (assumed to be an internal task management framework)`
> `basic shell utilities (e.g.`
> ``grep``
> ``awk``
> ``sed`).`

## Related

- [[`task-master documentation`]]
- [[`task-management workflows`]]
- [[`subtask conversion guide`]]

>[!INFO] Pre-Removal Validation
> The script first validates the subtask’s existence, completion status, and dependencies before proceeding. If the subtask is marked as "in-progress," it issues a warning to avoid unintended data loss.
>

>[!WARNING] Data Loss Risk
> Deleting a subtask permanently removes its data unless converted to standalone. Always confirm the action (`y/n`) to prevent accidental deletions. Impact on parent task estimates and dependent subtasks may require manual review.
