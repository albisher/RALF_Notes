**Tags:** #Dynamic class loading, #Dependency injection, #Type registry, #Python module discovery
**Created:** 2026-01-13
**Type:** code-library

# box_loader

## Summary

```
Manages dynamic box class discovery, registration, and instantiation for a modular system.
```

## Details

> This system dynamically loads Python classes inheriting from a base `Box` interface from a directory structure, registers them in a registry, and provides methods to retrieve or instantiate them. It handles discovery via recursive file traversal, imports modules dynamically, and caches instances for reuse. The `BoxRegistry` maintains mappings between box names and their classes, while `BoxLoader` orchestrates discovery and instantiation.

## Key Functions

### `BoxRegistry.register`

Registers a box class with a customizable name, validating inheritance from `Box`.

### `BoxRegistry.get_box_instance`

Retrieves or creates a cached instance of a box class.

### `BoxLoader.discover_boxes`

Recursively scans a directory for `.py` files, skips excluded files, and loads box classes from each file.

### `BoxLoader._load_box_from_file`

Imports a module and inspects its classes to find subclasses of `Box`, registering them.

### `BoxLoader.load_box`

Delegates to the registry to get an instance of a box by name with provided constructor arguments.

## Usage

1. Initialize `BoxLoader` with a base path (defaults to parent of parent directory).
2. Call `discover_boxes()` to populate the registry with all boxes in the directory.
3. Use `load_box()` to retrieve a box instance by name with optional constructor arguments.
4. Access the registry directly via `get_registry()` for programmatic control.

## Dependencies

> ``os``
> ``importlib``
> ``inspect``
> ``logging``
> ``pathlib``
> ``.box_interface` (base `Box` class)`
> `external logging framework.`

## Related

- [[Dynamic Module Discovery Patterns]]
- [[Dependency Injection in Python]]

>[!INFO] Exclusion Logic
> Skips `__init__.py`, `box_loader.py`, `box_interface.py`, and `orchestrator.py` during discovery to avoid circular dependencies or redundant files.

>[!WARNING] Error Handling
> Logs warnings for import failures but continues discovery; fails silently only if instantiation throws an exception.
