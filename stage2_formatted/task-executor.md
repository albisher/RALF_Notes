**Tags:** #task-execution, #implementation-agent, #task-orchestration, #software-development, #agent-based-system
**Created:** 2026-01-13
**Type:** code-notes

# task-executor

## Summary

```
Agent framework for executing specific task implementations with structured workflows and dependency management.
```

## Details

> The `task-executor` agent is designed to handle the implementation phase of predefined tasks, acting as a specialized executor for subtasks identified by a task-orchestrator. It operates within a structured workflow that includes task analysis, dependency validation, incremental implementation, and quality assurance. The agent adheres to project coding standards and maintains clear documentation of progress via subtask updates. It integrates with a `task-master` system to track status, dependencies, and execution progress, ensuring alignment with broader development workflows.

## Key Functions

### `Task Analysis`

Retrieve and parse task details (ID, requirements, dependencies) using `task-master show <id>`.

### `Implementation Planning`

Outline file modifications, dependencies, and testing strategies before coding.

### `Progress Tracking`

Update task status (`in-progress`/`done`) and log implementation decisions via `task-master update-subtask`.

### `Dependency Validation`

Check prerequisites and resolve conflicts using `task-master validate-dependencies`.

### `Quality Assurance`

Execute task-defined tests, verify acceptance criteria, and resolve integration issues.

### `Workflow Coordination`

Integrate with `task-orchestrator` to transition from planning to execution phases.

## Usage

1. **Trigger**: Activated by `task-orchestrator` when a task (e.g., "Implement JWT validation") is identified.
2. **Execution**:
   - Retrieve task details (`task-master show <id>`).
   - Plan implementation (files, dependencies, tests).
   - Update status to `in-progress` (`task-master set-status --id=<id> --status=in-progress`).
   - Implement incrementally, preferring edits over new files.
   - Log progress via subtask updates.
3. **Completion**: Mark task as `done` only after testing and verification.

## Dependencies

> ``task-master` (CLI tool for task management)`
> ``sonnet` (model used for agent logic)`
> `project-specific standards (e.g.`
> ``CLAUDE.md`).`

## Related

- [[task-orchestrator]]
- [[task-master]]
- [[CLAUDE]]

>[!INFO] **Core Focus**
> This agent **only executes** tasks—it does not plan, prioritize, or resolve ambiguities. Always clarify requirements before implementation if unsure.

>[!WARNING] **Dependency Blockers**
> If a task depends on incomplete prerequisites, **pause implementation** and flag blockers via `task-master update-subtask`. Do not proceed until dependencies are resolved.
