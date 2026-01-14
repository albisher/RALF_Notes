**Tags:** #task-management, #interactive-learning, #workflow-automation, #project-initiation, #command-discovery
**Created:** 2026-01-13
**Type:** tutorial

# learn

## Summary

```
Explains Task Master’s interactive learning system for discovering project workflows, task management, and automation commands.
```

## Details

> This file outlines an interactive learning interface for Task Master, designed to guide users through its capabilities based on input arguments. It categorizes learning paths into **project initialization**, **task management**, **automation**, **analysis**, and **troubleshooting**, with tailored suggestions for beginners, intermediates, and advanced users. The system dynamically recommends commands like task creation (`/project:task-master:init`), status checks (`/project:task-master:status`), and automation pipelines (`/project:workflows:pipeline init`). It also supports command chaining, filtering, and scenario-specific workflows (e.g., breaking down tasks or planning sprints).

## Key Functions

### ``/project`

task-master:init <prd-file>`**: Creates tasks from project requirements.

### ``/project`

task-master:next`**: Identifies the next task to prioritize.

### ``/project`

workflows:auto-implement`**: Automates workflow execution.

### ``/project`

task-master:expand <id>`**: Decomposes complex tasks into subtasks.

### ``/project`

task-master:status`**: Displays current project state.

### ``/project`

task-master:list <filters>`**: Filters tasks by status/priority (e.g., `pending high`).

## Usage

1. Input a keyword (e.g., `start`, `manage`) to trigger category-specific suggestions.
2. Follow prompts to explore commands (e.g., `/project:task-master:init demo-prd.md`).
3. Use advanced patterns like command chaining or filters (e.g., `/project:task-master:list blocked`).

## Dependencies

> `None (standalone interactive guidance system).`

## Related

- [[Task Master CLI Documentation]]
- [[Project Workflow Cheat Sheet]]

>[!INFO] Dynamic Guidance
> The system adapts to user state (e.g., "No tasks yet?" → suggests initialization).

>[!WARNING] Command Complexity
> Advanced commands (e.g., `pipeline`) require understanding workflow chaining. Start with simpler commands first.
