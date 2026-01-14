**Tags:** #data-normalization, #generator-processing, #standardization, #box-pattern, #type-mapping
**Created:** 2026-01-13
**Type:** code-notes

# generator_format_box

## Summary

```
Standardizes generator outputs into a consistent structure for different entity types (characters, robots, etc.).
```

## Details

> The `GeneratorFormatBox` class normalizes raw generator outputs into a unified format by applying type-specific transformation rules. It handles nested wrapper structures (e.g., from `generator_service`) and merges metadata like constraints or generation methods into a standardized output. The system dynamically selects the appropriate formatter based on the `generator_type`, falling back to a default handler if no rule exists.

## Key Functions

### ``execute()``

Orchestrates the formatting process, validating inputs and routing to the correct transformation function.

### ``_format_character()``

Formats character-specific generator outputs (e.g., extracting attributes like name, traits, or stats).

### ``_format_robot()``

Handles robot/creature-specific fields (e.g., `body`, `abilities`, `weaknesses`).

### ``_format_plant()``

Processes plant-related data (e.g., `growth_pattern`, `habitat`).

### ``_format_building()``

Structures building outputs (e.g., `architectural_features`, `materials`).

### ``_format_creature()``

Generic wrapper for creature types (e.g., `monsters`, `dragons`) with shared fields.

### ``_format_default()``

Fallback for unsupported generator types, preserving raw output with metadata.

## Usage

1. Call `GeneratorFormatBox().execute()` with `BoxInput` containing:
   - `generator_output`: Raw generator result (dict).
   - `generator_type`: Target entity type (e.g., `"character"`).
   - Optional metadata (`hash`, `seed`, `additional_data`).
2. Retrieve `formatted_output` from `BoxOutput.data["formatted_output"]` for consistent processing.

## Dependencies

> ``..core.box_interface``
> ``Box``
> ``BoxInput``
> ``BoxOutput` (custom module imports for input/output handling).`

## Related

- [[`GeneratorBridgeBox`]]
- [[`generator_service` documentation]]

>[!INFO] Dynamic Rule Dispatch
> The system uses `transformation_rules` to map `generator_type` to a specific formatter. Override `_format_creature()` for custom creature logic.

>[!WARNING] Wrapper Handling
> If `generator_output` is a `generator_service` wrapper (e.g., `{'type': 'character', 'description': {...}}`), it extracts `description` and merges metadata like `constraints` into `additional_data`. Ensure `generator_type` is provided unless the wrapper defines one.
