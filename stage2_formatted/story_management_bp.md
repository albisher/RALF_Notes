**Tags:** #flask, #api-blueprint, #story-generation, #database-operations, #jwt-authentication, #card-management, #timeline-events
**Created:** 2026-01-13
**Type:** documentation-research

# story_management_bp

## Summary

```
Manages story generation and element handling via Flask blueprint with JWT authentication.
```

## Details

> This `StoryManagementAPIBox` class defines a Flask blueprint for handling story creation, retrieval, and database operations. It uses a `StoryChainOrchestratorBox` to generate stories from structured world data (e.g., characters, locations) and integrates with database boxes (`CardReadBox`, `CardWriteBox`, etc.) for CRUD operations on story elements (cards marked as `is_story_element=True`). The `/generate` endpoint validates inputs (e.g., `world_id`), fetches world context (e.g., characters, events), and delegates story generation to the orchestrator. The `/<story_id>` endpoint retrieves story elements via `CardReadBox` with optional `world_id` filtering.

## Key Functions

### ``StoryManagementAPIBox.__init__()``

Initializes database communication boxes and registers routes.

### ``_register_routes()``

Defines Flask routes for story generation (`/generate`) and retrieval (`/<story_id>`).

### ``generate_story()``

Validates inputs, constructs world data, and calls `StoryChainOrchestratorBox` to generate a story.

### ``get_story()``

Queries story elements (cards) from the database using `CardReadBox` with JWT authentication.

## Usage

1. **Initialize**: Create an instance of `StoryManagementAPIBox`.
2. **Register Routes**: Call `_register_routes()` to attach endpoints to a Flask blueprint.
3. **Generate Story**: Send a POST request to `/api/story/generate` with `world_id` and optional `timeline_id`/`location` to trigger story generation.
4. **Retrieve Story**: Fetch story elements via GET `/api/story/<story_id>` (with optional `world_id` query param).

## Dependencies

> ``flask``
> ``flask-jwt-extended``
> ``models.db``
> ``Card``
> ``Timeline``
> ``TimelineEvent``
> ``World``
> ``WorldElement``
> ``CardReadBox``
> ``CardWriteBox``
> ``CardUpdateBox``
> ``CardDeleteBox``
> ``StoryChainOrchestratorBox``
> ``BoxInput`.`

## Related

- [[models]]
- [[card_read_box]]
- [[story_chain_orchestrator]]

>[!INFO] Context Validation
> The `/generate` endpoint validates `world_id` and retrieves associated `World`, `Timeline`, and `WorldElement` data dynamically. Missing or invalid data returns HTTP 400/404 errors.

>[!WARNING] Error Handling
> Uncaught exceptions log to `logger` with `exc_info=True` and return a generic 500 error. Customize error handling for production to avoid exposing sensitive details.
