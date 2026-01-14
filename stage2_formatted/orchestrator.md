**Tags:** #orchestration, #dependency-management, #execution-flow, #modular-architecture
**Created:** 2026-01-13
**Type:** code-notes

# orchestrator

## Summary

```
Manages box execution with dependency resolution and error handling for modular workflows.
```

## Details

> The `BoxOrchestrator` class coordinates execution of independent "box" components, handling input validation, dependency resolution via topological sorting, and chaining operations. It maintains an execution history and validates inputs before processing. The orchestrator ensures proper dependency order by resolving dependencies before executing target boxes, while logging errors and failures for debugging.

## Key Functions

### ``__init__``

Initializes box discovery and dependency registry.

### ``execute_box``

Executes a single box with input validation and error handling.

### ``execute_chain``

Runs a sequence of boxes, passing output data as input to subsequent boxes.

### ``execute_with_dependencies``

Executes a box and its dependencies in topological order.

### ``_resolve_dependencies``

Implements topological sort to determine dependency execution order.

## Usage

1. Initialize with a base path to box directories.
2. Use `execute_box` for single-box execution.
3. Use `execute_chain` for sequential workflows.
4. Use `execute_with_dependencies` for boxes requiring prior dependencies.

## Dependencies

> ``.box_interface` (BoxInput`
> `BoxOutput)`
> ``.box_loader` (BoxLoader`
> `BoxRegistry)`
> ``typing``
> ``collections.defaultdict``
> ``logging``

## Related

- [[`box_interface]]
- [[`box_loader]]

>[!INFO] Dependency Resolution
> Topological sort ensures no circular dependencies are executed, preventing runtime errors.

>[!WARNING] Error Handling
> Failed dependencies halt execution early, returning partial results. Consider retry logic for transient failures.
