**Tags:** #orchestration, #box-management, #transaction-handling, #dependency-resolution, #parallel-execution, #api-integration, #error-handling
**Created:** 2026-01-13
**Type:** code-library

# box-orchestrator

## Summary

```
Manages box execution workflows with dependency validation, parallel processing, and transaction support for a modular system.
```

## Details

> The `BoxOrchestrator` class centralizes box management, enabling automatic registration, validation, and execution of boxes (modular components) via a registry system. It handles dependency resolution, circular dependency detection, and transaction support with rollback capabilities. The orchestrator also supports parallel execution, performance monitoring, and standardized logging. Boxes are initialized dynamically based on available modules, with API-dependent boxes requiring an external `apiClient`. The system ensures robust error handling and metrics collection for execution tracking.

## Key Functions

### ``constructor(apiClient)``

Initializes the orchestrator with an API client, sets up transaction and metrics tracking, and validates the box registry.

### ``initializeBoxes()``

Dynamically registers all available boxes (common, API-dependent, and stage-specific) into the registry.

### ``_sanitizeParamsForLogging(params)``

Private helper to sanitize large objects/arrays for logging to avoid clutter.

### ``_registerBox(name, boxInstance)``

Internal method to register a box with the registry system.

### ``_initializeAllBoxes()``

Initializes all registered boxes (e.g., setting up API clients or dependencies).

### ``executeBox(boxName, input, options)``

Core method to execute a box, handling transactions, dependencies, and error rollback (not fully shown in snippet but implied).

### ``_validateRegistry()``

Validates the box registry for completeness and circular dependencies.

## Usage

1. **Initialization**: Instantiate `BoxOrchestrator` with an `apiClient`:
   ```javascript
   const orchestrator = new BoxOrchestrator(apiClient);
   ```
2. **Execute a Box**: Call `orchestrator.executeBox(boxName, input, options)` to run a box, passing its name, input data, and optional execution options (e.g., parallel execution flags).
3. **Dynamic Registration**: Boxes are auto-registered during initialization, but custom boxes can be added via `_registerBox()` if needed.
4. **Metrics/Logging**: Built-in metrics (`_globalMetrics`) track execution stats, and sanitized logs are generated via `_sanitizeParamsForLogging()`.

## Dependencies

> ``../boxes/core/box_interface.js``
> ``../boxes/common/error_handling_box.js``
> ``../boxes/common/validation_box.js``
> ``../boxes/common/map_render_box.js``
> ``../boxes/common/map_coordinate_box.js``
> ``../boxes/common/card_filtering_box.js``
> ``../boxes/common/data_loading_box.js``
> ``../boxes/common/story_export_box.js``
> ``../boxes/common/date_parsing_box.js``
> ``../boxes/common/timeline_position_box.js``
> ``../boxes/api/cards_api_box.js``
> ``../boxes/api/timelines_api_box.js``
> ``../boxes/api/worlds_api_box.js``
> ``../boxes/api/story_api_box.js``
> ``../boxes/api/auth_api_box.js``
> ``../boxes/stages/generate_box.js``
> ``../boxes/stages/link_box.js``
> ``../boxes/stages/card_box.js``
> ``../boxes/stages/timeline_box.js``
> ``../boxes/stages/story_box.js``
> ``../boxes/generators/hash_based_heightmap_utils_box.js``
> ``../boxes/generators/world_type_terrain_generator_box.js``
> ``../boxes/generators/world_type_heightmap_generator_box.js``
> ``../boxes/maps/map_color_box.js``
> ``./box-registry.js``
> ``./logger.js``

## Related

- [[box-registry]]
- [[logger]]
- [[box_interface]]

>[!INFO] Transaction Support
> The orchestrator uses a stack (`_transactionStack`) to manage nested transactions. If a box fails, all dependent transactions are rolled back automatically, ensuring data consistency.

>[!WARNING] API Client Dependency
> API-dependent boxes (e.g., `CardsAPIBox`) require an `apiClient` to initialize. Missing this will result in uninitialized boxes. Always pass a valid client during construction.
