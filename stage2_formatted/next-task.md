**Tags:** #context-aware, #task-management, #decision-making, #time-management, #workflow-automation
**Created:** 2026-01-13
**Type:** research

# next-task

## Summary

```
A dynamic task prioritization system that intelligently selects next actions based on contextual data like task states, time, dependencies, and user patterns.
```

## Details

> This system dynamically evaluates task states (active/in-progress/blocked) and recent activity to determine the optimal next action. It integrates time constraints, dependencies, and user-specific working patterns to minimize decision friction. The logic prioritizes immediate needs (e.g., blocked tasks) while offering alternatives for efficiency (e.g., quick tasks or strategic expansions). It also leverages special arguments (e.g., "quick," "easy") to refine recommendations, ensuring adaptability to user preferences.

## Key Functions

### `Context Gathering`

Analyzes active/in-progress tasks, recent activity, and time since last work.

### `Smart Decision Tree`

Uses conditional logic to prioritize tasks based on state (e.g., idle tasks, blocked tasks, or high-priority tasks).

### `Special Arguments Handling`

Processes flags like "quick," "easy," or "continue" to tailor recommendations.

### `Preparation Workflow`

Automates setup (environment, tests, files) and provides historical context for selected tasks.

### `Alternative Suggestions`

Offers multiple options (primary, quick, strategic, learning) to balance efficiency and flexibility.

### `Workflow Integration`

Connects to task management, workflow automation, and complexity analysis tools.

## Usage

1. **Trigger**: Call with arguments (e.g., `next-task --quick` or `next-task --continue`).
2. **Output**: Returns a prioritized task with context, preparation steps, and alternatives.
3. **Integration**: Automatically initiates related workflows (e.g., task start, expansion, or dependency resolution).

## Dependencies

> ``/project:task-master``
> ``/project:workflows:auto-implement``
> ``/project:task-master:expand``
> ``/project:utils:complexity-report` (assumed system modules)`

## Related

- [[None]]

>[!INFO] **Dynamic Prioritization**
> The system dynamically adjusts based on real-time task states, ensuring relevance without manual intervention.

>[!WARNING] **Dependency Risk**
> If tasks are deeply interdependent, the system may suggest complex resolutions—verify before implementation.
