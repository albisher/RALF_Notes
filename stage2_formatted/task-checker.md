**Tags:** #quality-assurance, #task-verification, #code-review, #automated-checking, #requirement-validation
**Created:** 2026-01-13
**Type:** code-agent-description

# task-checker

## Summary

```
Agent designed to perform rigorous verification of task implementations marked for review, ensuring compliance with specifications, code quality, and test coverage before approval.
```

## Details

> The `task-checker` agent is a specialized quality assurance tool that systematically evaluates tasks marked as 'review' by:
> 1. Retrieving task specifications and test requirements via the `mcp__task-master-ai__get_task` tool
> 2. Examining implementation files using `Read` and pattern matching with `Grep`
> 3. Executing build and test commands via `Bash` to validate functionality
> 4. Assessing code quality against project conventions (TypeScript typing, error handling, documentation)
> 5. Validating all dependencies and integration points
> 
> It operates as a gatekeeper between implementation and completion, generating structured verification reports that classify tasks as PASS, PARTIAL, or FAIL based on predefined decision criteria.

## Key Functions

### `Task Specification Review`

Extracts and analyzes requirements from task metadata

### `Implementation Verification`

Validates file existence, content, and structure against specifications

### `Test Execution`

Runs automated tests and verifies build success

### `Code Quality Assessment`

Evaluates adherence to project standards (typing, error handling, documentation)

### `Dependency Validation`

Checks integration with related tasks and system stability

### `Report Generation`

Produces YAML-formatted verification reports with detailed findings

## Usage

1. Trigger when a task is marked 'review' by the task-executor
2. Agent retrieves task details and executes verification workflow
3. Generates structured report with:
   - Task status (PASS/PARTIAL/FAIL)
   - Met requirements checklist
   - Found issues/warnings
   - Test results
   - Recommendations
4. Output determines whether task proceeds to 'done' or returns to 'pending'

## Dependencies

> ``mcp__task-master-ai__get_task``
> ``Read` tool`
> ``Bash` tool`
> ``Grep` tool`

## Related

- [[Task Implementation Guide]]
- [[Quality Assurance Standards]]
- [[Task Review Workflow]]

>[!INFO] Critical Role
>This agent acts as the sole quality gate between implementation and completion, preventing incomplete or low-quality work from being marked as done.

>[!WARNING] Strict Non-Interference
>Never modify code or implement fixes - only verify existing implementations against requirements. All corrections must be handled by the task-executor.
