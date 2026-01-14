**Tags:** #data-loading, #box-architecture, #json-processing, #error-handling, #async-io
**Created:** 2026-01-13
**Type:** code-notes

# data_loading_box

## Summary

```
Handles loading static JSON data files via configurable paths with robust error handling.
```

## Details

> This `DataLoadingBox` class extends a base `Box` component to fetch and parse static data files (primarily JSON) from configurable paths. It validates inputs, checks response validity, and ensures proper JSON parsing before returning structured output. The box supports dynamic path resolution via a configuration service and includes comprehensive error handling for network issues, invalid responses, and JSON parsing failures.

## Key Functions

### ``constructor()``

Initializes the box with metadata (version, dependencies, input/output schemas).

### ``_executeInternal(inputData)``

Core async method that:

## Usage

1. Instantiate `DataLoadingBox` (inherits Box).
2. Call `_executeInternal` with an input object containing:
   - `dataPath`: Path to JSON file (string).
   - Optional `operation`: (unused in this version).
3. Handle output via `BoxOutput.success({ data })` (valid JSON) or `BoxOutput.error` (failures).

## Dependencies

> ``../core/box_interface.js` (Box class and utilities)`
> ``../../services/config.js` (path resolution)`
> ``fetch` (built-in browser/Node.js API).`

## Related

- [[`Box` architecture documentation]]
- [[`config]]

>[!INFO] Dynamic Path Resolution
> Uses `config.getDataPath()` to resolve paths if provided; otherwise, falls back to raw `dataPath`.

>[!WARNING] Error Preview Limitation
> For non-JSON responses, only shows first 200 chars of raw text to avoid flooding error messages.
