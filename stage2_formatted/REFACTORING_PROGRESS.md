**Tags:** #refactoring, #object-oriented-design, #code-organization, #box-architecture, #mixin-pattern, #component-extraction
**Created:** 2026-01-13
**Type:** code-refactoring-progress

# REFACTORING_PROGRESS

## Summary

```
Tracks progress of refactoring a monolithic application into a modular architecture using box-based components and mixins.
```

## Details

> This document records a refactoring effort to restructure large Vue components (`WorkflowPage.vue`, `CardViewPage.vue`) into smaller, reusable components and boxes. The goal is to improve separation of concerns, reduce file size, and eliminate direct API calls by delegating logic to specialized boxes (e.g., `MapCoordinateBox`, `CardFilteringBox`). Progress includes completed tasks like creating shared mixins and fixing API violations, while remaining challenges focus on extracting business logic into components and boxes, particularly for date parsing, map rendering, and filtering logic.

## Key Functions

### `MapCoordinateBox`

Handles coordinate projection, conversion, and normalization.

### `CardFilteringBox`

Manages card filtering, sorting, and searching.

### `WorldsAPIBox`

Extends API operations (`updateTimeSystem`, `updateInfo`, `updateRules`).

### `workflowStagesMixin`

Manages workflow stage lifecycle.

### `worldOperationsMixin`

Handles world-related operations.

### `CardViewFilters.vue`

UI component for card filtering.

### `CardViewMap.vue** (planned)`

Extracts map rendering logic.

## Usage

- **Current State**: Components now use `BoxOrchestrator` to delegate logic to boxes (e.g., `WorldsAPIBox`).
- **Next Steps**: Extract logic into standalone components (e.g., `CardViewMap.vue`) and boxes (e.g., `DateParsingBox`).
- **Key Action**: Replace monolithic logic with box-based operations and modular components.

## Dependencies

> ``BoxOrchestrator``
> ``ValidationBox``
> ``secureStorage``
> ``Vue.js` (for Vue components)`
> ``Vuex` (for state management)`
> ``Vuex-persist` (for persistence).`

## Related

- [[Refactoring_Architecture_Decision]]
- [[Box_Design_Patterns]]
- [[Vue_Component_Extraction_Guide]]

>[!INFO] File Size Tradeoff
> Incremental increases in file size (e.g., `WorkflowPage.vue` from 2,693 to 2,732 lines) occur due to proper box orchestrator calls, but this is expected. Future extraction of components will reduce sizes significantly.


>[!WARNING] Critical Path
> Extracting map rendering logic into `CardViewMap.vue` and using `MapCoordinateBox` must be prioritized to avoid redundant calculations and improve maintainability.
