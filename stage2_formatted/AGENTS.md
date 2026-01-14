**Tags:** #AI-Agent, #Task-Management, #CLI-Tools, #Workflow-Automation, #Product-Requirements-Documentation, #Dependency-Management, #MCP-Integration, #Claude-Code
**Created:** 2026-01-13
**Type:** code-notes

# AGENTS

## Summary

```
A CLI-based Task Master AI agent framework for organizing, analyzing, and managing development tasks with AI-assisted expansion and dependency tracking.
```

## Details

> This system automates task creation, refinement, and tracking using AI models. It integrates with Product Requirements Documents (PRD) to generate structured tasks, supports complex task expansion into subtasks, and manages dependencies between tasks. The framework includes a CLI interface for daily workflows and an MCP server for Claude Code integration, enabling multi-agent collaboration across sessions. Key features include interactive AI model configuration, task status tracking, and automated complexity analysis.

## Key Functions

### ``task-master init``

Initializes the project directory with core files.

### ``task-master parse-prd``

Extracts tasks from a PRD document.

### ``task-master models --setup``

Configures AI models interactively.

### ``task-master list``

Displays all tasks with statuses.

### ``task-master next``

Selects the next available task for work.

### ``task-master add-task``

Creates new tasks with AI-assisted prompts.

### ``task-master expand --all``

Breaks tasks into subtasks recursively.

### ``task-master analyze-complexity``

Evaluates task difficulty using AI.

### ``task-master set-status``

Marks tasks as complete or revisited.

### ``initialize_project` (MCP)`

Equivalent to `task-master init` via MCP.

### ``parse_prd` (MCP)`

Equivalent to `task-master parse-prd`.

### ``get_tasks` (MCP)`

Equivalent to `task-master list`.

### ``next_task` (MCP)`

Equivalent to `task-master next`.

### ``add_task` (MCP)`

Equivalent to `task-master add-task`.

## Usage

1. Initialize the project with `task-master init`.
2. Parse PRD tasks with `task-master parse-prd`.
3. Configure AI models interactively via `task-master models --setup`.
4. Use MCP commands (e.g., `initialize_project`) in Claude Code sessions for workflow automation.
5. Daily workflow: `task-master next` → review → `task-master update-subtask` → `task-master set-status`.

## Dependencies

> ``task-master-ai``
> ``npx``
> ``anthropic``
> ``perplexity``
> ``openai``
> ``google``
> ``xai``
> ``openrouter``
> ``mistral``
> ``azure-opena``
> ``ollama``
> ``.env` (API keys)`
> ``node.js` (for MCP server).`

## Related

- [[Task Master Documentation]]
- [[Claude Code Guide]]
- [[MCP Server Configuration]]

>[!INFO] Project Initialization
> Always run `task-master init` in the project root before parsing PRD or using other commands. This creates the `.taskmaster` directory structure.

>[!WARNING] Dependency Management
> Manually validate dependencies with `task-master validate-dependencies` before merging tasks. Unresolved dependencies may cause workflow failures.

>[!INFO] MCP Integration
> Ensure `.mcp.json` is updated with correct API keys for all supported providers. Missing keys will trigger errors during MCP command execution.

>[!WARNING] PRD Parsing
> Use `--append` flag when updating existing PRD tasks to avoid overwriting existing entries. This preserves historical task data.
