**Tags:** #procedural_generation, #world_context, #box_interface, #generation_service, #python_generators
**Created:** 2026-01-13
**Type:** documentation

# map_generator_box

## Summary

```
Generates procedural maps using context-aware logic from world data and Python generators.
```

## Details

> The `MapGeneratorBox` class is a procedural map generator that integrates a Python generator to produce map parameters based on an input hash, world type, and description. It retrieves context from a world ID if provided, defaults to generic values otherwise, and delegates map generation to a `GeneratorBridgeBox`. The generated parameters include a seed derived from the input hash to ensure reproducibility. Error handling ensures robustness with logging for debugging.

## Key Functions

### ``execute(input_data)``

Orchestrates map generation by fetching world context, invoking the generator bridge, and validating outputs.

### ``__init__()``

Initializes dependencies (`GeneratorBridgeBox`, `WorldReadBox`) and configures the box with metadata.

### ``world_read_box.execute()``

(Internal) Retrieves world metadata (type/description) from a world ID if provided.

### ``generator_bridge.execute()``

(Internal) Delegates map parameter generation to a Python generator with context-aware constraints.

## Usage

1. Pass an input hash and optional world metadata (ID, type, description) via `BoxInput`.
2. The box fetches world context if a `world_id` is provided, defaults to generic values otherwise.
3. Generates map parameters via `GeneratorBridgeBox`, ensuring a seed is included.
4. Returns a `BoxOutput` with `map_parameters`, `hash`, and `world_context`.

## Dependencies

> ``..core.box_interface``
> ``..generators.generator_bridge``
> ``..storage.world_read_box``
> ``logging``

## Related

- [[`generator_bridge]]
- [[`world_read_box]]
- [[`box_interface]]

>[!INFO] Context Fallback
> If `world_id` is provided but `world_type` is missing, the box queries `WorldReadBox` to fetch the world’s type and description. If neither is provided, defaults to `"Planet"` and an empty description.

>[!WARNING] Input Validation
> Missing `input_hash` triggers an immediate failure. Unhandled exceptions in the bridge or storage layers propagate as errors with logged details.
