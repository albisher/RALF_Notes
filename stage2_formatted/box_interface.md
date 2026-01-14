**Tags:** #Abstract-Class, #Input-Output-Contract, #Dependency-Management, #Type-Hinting, #Dataclass
**Created:** 2026-01-13
**Type:** documentation

# box_interface

## Summary

```
Defines a standardized box interface for modular workflow processing with input/output validation and dependency tracking.
```

## Details

> The `Box` interface uses Python’s ABC (Abstract Base Class) to enforce a contract for all concrete box implementations. It defines `BoxInput` and `BoxOutput` dataclasses for consistent data handling, while `execute()` is the core abstract method requiring subclasses to implement. The `validate_input()` method provides default validation logic, though subclasses can override it. Dependencies between boxes are tracked via `dependencies` list.

## Key Functions

### ``BoxInput``

Standardized input structure (dict + optional context).

### ``BoxOutput``

Standardized output structure (bool success, dict data, optional error/metadata).

### ``execute(input_data`

BoxInput) -> BoxOutput`**: Abstract method—must be implemented by subclasses.

### ``validate_input(input_data`

BoxInput) -> tuple[bool, Optional[str]]`**: Default input validation.

### ``get_dependencies()``

Returns a list of box names this box depends on.

## Usage

1. Subclass `Box` and implement `execute()`.
2. Define `dependencies` for required boxes.
3. Use `BoxInput`/`BoxOutput` for structured data exchange.
4. Override `validate_input()` for custom rules.

## Dependencies

> ``abc``
> ``typing``
> ``dataclasses``

## Related

- [[None]]

>[!INFO] Input Validation
>Subclasses must override `validate_input()` if custom rules are needed (e.g., schema validation). The default checks only for `BoxInput` type and dict data.

>[!WARNING] Dependency Management
>Missing dependencies in `self.dependencies` may cause runtime errors. Always declare required boxes explicitly.
