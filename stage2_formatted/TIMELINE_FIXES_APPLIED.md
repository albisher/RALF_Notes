**Tags:** #reactivity, #vuejs, #timing-issues, #race-conditions, #code-refactoring, #vue-computed, #setTimeout-hack, #data-fetching
**Created:** 2026-01-13
**Type:** documentation

# TIMELINE_FIXES_APPLIED

## Summary

```
Documentation summarizing fixes for critical issues in a Vue.js timeline component, improving timing, reactivity, and code organization.
```

## Details

> This document details five key fixes applied to a Vue.js component (`TopTimeline.vue`) to resolve issues related to timing, race conditions, and inefficient logic. The fixes centralize year extraction logic, eliminate hacks like `setTimeout`, and enhance reactivity with proper watchers and loading states. The refactoring ensures the year scale updates correctly after card loading and prevents redundant computations.

## Key Functions

### ``extractYearsFromCards()``

Centralized method for extracting years from cards, now guarded by loading state to prevent race conditions.

### ``watch`

cards` handler**: Reactive watcher that triggers extraction after `$nextTick` to ensure cards are loaded.

### ``yearMarkers()` (computed)`

Pure computed property that relies on pre-extracted years, avoiding side effects.

### ``isLoadingYears`/`yearsExtracted``

State flags to track extraction progress and prevent concurrent operations.

## Usage

1. **Initialization**: Initialize `YearExtractionBox` and ensure `cards` data is reactive.
2. **Trigger Extraction**: Use the centralized `extractYearsFromCards()` method when cards or markers change.
3. **Reactivity**: Leverage Vue’s reactivity system with `watch` and `computed` to maintain state consistency.

## Dependencies

> `Vue.js (3.x)`
> `Vuex (if applicable for state management)`
> `Vuex devtools (for debugging reactivity).`

## Related

- [[Vue]]
- [[Vue]]
- [[Race Condition Prevention in Single-File Components]]

>[!INFO] **Critical Timing Fix**
> The removal of `setTimeout` ensures the year scale appears immediately after cards load, eliminating visual delays. The `$nextTick` wrapper guarantees cards are fully rendered before extraction.


>[!WARNING] **Loading State Protection**
> The `isLoadingYears` flag prevents race conditions by blocking concurrent extractions, improving UI responsiveness and avoiding errors during rapid data changes.
