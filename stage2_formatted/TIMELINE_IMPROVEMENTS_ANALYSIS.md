**Tags:** #reactivity, #vuejs, #timeline, #data-loading, #async-processing, #race-condition, #code-duplication, #performance-optimization
**Created:** 2026-01-13
**Type:** documentation

# TIMELINE_IMPROVEMENTS_ANALYSIS

## Summary

```
Analyzes timeline data population flow in a Vue.js component, identifying timing issues, redundant logic, and inefficient data handling, then proposes centralized reactive improvements.
```

## Details

> The document analyzes a Vue.js component (`TopTimeline.vue`) responsible for populating a timeline with years extracted from cards and markers. Key issues include:
> 1. **Race conditions** where year extraction occurs before cards are loaded (e.g., in `mounted()`), requiring a 500ms `setTimeout` workaround.
> 2. **Redundant extraction logic** implemented in multiple places (e.g., `mounted()`, `watch: cards`, computed properties), leading to code duplication and inconsistent behavior.
> 3. **Inefficient watching** of the `cards` array with `deep: false`, missing deep changes and unnecessarily comparing IDs/names.
> 4. **Heavy work in computed properties**, violating Vue’s reactivity principles by performing extraction synchronously.
> 
> The analysis highlights that year extraction should be deferred until cards are fully populated, and logic should be centralized to avoid duplication and improve maintainability.

## Key Functions

### ``mounted()``

Initializes the `YearExtractionBox` but does not extract years immediately (problematic timing).

### ``watch`

cards`: Triggers year extraction when cards change, but uses inefficient checks and lacks deep watching.

### ``watch`

markers`: Similar to `cards`, but not detailed in the snippet.

### ``yearMarkers()``

Computed property that extracts years as a fallback, violating Vue’s reactivity rules.

### ``extractYearsFromCards()``

Core method for extracting years from cards/markers (proposed to be centralized).

## Usage

The component (`TopTimeline.vue`) is used to render a timeline with years dynamically extracted from loaded cards and markers. The improvements focus on ensuring years are extracted **only after data is ready** and centralizing logic to avoid redundancy.

## Dependencies

> `Vue.js (3.x)`
> `Composition API (likely used for reactivity)`
> ``YearExtractionBox` class`
> ``extractYearFromCard` helper function.`

## Related

- [[Vue]]
- [[Asynchronous data loading in Vue]]
- [[Race conditions in frontend development]]

>[!INFO] Critical Race Condition
> The original `mounted()` call extracts years **before** `loadWorldData()` (an async operation in the parent component) completes, causing a race condition. This forces a hacky `setTimeout` workaround, which is unreliable and inefficient.


>[!WARNING] Performance Overhead
> Multiple extraction points (e.g., `watch: cards`, computed property) trigger redundant computations, increasing memory usage and rendering delays. Centralizing logic reduces this overhead.
