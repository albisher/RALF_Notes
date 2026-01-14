**Tags:** #task-management, #hierarchical-view, #subtask-display, #project-overview, #bash-scripting
**Created:** 2026-01-13
**Type:** code-notes

# list-tasks-with-subtasks

## Summary

```
A hierarchical task listing tool that visualizes parent tasks with nested subtasks for project management.
```

## Details

> The script implements a command-line interface (`task-master list --with-subtasks`) to recursively display tasks and their subtasks in a structured, indented format. It enhances visibility by incorporating status badges, progress indicators, and dependency markers. The output dynamically calculates completion percentages for parent tasks and highlights problematic subtask chains (e.g., blocked dependencies). The design prioritizes readability through indentation and color-coded status indicators, making it easier to assess project progress and critical paths.

## Key Functions

### ``task-master list --with-subtasks``

Core command to render the hierarchical task tree.

### `Completion percentage calculation`

Computes parent task completion based on subtask statuses.

### `Blocked subtask detection`

Flags subtasks with unresolved dependencies or blockers.

### `Indentation logic`

Applies visual hierarchy via spaces or tabs for nested subtasks.

### `Status badge rendering`

Displays icons (e.g., ✅/❌) for task completion status.

### `Dependency/blocker highlighting`

Uses color or symbols to mark critical issues.

## Usage

1. **Installation**: Ensure `task-master` CLI is installed (assumes a local task database).
2. **Execution**:
   ```bash
   task-master list --with-subtasks
   ```
3. **Customization**:
   - Adjust indentation depth via config (e.g., `--indent=2`).
   - Filter by status: `--status=open` or `--status=blocked`.
   - Group tasks by category: `--group=functional_area`.

## Dependencies

> ``bash``
> ``jq` (for JSON parsing)`
> `custom task database (likely structured as JSON/YAML)`
> `optional: `colorterm` or ANSI escape codes for colored output.`

## Related

- [[Task Master CLI Documentation]]
- [[Project Hierarchy Cheat Sheet]]
- [[Subtask Dependency Rules]]

>[!INFO] Indentation Note
> Indentation is dynamically set based on subtask nesting depth (default: 2 spaces per level). Override with `--indent` flag (e.g., `--indent=4`).

>[!WARNING] Blocked Subtasks
> Subtasks marked as blocked (e.g., `blocked: true`) will appear with a red status badge. Resolve dependencies immediately to avoid cascading delays.
