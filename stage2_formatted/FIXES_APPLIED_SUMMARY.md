**Tags:** #refactoring, #architecture, #composable-pattern, #box-orchestration, #coordinate-transformation, #ui-component-separation
**Created:** 2026-01-13
**Type:** architecture

# FIXES_APPLIED_SUMMARY

## Summary

```
Document summarizes fixes applied for modularizing coordinate and card operations in a UI framework, with partial completion on refactoring large components to reduce file size.
```

## Details

> This document outlines completed and incomplete fixes for improving modularity and maintainability in a Vue.js-based UI framework. Key improvements include:
> - Creation of reusable `MapCoordinateBox` and `CardFilteringBox` for coordinate calculations and card logic.
> - Implementation of composables (`useCardOperations`, `useMapOperations`) to encapsulate related operations.
> - Updated coordinate calculations in `WorkflowPage.vue` and `CardViewPage.vue` to use centralized `MapCoordinateBox`.
> - Critical refactoring tasks remain, particularly addressing file size violations in `WorkflowPage.vue` (2,724 lines) and `CardViewPage.vue` (948 lines) by extracting logic into composables and components.

## Key Functions

### `MapCoordinateBox`

Handles coordinate projections (`project`, `convert`, `normalize`, `screenToLatLon`, `latLonToScreen`).

### `CardFilteringBox`

Manages filtering, sorting, and search operations (`filter`, `sort`, `search`, `filterAndSort`).

### `useCardOperations`

Centralizes card state and operations (loading, filtering, sorting, search, selection).

### `useMapOperations`

Manages map data and coordinate transformations (projection, conversion, location selection).

### `WorkflowPage.vue`

Large component needing refactoring into composables (e.g., `useWorldOperations`, `useTimelineOperations`).

### `CardViewPage.vue`

Large component needing modularization into smaller components (e.g., `CardViewHeader`, `CardViewGrid`).

## Usage

To apply these fixes:
1. **For completed fixes**: Use `MapCoordinateBox` and `CardFilteringBox` in components via `box-orchestrator.js` registration.
2. **For refactoring**: Replace monolithic logic in `WorkflowPage.vue`/`CardViewPage.vue` with newly created composables/boxes (e.g., `useCardOperations` for card logic).
3. **For remaining work**: Extract business logic (e.g., date parsing, timeline calculations) into dedicated boxes (e.g., `DateParsingBox`, `TimelinePositionBox`).

## Dependencies

> `Vue.js 3.x`
> `Composition API`
> ``box-orchestrator.js``
> ``DateParsingBox``
> ``TimelinePositionBox` (existing)`
> ``WorldsAPIBox` (existing).`

## Related

- [[FIXES_APPLIED_SUMMARY - Code Assessment Findings]]
- [[Architecture_Refactoring_Guide]]
- [[Vue_Composition_API_Examples.]]

>[!INFO] Critical Refactoring
> Focus on breaking down `WorkflowPage.vue` into composables (e.g., `useWorldOperations`, `useTimelineOperations`) to reduce file size from 2,724 lines to under 500. Extract business logic (e.g., date parsing, filtering) into dedicated boxes for modularity.

>[!WARNING] File Size Violation
> `CardViewPage.vue` (948 lines) must be split into smaller components (e.g., `CardViewHeader`, `CardViewGrid`) to comply with size targets. Overlapping logic with `useCardOperations` composable should be extracted early to avoid redundancy.
