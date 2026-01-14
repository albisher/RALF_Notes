**Tags:** #task-management, #subtask-conversion, #workflow-automation, #dependency-tracking, #bash-scripting
**Created:** 2026-01-13
**Type:** code-notes

# convert-task-to-subtask

## Summary

```
Script to convert standalone tasks into subtasks with validation and dependency updates.
```

## Details

> This script automates converting an existing standalone task into a subtask of another task within a task management system. It parses task IDs, validates parent-child relationships, and updates references while preserving task history and dependencies. The process includes checks for circular dependencies, priority alignment, and status compatibility before performing the conversion.

## Key Functions

### ``task-master add-subtask``

Core function to add a subtask with specified parent-child relationship.

### `Argument parsing`

Handles multiple syntax variations (e.g., "move task 8 under 5", "5 8").

### `Pre-conversion validation`

Ensures tasks exist, no circular dependencies, and subtask status compatibility.

### `Dependency updates`

Automatically adjusts references (e.g., renaming task ID to `5.1`).

### `Hierarchy maintenance`

Inherits parent context (e.g., priority, status) and updates time estimates.

## Usage

1. Run the script with arguments like:
   ```bash
   /project:tm/add-subtask/from-task 5 8
   ```
   (or equivalent variations: `move task 8 under 5`, `make 8 a subtask of 5`).
2. The script validates inputs, updates task hierarchy, and logs changes.
3. Verify results via updated task hierarchy and dependency lists.

## Dependencies

> ``task-master` (task management CLI tool)`
> `Bash scripting environment.`

## Related

- [[`task-master documentation`]]
- [[`task-management workflows`]]
- [[`dependency-resolution`]]

>[!INFO] Important Note
> **Task ID Renaming**: The converted task’s ID is updated to `<parent-id>.<new-suffix>` (e.g., `5.1`) to reflect hierarchy. Ensure no conflicting IDs exist before running.
>

>[!WARNING] Caution
> **Circular Dependencies**: If the parent task depends on the converted task (or vice versa), the script will abort. Manually resolve conflicts before execution.
