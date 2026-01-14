**Tags:** #API, #StoryManagement, #ModularDesign, #ErrorHandling, #AsynchronousOperations
**Created:** 2026-01-13
**Type:** code-notes

# story_api_box

## Summary

```
Manages story-related API operations via a modular, extensible box system for world/story management.
```

## Details

> The `StoryAPIBox` class extends a base `Box` component to encapsulate all story-related API interactions. It validates input, routes operations (e.g., listing, generating, updating stories), and delegates calls to an external `apiClient`. The box enforces strict input/output schemas and handles errors via predefined `BoxErrorCode`/`BoxErrorCategory` conventions. Operations include listing stories by world, fetching stories, generating new stories, saving/updating elements, and deleting elements.

## Key Functions

### ``constructor(apiClient)``

Initializes the box with an API client and configures metadata (version, dependencies, supported operations).

### ``_executeInternal(inputData)``

Core method that routes operations via a `switch-case` and delegates to `apiClient` methods, wrapping results in `BoxOutput` (success/error).

### ``list``

Validates `world_id` and fetches stories for that world.

### ``get``

Supports fetching by `story_id` or `world_id`.

### ``generate``

Creates a new story using `world_id` and optional `timeline_id`/`options`.

### ``save``

Saves story elements via `story_elements` array.

### ``updateElement`/`deleteElement``

Manages individual story elements.

## Usage

1. Instantiate `StoryAPIBox` with an `apiClient`:
   ```js
   const box = new StoryAPIBox(apiClient);
   ```
2. Call operations via `_executeInternal` with structured input:
   ```js
   const input = { data: { operation: 'list', world_id: '123' } };
   const output = await box._executeInternal(input);
   ```
3. Handle `BoxOutput` (success/error) in downstream systems.

## Dependencies

> ``../core/box_interface.js` (Box class`
> ``BoxInput``
> ``BoxOutput``
> `error codes)`
> ``apiClient` (external service for story operations).`

## Related

- [[`Box` architecture]]
- [[BoxOutput` schema]]
- [[`apiClient` implementation]]

>[!INFO] Input Validation
> Mandatory fields (`world_id`, `story_id`) are enforced via schema and error handling. Missing fields trigger `MISSING_REQUIRED_FIELD` errors.

>[!WARNING] External API Dependencies
> All operations delegate to `apiClient`, so network failures or API errors propagate as `API_ERROR` (category `EXTERNAL`). Test edge cases (e.g., invalid `world_id`).
