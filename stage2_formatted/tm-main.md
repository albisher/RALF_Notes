**Tags:** #CLI, #TaskManagement, #AIIntegration, #WorkflowAutomation, #ProjectOrganization
**Created:** 2026-01-13
**Type:** documentation

# tm-main

## Summary

```
A structured command reference for **Task Master CLI**, integrating with Claude Code for AI-driven task management, project setup, and workflow automation.
```

## Details

> This document outlines a hierarchical CLI system for **Task Master**, designed to streamline task generation, management, and analysis. Commands are organized into categories like project setup, task generation, status updates, subtask management, and workflow automation. The system supports natural language inputs, ID-based operations, and AI-assisted features (e.g., model configuration, task expansion, and dependency validation). It leverages external AI models for intelligent recommendations and automation.

## Key Functions

### ``/project`

tm/init`**: Initialize a new project with PRD file handling.

### ``/project`

tm/parse-prd`**: Extract tasks from Product Requirements Documents (PRD).

### ``/project`

tm/generate-tasks`**: Create task files from a `tasks.json` input.

### ``/project`

tm/set-status`**: Update task status (pending, in-progress, done, etc.).

### ``/project`

tm/analyze-complexity`**: Assess task difficulty and suggest expansions.

### ``/project`

tm/next-task`**: Recommend the next task based on priority and context.

### ``/project`

tm/workflows/smart-workflow`**: Execute AI-driven workflows dynamically.

### ``/project`

tm/utils/analyze-project`**: Provide deep insights into project structure.

## Usage

1. **Initialize a project**:
   ```bash
   /project:tm/init-project
   ```
2. **Add a task with AI assistance**:
   ```bash
   /project:tm/add-task "Implement user authentication"
   ```
3. **Update task status**:
   ```bash
   /project:tm/set-status/to-done "Task ID: 123"
   ```
4. **Expand a task for deeper analysis**:
   ```bash
   /project:tm/expand 123
   ```
5. **Use natural language for filtering**:
   ```bash
   /project:tm/list show blocked tasks
   ```

## Dependencies

> `- **Claude Code API** (for AI model integration)
- **Natural Language Processing (NLP)** libraries (for parsing natural language inputs)
- **Task Management Libraries** (e.g.`
> `JSON handling for task storage)
- **Optional**: External PRD parsers (for document-based task extraction)`

## Related

- [[TaskMaster CLI Documentation]]
- [[Claude Code API Reference]]
- [[AI Workflow Automation Guide]]

>[!INFO] Natural Language Support
>Commands like `add-task` and `update-task` accept free-form text, allowing users to describe tasks concisely (e.g., `/project:tm/add-task "Fix login bug"`). The system parses arguments dynamically.


>[!WARNING] ID-Based Errors
>Commands requiring IDs (e.g., `show-task 45`) will fail silently if the ID is invalid. Always verify task IDs or use `-y` for quick confirmation prompts.
