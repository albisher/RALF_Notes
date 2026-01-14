**Tags:** #AI-Assisted-Workflow, #Context-Aware-Automation, #Smart-Productivity, #Command-Execution, #Pattern-Learning
**Created:** 2026-01-13
**Type:** code-notes

# smart-workflow

## Summary

```
A dynamic workflow executor that adapts to user command history, project state, and temporal context for optimized task management.
```

## Details

> The `smart-workflow` system dynamically selects and executes workflows based on:
> 1. **Command history** (e.g., `status`, `complete`) to infer intent.
> 2. **Project state** (e.g., pending tasks, blocked work) to prioritize actions.
> 3. **Temporal context** (time of day, day of week) to trigger time-sensitive workflows.
> 4. **User patterns** (e.g., morning routines) to personalize execution.
> 
> It composes workflows in four phases:
> - **State analysis** (e.g., parsing `list pending` for backlog data).
> - **Primary workflow execution** (e.g., triggering a standup script).
> - **Follow-up suggestions** (e.g., recommending next tasks).
> - **Environment prep** (e.g., setting up tools for coding).
> 
> The system also **learns** by tracking sequences (e.g., `status → complete`) and preferences (e.g., Friday workflows), adapting over time.

## Key Functions

### `ContextAnalyzer`

Parses recent commands/project state to determine intent.

### `WorkflowSelector`

Maps intent to predefined workflows (e.g., standup, sprint planning).

### `ExecutionEngine`

Orchestrates command chaining (e.g., `analyze → execute → suggest`).

### `LearningModule`

Tracks user patterns (time, commands) for future personalization.

## Usage

1. Trigger with `$ARGUMENTS` (e.g., no args for default behavior).
2. System auto-detects workflow based on:
   - Last command (e.g., `expand` → complexity analysis).
   - Time (e.g., Friday → weekly review).
   - Project state (e.g., pending tasks → sprint planning).
3. Outputs:
   - Executed commands.
   - Follow-up suggestions.
   - Adapted environment setup.

## Dependencies

> ``command-history``
> ``project-state-api``
> ``time-context``
> ``user-patterns` (internal modules)
*(External: None`
> `but may integrate with CLI parsers or task managers.)*`

## Related

- [[Smart-Workflow-Documentation]]
- [[User-Pattern-Tracking]]
- [[Workflow-Template-Repository]]

>[!INFO] Dynamic Adaptation
> The system **learns** from your workflows (e.g., if you always use `status` → `commit` on Fridays, it will auto-chain them).
>

>[!WARNING] Context Dependency
> If no commands are run, it defaults to **time-based** workflows (e.g., morning standup). Avoid empty inputs to prevent ambiguity.
