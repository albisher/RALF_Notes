**Tags:** #task-breakdown, #subtask-generation, #workflow-automation, #time-estimation, #process-management
**Created:** 2026-01-13
**Type:** code-notes

# expand-task

## Summary

```
A modular tool for decomposing complex tasks into actionable subtasks with structured analysis and time estimation.
```

## Details

> The `expand-task` script dynamically analyzes task complexity by identifying components, technical challenges, and logical dependencies. It generates a structured set of subtasks (3–7) with clear acceptance criteria, ensuring manageable chunks (1–4 hours each) and logical execution order. The process includes predefined templates for feature development, bug fixes, and refactoring, adjusting subtask structure based on task type.

## Key Functions

### ``expand --id=$ARGUMENTS``

Orchestrates task breakdown via CLI, triggering analysis and subtask generation.

### `Task Analysis Module`

Evaluates complexity, technical risks, and time estimates.

### `Subtask Generator`

Produces hierarchical subtasks with implementation order and acceptance criteria.

### `Smart Breakdown Engine`

Dynamically applies task-specific workflows (e.g., feature vs. bug fix).

## Usage

```bash
task-master expand --id=<TASK_ID>
```
1. Run the command with a task ID to trigger expansion.
2. Output includes subtask hierarchy, updated estimates, and suggested order.
3. Integrate subtasks into project workflows (e.g., Kanban boards).

## Dependencies

> ``bash``
> ``task-master` CLI tool (assumed to handle task metadata)`
> `optional external libraries for complexity scoring (e.g.`
> ``task-complexity` plugin).`

## Related

- [[Task Master Documentation]]
- [[Workflow Automation Guide]]
- [[Time Estimation Best Practices]]

>[!INFO] Critical Path Insight
> Subtasks are flagged for critical path items (e.g., dependencies on other tasks) to prioritize resource allocation.

>[!WARNING] Over-Breakdown Risk
> Avoid excessive subtasks (>7) to prevent cognitive overload; default to 3–5 for balance.
