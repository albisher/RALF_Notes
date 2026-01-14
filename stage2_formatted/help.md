**Tags:** #help-system, #task-management, #command-reference, #natural-language-processing
**Created:** 2026-01-13
**Type:** documentation

# help

## Summary

```
Provides a structured guide to Task Master CLI commands for task organization and workflow automation.
```

## Details

> This document outlines the help system for **Task Master**, a command-line tool for managing project tasks. It categorizes commands into logical groups (e.g., setup, task generation, status management) and provides natural language examples for quick usage. The help system supports tab completion for quick navigation and includes subcommands for granular control (e.g., parsing requirements, updating tasks, or managing workflows). It also emphasizes natural language filtering (e.g., listing pending tasks with filters like "high priority").

## Key Functions

### ``/project`

tm/help`**: Displays general help or command-specific details.

### ``/project`

tm/setup/install`**: Guides installation methods (comprehensive or quick).

### ``/project`

tm/init`**: Initializes a new project with AI configuration.

### ``/project`

tm/parse-prd`**: Extracts tasks from Product Requirements Documents (PRD).

### ``/project`

tm/list`**: Lists tasks with natural language filters (e.g., `pending high priority`).

### ``/project`

tm/set-status`**: Manages task statuses (e.g., `to-done`, `to-cancelled`).

### ``/project`

tm/expand`**: Breaks down complex tasks into sub-tasks.

### ``/project`

tm/workflows/smart-flow`**: Automates task execution via intelligent workflows.

### ``/project`

tm/learn`**: Provides interactive tutorials for users.

## Usage

1. **Basic Help**: Run `/project:tm/help` to see all commands.
2. **Command-Specific Help**: Use `/project:tm/help <command>` (e.g., `/project:tm/help list`).
3. **Natural Language Queries**: Filter tasks dynamically (e.g., `/project:tm/list pending high priority`).
4. **Workflow Automation**: Chain commands (e.g., `/project:tm/workflows/pipeline`).

## Dependencies

> `None (standalone documentation; assumes Task Master CLI is installed separately).`

## Related

- [[Task Master CLI Documentation]]
- [[Task Master Installation Guide]]

>[!INFO] Quick Start
> Start by installing Task Master with `/project:tm/setup/quick-install` and initialize your project with `/project:tm/init/quick`.

>[!WARNING] Command Chaining
> Ensure commands are compatible for workflows (e.g., `expand` must precede `show` for detailed views).
