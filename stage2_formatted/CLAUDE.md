**Tags:** #AI-Agent-Integration, #Task-Management-System, #CLI-Tools, #MCP-Server, #Product-Requirements-Documentation, #Workflow-Automation
**Created:** 2026-01-13
**Type:** documentation

# CLAUDE

## Summary

```
A CLI-based task management system with AI-driven workflow automation, integrating with Claude Code for enhanced productivity.
```

## Details

> This system automates task creation, expansion, and management from a Product Requirements Document (PRD), leveraging AI-assisted research and complexity analysis. It centralizes tasks in a structured JSON database and auto-generates markdown files for individual tasks. The system supports dependency tracking, status updates, and batch operations. It integrates with multiple AI APIs via MCP (Multi-Client Platform) and is designed to streamline daily development workflows by dynamically assigning tasks and providing AI-assisted implementation guidance.

## Key Functions

### ``task-master init``

Initializes the project directory with core files.

### ``task-master parse-prd``

Extracts tasks from a PRD document.

### ``task-master list``

Displays all tasks with their statuses.

### ``task-master next``

Selects the next available task for immediate work.

### ``task-master add-task``

Creates new tasks with AI-assisted prompts.

### ``task-master expand``

Breaks down tasks into subtasks using research.

### ``task-master analyze-complexity``

Evaluates task difficulty and suggests refinements.

### ``task-master models --setup``

Configures AI models interactively.

### ``initialize_project` (MCP)`

Equivalent to `task-master init` via MCP.

### ``parse_prd` (MCP)`

Equivalent to `task-master parse-prd`.

### ``get_tasks` (MCP)`

Equivalent to `task-master list`.

### ``next_task` (MCP)`

Equivalent to `task-master next`.

## Usage

1. Initialize the project with `task-master init`.
2. Parse tasks from a PRD using `task-master parse-prd`.
3. Use `task-master next` to start daily workflows.
4. Expand tasks with `task-master expand --research` for granularity.
5. Integrate with Claude Code via `.claude/settings.json` and MCP commands.

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
> ``.mcp.json` (MCP server config).`

## Related

- [[Task Master CLI Documentation]]
- [[MCP Server Guide]]
- [[AI Agent Workflow Cheat Sheet]]

>[!INFO] Project Initialization
> Ensure `.env` contains all required API keys before running `task-master init`. Missing keys will cause MCP integration to fail.

>[!WARNING] Dependency Management
> Always validate dependencies with `task-master validate-dependencies` before merging or releasing tasks. Unresolved dependencies may cause workflow disruptions.
