**Tags:** #complexity-analysis, #task-breakdown, #AI-driven-development, #project-management, #risk-assessment
**Created:** 2026-01-13
**Type:** documentation

# analyze-complexity

## Summary

```
Analyzes task complexity using AI to recommend expansion strategies for high-risk projects.
```

## Details

> This tool evaluates pending tasks across a project by assessing technical, time-based, and dependency-related factors. It employs AI to score tasks on a 1-10 scale, categorizing them into high, medium, or low complexity. Based on the analysis, it generates structured recommendations for breaking down complex tasks into subtasks, mitigating risks, and optimizing resource allocation. The output includes detailed risk factors and expansion strategies tailored to team expertise and project constraints.

## Key Functions

### ``analyze-complexity``

Executes AI-driven complexity analysis of pending tasks.

### ``--research` flag`

Enables deeper research-based analysis for critical tasks.

### ``--threshold=5``

Filters tasks above a specified complexity score for prioritization.

### ``expand` command integration`

Uses results to break down recommended tasks.

### `Report generation`

Saves findings to a structured markdown file for review.

## Usage

Run via CLI:
```bash
task-master analyze-complexity [--research] [--threshold=5]
```
- Default: Analyzes all pending tasks.
- `--research`: Enhances analysis with research AI for deeper insights.
- `--threshold=5`: Flags tasks scoring above 5 for review.

## Dependencies

> `AI-driven task analysis libraries (e.g.`
> `custom ML models for complexity scoring)`
> `task management framework (e.g.`
> `TaskMaster CLI)`
> `and markdown processing tools.`

## Related

- [[TaskMaster CLI Documentation]]
- [[Project Complexity Guidelines]]
- [[Risk Mitigation Framework]]

>[!INFO] Output Location
> Results are saved to `.taskmaster/reports/complexity-analysis.md` for easy access during sprint planning.

>[!WARNING] Threshold Sensitivity
> Adjusting `--threshold` too low may generate excessive expansion recommendations; test with conservative values first.
