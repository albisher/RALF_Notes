**Tags:** #cli-tools, #task-management, #ai-assisted-workflow, #natural-language-interface, #project-organization
**Created:** 2026-01-13
**Type:** tutorial

# TM_COMMANDS_GUIDE

## Summary

```
A comprehensive guide to using Task Master’s slash commands via Claude Code for project management with natural language support.
```

## Details

> This guide provides a structured overview of Task Master’s slash commands, enabling users to manage tasks through `/project:tm/` with natural language capabilities. The system organizes commands hierarchically (e.g., `/project:tm/[command]/[subcommand]`) and supports adaptive workflows based on project state. Key features include AI-driven task analysis, dependency management, and visual status tracking.

## Key Functions

### ``/project`

tm/setup/quick-install`**: One-line installation of Task Master.

### ``/project`

tm/init/quick`**: Quick project initialization with auto-confirmation.

### ``/project`

tm/parse-prd`**: AI-driven task extraction from Product Requirements Documents.

### ``/project`

tm/next`**: AI-recommended next task selection.

### ``/project`

tm/set-status/[status]`**: Batch status updates (e.g., pending/in-progress).

### ``/project`

tm/workflows/smart-flow`**: Dynamic workflow automation (e.g., morning routine).

### ``/project`

tm/learn`**: Interactive help mode for command discovery.

## Usage

1. **Installation**: Run `/project:tm/setup/quick-install` or `/project:tm/setup/install`.
2. **Initialization**: Use `/project:tm/init` or `/project:tm/init/quick` to set up a project.
3. **Task Management**: Parse requirements (`/project:tm/parse-prd`), list tasks (`/project:tm/list`), or update statuses (`/project:tm/set-status/to-done <id>`).
4. **Workflow Automation**: Chain commands (e.g., `/project:tm/workflows/pipeline init → expand/all`).

## Dependencies

> `None (integrates with Claude Code’s built-in AI and slash command infrastructure).`

## Related

- [[`TM_COMMANDS_REFERENCE`]]
- [[`CLAUDE_CODE_SLASH_COMMANDS`]]

>[!INFO] Natural Language Support
> Commands like `/project:tm/list pending high priority` filter tasks dynamically without syntax errors.

>[!WARNING] Dependency Risks
> Auto-fix (`/project:tm/fix-dependencies`) may override manual changes—review changes carefully before execution.
