**Tags:** #dependency-management, #box-registry, #circular-dependency-detection, #metadata-tracking
**Created:** 2026-01-13
**Type:** code-notes

# box-registry

## Summary

```
Manages box registration, dependency validation, and metadata tracking for modular box systems.
```

## Details

> The `BoxRegistry` class centralizes box lifecycle management, including registration, unregistration, metadata storage, and dependency validation. It uses two internal Maps (`_boxes` and `_boxMetadata`) to track box instances and their metadata. The system validates box compliance with the `Box` interface, checks for circular dependencies, and ensures all dependencies exist before registration. Metadata includes version, author, operations, and parallel execution support.

## Key Functions

### `register`

Validates and stores a box instance along with its metadata.

### `unregister`

Removes a box from both the registry and its metadata.

### `get`

Retrieves a box instance by name.

### `has`

Checks if a box exists in the registry.

### `getMetadata`

Fetches metadata for a specific box.

### `list`

Returns all registered box names.

### `getAllMetadata`

Returns metadata for all registered boxes.

### `_validateBox`

Private method to ensure a box conforms to the `Box` interface.

### `checkCircularDependencies`

Detects cycles in dependency graphs.

### `validateDependencies`

Identifies missing dependencies across all registered boxes.

## Usage

```javascript
const registry = new BoxRegistry();

// Register a box
registry.register('myBox', new MyBox(), { custom: 'metadata' });

// Check if a box exists
registry.has('myBox');

// Get box metadata
registry.getMetadata('myBox');

// Validate dependencies
const issues = registry.validateDependencies();
```

## Dependencies

> ``../boxes/core/box_interface.js` (Box class and related types)`
> ``./logger.js` (logging utilities)`

## Related

- [[Box Interface Documentation]]
- [[Dependency Resolution Guide]]

>[!INFO] Metadata Extensibility
> Metadata can be extended with custom properties via the `metadata` parameter in `register()`, allowing flexible configuration beyond defaults.

>[!WARNING] Circular Dependency Risk
> `checkCircularDependencies()` must be called explicitly before registration to avoid runtime errors in dependency chains. Unchecked cycles may cause infinite loops.
