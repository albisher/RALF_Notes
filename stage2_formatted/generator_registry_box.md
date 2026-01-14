**Tags:** #automation, #registry, #module-discovery, #dependency-management
**Created:** 2026-01-13
**Type:** code-notes

# generator_registry_box

## Summary

```
Manages auto-discovery and registration of generators (built-in and custom) for a system.
```

## Details

> This `GeneratorRegistryBox` class dynamically discovers built-in generators from a predefined folder (`Generators/`) and allows registration/unregistration of custom generators. It uses a `Box` interface to handle operations like listing, retrieving, or managing generators via an input-driven execution system. The registry stores metadata about each generator, including its ID, path, supported constraints, and function name, enabling flexible querying and execution.
> 
> The class initializes with a base path for generators, dynamically adds this path to `sys.path` to enable Python module imports, and implements methods to handle operations like discovery, listing, registration, and retrieval of generators.

## Key Functions

### ``discover_generators()``

Scans the `Generators/` directory for all Python modules, populates the internal registry with metadata about each generator, and marks discovery as complete.

### ``list_generators()``

Returns a filtered list of registered generators based on customization flags (`include_custom`, `type_filter`).

### ``get_generator()``

Retrieves metadata for a specific generator by its ID.

### ``register_generator()``

Adds a custom generator to the registry using provided metadata.

### ``unregister_generator()``

Removes a generator from the registry by its ID.

### ``execute()``

Orchestrates operations (discover, list, get, register, unregister) based on input data, returning success/error status and relevant data.

## Usage

1. Initialize `GeneratorRegistryBox` with an optional `generators_base_path` (defaults to a relative path).
2. Call `execute()` with an input dictionary specifying an operation (e.g., `{"operation": "discover"}`).
3. For listing generators: `{"operation": "list", "include_custom": True, "type_filter": "physical_form"}`.
4. For retrieving a generator: `{"operation": "get", "generator_id": "plants"}`.
5. For registering a custom generator: `{"operation": "register", "generator_metadata": {...}}`.
6. For unregistering: `{"operation": "unregister", "generator_id": "characters"}`.

## Dependencies

> ``os``
> ``sys``
> ``importlib.util``
> ``inspect``
> ``logging``
> ``typing` (standard libraries)
`..core.box_interface` (custom module for `Box``
> ``BoxInput``
> ``BoxOutput` classes)`

## Related

- [[`box_interface]]
- [[` directory structure]]

>[!INFO] Dynamic Path Handling
> The code dynamically adds the `generators_base_path` to `sys.path` to ensure Python can import modules from the specified directory, even if it’s not in the default search path.

>[!WARNING] State Management
> The `_discovered` flag prevents redundant discovery calls, but manual state checks (e.g., `if self._discovered`) are required to avoid infinite loops or stale registries.
