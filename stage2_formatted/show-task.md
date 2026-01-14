**Tags:** #task-management, #context-aware, #rich-display, #time-intelligence, #dependency-tracking, #visualization, #workflow-analysis
**Created:** 2026-01-13
**Type:** documentation

# show-task

## Summary

```
Provides a structured framework for displaying task details with contextual insights, dependencies, and actionable recommendations.
```

## Details

> This module enhances task visualization by parsing arguments to dynamically render task information with rich context. It categorizes tasks based on input arguments (e.g., number, "current," "next") and enriches output with status history, time intelligence, and relationship mapping. The display includes visual indicators (e.g., priority badges, progress bars) and intelligent insights like risk assessment and bottleneck analysis. Multi-task views aggregate dependencies and suggest optimal workflows.

## Key Functions

### `Smart Task Selection`

Routes tasks based on argument inputs (e.g., "current," "blocked").

### `Contextual Information Renderer`

Extracts and formats core details (status, dependencies, time metrics).

### `Visual Enhancement Engine`

Generates formatted output with emojis, progress bars, and timestamps.

### `Intelligent Insights Generator`

Analyzes tasks for risk, bottlenecks, and recommendations.

### `Action Suggestion Provider`

Offers context-aware next steps (e.g., unblocking, completion checklists).

## Usage

1. **Input Arguments**:
   - Pass a numeric task ID (e.g., `show-task 45`) to display details.
   - Use keywords like `current`, `next`, or `blocked` (e.g., `show-task current`).
   - Combine IDs for comparative views (e.g., `show-task 45 46`).

2. **Output**:
   - Richly formatted task cards with visual cues (e.g., status emojis, progress bars).
   - Insights like risk assessment and dependency chains.
   - Actionable suggestions (e.g., unblocking steps).

## Dependencies

> ``argparse``
> ``datetime``
> ``collections` (Python standard libraries)`
> `external libraries for dependency graph visualization (e.g.`
> ``networkx` or custom parsing logic).`

## Related

- [[Task Management System Architecture]]
- [[Workflow Automation Guide]]
- [[Dependency Graph Visualization]]

>[!INFO] **Dynamic Argument Handling**
> The module prioritizes flexibility by parsing `$ARGUMENTS` to adapt to user queries (e.g., single ID vs. keywords). Argument parsing logic must handle edge cases like invalid inputs gracefully.


>[!WARNING] **Data Dependency Risk**
> If external task data (e.g., dependencies, timestamps) is not fetched fresh, insights (e.g., time metrics) may become stale. Ensure real-time data integration for critical workflows.
