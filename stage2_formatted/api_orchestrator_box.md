**Tags:** #API_Orchestration, #Modular_Architecture, #Event-Driven, #Dependency_Management
**Created:** 2026-01-13
**Type:** code-notes

# api_orchestrator_box

## Summary

```
Manages routing of API requests to specialized API handlers for domain-specific operations.
```

## Details

> The `APIOrchestratorBox` class acts as a central coordinator for multiple API-related boxes (e.g., `CardsAPIBox`, `TimelinesAPIBox`). It validates input requests by domain (e.g., `cards`, `timelines`) and delegates execution to the appropriate specialized box. The orchestrator validates the input schema (e.g., enforces required `domain` field) and routes operations like `execute` to domain-specific handlers. Error handling propagates exceptions to a unified `BoxOutput.error` format, categorizing issues (e.g., invalid input, API failures).

## Key Functions

### ``constructor(apiClient)``

Initializes the orchestrator with dependencies (e.g., `CardsAPIBox`, `TimelinesAPIBox`) and configures metadata (version, author, timeout).

### ``_executeInternal(inputData)``

Routes input to the correct box via a `switch-case` on the `domain` field, then invokes the box’s `execute` method with remaining parameters. Returns a `BoxOutput` (success/error).

## Usage

1. Instantiate with an `apiClient`:
   ```js
   const orchestrator = new APIOrchestratorBox(apiClient);
   ```
2. Call `_executeInternal` with an input object:
   ```js
   const result = await orchestrator._executeInternal({
     data: { domain: 'cards', operation: 'fetch' }
   });
   ```
3. Handle `BoxOutput` (success/error) in downstream logic.

## Dependencies

> ``../core/box_interface.js``
> ``CardsAPIBox``
> ``TimelinesAPIBox``
> ``WorldsAPIBox``
> ``StoryAPIBox``

## Related

- [[Space Peral Core Box Interface]]
- [[CardsAPIBox]]
- [[TimelinesAPIBox]]

>[!INFO] Input Validation
> The orchestrator enforces schema validation (e.g., `domain` must be one of `['cards', 'timelines', 'worlds', 'story']`). Invalid inputs trigger `BoxErrorCode.INVALID_FIELD_VALUE`.

>[!WARNING] Error Propagation
> Uncaught exceptions in child boxes (e.g., `CardsAPIBox`) are caught and wrapped in `BoxOutput.error` with `BoxErrorCategory.EXTERNAL`, ensuring consistent error handling across domains.
