**Tags:** #Agile #ProjectManagement, #Dashboard #Analytics
**Created:** 2026-01-13
**Type:** documentation

# project-status

## Summary

```
Provides an enhanced status command for project tracking with contextual insights, visual analytics, and actionable recommendations.
```

## Details

> This file outlines an **intelligent status command** designed to deliver a comprehensive project overview by analyzing user-provided arguments (e.g., `sprint`, `blocked`, `team`). It dynamically segments data into executive summaries, workflow health metrics, predictive analytics, and visualizations. The system prioritizes real-time insights—such as task progress, blockers, and velocity trends—while offering structured recommendations for immediate actions, task sequencing, and process improvements. Historical comparisons enable trend analysis, reinforcing iterative decision-making.

## Key Functions

### `Executive Summary`

Generates a high-level dashboard with key metrics (active tasks, progress %, blockers, time analysis).

### `Contextual Analysis`

Filters insights based on argument inputs (e.g., `sprint`, `blocked`, `risk`) to focus on specific concerns.

### `Smart Insights`

Identifies workflow inefficiencies (e.g., idle tasks, bottlenecks) and predictive risks (e.g., deadline misses).

### `Visual Intelligence`

Renders dynamic visuals (e.g., progress bars, velocity trends) for immediate comprehension.

### `Actionable Recommendations`

Provides structured suggestions for unblocking critical tasks, optimizing workflows, and resource allocation.

## Usage

1. **Input Arguments**: Pass keywords like `sprint`, `blocked`, or `team` to refine insights (e.g., `project-status sprint`).
2. **Output**: Returns a structured report with:
   - **Metrics**: Progress %, velocity trends, blocked tasks.
   - **Visuals**: Progress bars, priority distributions.
   - **Recommendations**: Immediate actions, process improvements.
3. **Historical Context**: Compare current data to past periods for trend analysis.

## Dependencies

> `Agile frameworks (Scrum/Kanban)`
> `data visualization libraries (e.g.`
> `Chart.js`
> `Plotly)`
> `time-tracking APIs`
> `dependency resolution tools.`

## Related

- [[Project Management Dashboards]]
- [[Agile Velocity Tracking]]
- [[Scrum Burndown Analysis]]

>[!INFO] **Dynamic Filtering**
> The command adapts its output based on `$ARGUMENTS`, ensuring relevance to the user’s query (e.g., `blocked` highlights dependency chains).

>[!WARNING] **Data Dependency**
> Requires access to task history, team workloads, and time-tracking data to generate accurate insights. Incomplete data may skew analytics.
