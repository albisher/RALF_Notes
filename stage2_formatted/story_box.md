**Tags:** #story-management, #api-integration, #box-architecture, #async-processing
**Created:** 2026-01-13
**Type:** code-notes

# story_box

## Summary

```
Manages story stage operations via API client, supporting generation, listing, retrieval, and saving stories.
```

## Details

> The `StoryBox` class extends a generic `Box` component to handle story-related workflows through a modular API client (`StoryAPIBox`). It processes input operations (`generate`, `list`, `get`, `save`) by delegating to the underlying API layer, validating inputs/outputs via JSON schemas, and enforcing a 60-second timeout for long-running tasks. Error handling routes unexpected operations to a fallback message, while external API failures propagate as `API_ERROR`.

## Key Functions

### ``constructor(apiClient)``

Initializes the box with metadata (version, dependencies) and configures input/output schemas for supported operations.

### ``_executeInternal(inputData)``

Orchestrates operation execution by routing requests to `StoryAPIBox` via `BoxInput` wrappers, with fallback error handling for unsupported operations.

## Usage

1. Instantiate `StoryBox` with an API client.
2. Call `_executeInternal` with an input object containing `operation` (e.g., `generate`) and parameters (e.g., `worldId`).
3. Handle the returned `BoxOutput` (success/error).

## Dependencies

> ``../core/box_interface.js``
> ``../api/story_api_box.js``
> ``Box``
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory``

## Related

- [[`StoryAPIBox`]]
- [[`Box` architecture documentation]]

>[!INFO] Timeout Handling
> Story generation may exceed 60 seconds; ensure client handles timeouts gracefully.

>[!WARNING] Deprecation Warning
> Unknown operations trigger a redirect to `StoryExportBox`; check for breaking changes in future versions.
