**Tags:** #flask, #api, #research, #blueprint, #data-processing, #storage, #integration
**Created:** 2026-01-13
**Type:** documentation-research-api

# research_bp

## Summary

```
Flask blueprint module for managing research API endpoints, handling queries, storage, and integration workflows.
```

## Details

> This code defines a Flask blueprint (`ResearchAPIBox`) for a research-focused API system. It integrates three core components: a research service handler, a storage system, and an integrator module. The blueprint registers four routes:
> - **POST `/query`**: Executes a research query, processes results, and saves them to storage.
> - **GET `/list`**: Retrieves a list of saved research entries.
> - **GET `/<research_id>`**: Fetches a specific research entry by ID.
> - **POST `/<research_id>/integrate`**: Integrates research results into a story context with optional edits.
> 
> The system validates inputs, logs errors, and returns structured JSON responses. It relies on a `Box` interface for modular service execution, abstracting dependencies like `ResearchServiceBox`, `ResearchStorageBox`, and `ResearchIntegratorBox`.

## Key Functions

### ``ResearchAPIBox``

Core class initializing the Flask blueprint and registering routes.

### ``_register_routes()``

Dynamically registers all API endpoints on the blueprint.

### ``query_research()``

Handles POST requests for research queries, validates inputs, and orchestrates service/storage workflows.

### ``list_research()``

Returns a list of saved research entries via GET `/list`.

### ``get_research(research_id)``

Retrieves a specific research entry by ID via GET `/<research_id>`.

### ``integrate_research(research_id)``

Integrates research into a story context via POST `/<research_id>/integrate`.

## Usage

1. Initialize `ResearchAPIBox` in your Flask app.
2. Register the blueprint with `app.register_blueprint(ResearchAPIBox.blueprint)`.
3. Call endpoints via HTTP requests:
   - **POST `/api/research/query`**: Submit a research query with `query`, `story_context`, `model`, and `api_key`.
   - **GET `/api/research/list`**: Retrieve saved research entries.
   - **GET `/api/research/<research_id>`**: Fetch a specific research entry.
   - **POST `/api/research/<research_id>/integrate`**: Integrate research into a story with optional edits.

## Dependencies

> ``flask``
> ``request``
> ``jsonify``
> ``Box``
> ``BoxInput``
> ``BoxOutput``
> ``ResearchServiceBox``
> ``ResearchStorageBox``
> ``ResearchIntegratorBox``

## Related

- [[research_service_research_service_box]]
- [[research_storage_research_storage_box]]
- [[research_integrator_research_integrator_box]]

>[!INFO] Input Validation
> Mandatory fields (e.g., `query`) are checked early to avoid processing invalid requests. Non-critical failures (e.g., storage errors) log warnings but do not halt execution.


>[!WARNING] Error Handling
> Uncaught exceptions log to `logger` with `exc_info=True` and return HTTP 500. Missing research IDs return HTTP 404. Always validate `result.success` before returning data.
