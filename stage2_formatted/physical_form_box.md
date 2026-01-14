**Tags:** #generation, #physical_design, #entity_creation, #box_pattern, #hash_based
**Created:** 2026-01-13
**Type:** code-notes

# physical_form_box

## Summary

```
Generates physical descriptions for entities (plants, robots, buildings) via hash-based generation system.
```

## Details

> This `PhysicalFormBox` class acts as a middleware layer between user input and specialized generators. It validates required inputs (hash and entity type), routes requests through a `GeneratorBridgeBox` to delegate actual generation logic, and packages results into a standardized output. The system supports customizable constraints (e.g., biome for plants) and falls back to the entity type if no specific generator is provided.

## Key Functions

### ``__init__()``

Initializes dependencies (`HashGeneratorMasterBox`, `GeneratorBridgeBox`, `GeneratorRegistryBox`) and sets up box metadata.

### ``execute(input_data)``

Orchestrates the generation workflow:

## Usage

1. Pass a `BoxInput` with:
   - `input_hash`: Unique identifier for generation.
   - `entity_type`: Target category (e.g., "plant").
   - Optional: `generator_type` or `constraints`.
2. Output includes:
   - `physical_form`: Generated attributes (e.g., size, texture).
   - Metadata (hash, entity_type, generator used).

## Dependencies

> ``..core.box_interface``
> ``..generators.hash_generator_master_box``
> ``..generators.generator_bridge``
> ``..generators.generator_registry_box``

## Related

- [[`GeneratorBridgeBox`]]
- [[BoxOutput`]]
- [[`HashGeneratorMasterBox`]]

>[!INFO] Input Validation
> Always checks for required fields (`input_hash`, `entity_type`) before delegation. Missing values trigger immediate failure.

>[!WARNING] Error Handling
> Logs exceptions and returns generic failure messages to avoid exposing internal generator details. Critical paths (e.g., bridge failure) propagate errors upward.
