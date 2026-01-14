**Tags:** #prd-parsing, #task-generation, #requirements-analysis, #sprint-planning, #automation
**Created:** 2026-01-13
**Type:** code-notes

# parse-prd

## Summary

```
Tool automates extraction of structured tasks from PRD documents for sprint planning.
```

## Details

> This script processes Product Requirements Documents (PRD) to decompose high-level requirements into executable tasks. It performs multi-stage analysis: extracting core requirements, identifying technical dependencies, and generating implementation workflows. The parser defaults to creating 10-15 tasks but allows customization via command-line options for research or comprehensive modes.

## Key Functions

### `parse-prd`

Core function that reads PRD files and generates task breakdowns.

### `task-master`

CLI wrapper handling input/output and argument parsing.

### `dependency_graph`

Generates visual representation of task relationships.

### `task-expansion`

Suggests sub-tasks for complex requirements.

## Usage

```bash
task-master parse-prd --input=path/to/prd.md --num-tasks=12 --mode=comprehensive
```
- `--input`: Path to PRD document
- `--num-tasks`: Custom task count (default 10-15)
- `--mode`: Research/comprehensive (default research)

## Dependencies

> `bash`
> `python3`
> `taskmaster-library (internal dependency)`
> `dependency-graph-visualizer`

## Related

- [[TaskMaster Documentation]]
- [[PRD Template Guide]]
- [[Sprint Planning Cheat Sheet]]

>[!INFO] Input Validation
> Script validates PRD format before processing and warns if invalid YAML/Markdown detected.

>[!WARNING] Mode Conflict
> Using both `--num-tasks` and `--mode` may override default behavior - check output for warnings.
