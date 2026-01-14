**Tags:** #Vue.js, #Reactivity, #API-Data-Flow, #Composable-Pattern, #Timeline-Visualization, #Data-Extraction, #Year-Markers, #Event-Rendering
**Created:** 2026-01-13
**Type:** documentation

# TIMELINE_POPULATION_FLOW

## Summary

```
Document outlines the structured flow of populating a timeline with cards and year markers, detailing initialization, API data loading, and rendering phases.
```

## Details

> This document traces the complete workflow for populating a top-level timeline in a Vue.js application. It begins with initialization in `WorkflowPage.vue`, where data orchestration kicks off via `loadWorldData()`. The process splits into two primary data loading phases: **Card Loading** (via `CardsAPIBox` and `useCardOperations`) and **Timeline Event Loading** (via `TimelinesAPIBox` and `useTimelineOperations`). The **Year Extraction Phase** uses `YearExtractionBox` and `TopTimeline.vue` to parse dates from cards and generate year markers, while the **Marker Generation Phase** employs `TimelinePositionBox` and `DateParsingBox` to calculate positions for events. The flow ensures reactive updates via Vue’s composables and composable patterns, with fallback mechanisms for missing data.

## Key Functions

### ``WorkflowPage.vue``

- `mounted()`: Initializes data loading.

### ``loadWorldData()``

Orchestrates all data fetching (cards, events, years).

### ``CardsAPIBox``

- `_executeInternal()`: Validates and executes API calls for cards.

### ``list()``

Retrieves card data via `boxOrchestrator`.

### ``useCardOperations.js``

- `loadCards()`: Maps API response to card format and filters them.

### ``filteredCards``

Computed property for dynamic filtering.

### ``TimelinesAPIBox``

- Handles timeline-related API operations (e.g., `list`).

### ``useTimelineOperations.js``

- `loadTimelineEvents()`: Maps events to `timelineNodes` and triggers `generateTopTimelineMarkers()`.

### ``YearExtractionBox``

- `_extractYearsFromCards()`: Extracts years from cards using regex patterns.

### ``_extractYearFromCard()``

Parses date strings (e.g., `"Year 2020"` or ISO format).

### ``TopTimeline.vue``

- `extractYearsFromCards()`: Uses `YearExtractionBox` to merge years from cards and markers.

### ``yearMarkers``

Computed property generating year positions (0–100%).

### ``TimelinePositionBox``

- Calculates positions for events based on year ranges (e.g., `((year - minYear) / yearRange) * 90 + 5`).

### ``calculateYearMarkersFromCards()``

Direct year extraction in `WorkflowPage.vue` (fallback to `YearExtractionBox`).

## Usage

1. **Initialize**: Call `loadWorldData()` in `WorkflowPage.vue` to start data loading.
2. **Card Loading**: `loadCards()` via `useCardOperations` populates `cards.value`.
3. **Timeline Events**: `loadTimelineEvents()` processes events and triggers `generateTopTimelineMarkers()`.
4. **Year Extraction**: `extractYearsFromCards()` in `TopTimeline.vue` merges years from cards and markers.
5. **Rendering**: `yearMarkers` computed property generates positions for year markers, which render dynamically.

## Dependencies

> `Vue 3 (Composition API)`
> ``boxOrchestrator` (internal orchestrator for API calls)`
> ``ValidationBox``
> ``apiClient``
> ``CardFiltering` box`
> ``DateParsingBox``
> ``TimelinePositionBox``
> ``useCardOperations``
> ``useTimelineOperations``
> ``YearExtractionBox`.`

## Related

- [[`API-Box-Architecture]]
- [[`Vue-Composable-Guide]]
- [[`Timeline-Visualization-Design]]

>[!INFO] **Reactive Updates**
> The composables (`useCardOperations`, `useTimelineOperations`) use Vue’s reactive refs (`cards.value`, `timelineNodes`) to ensure UI updates reflect changes in data.


>[!WARNING] **Fallback Logic**
> If no events are found, `WorkflowPage.vue` falls back to `generateTimelineFromCards()`, which extracts years directly from cards (e.g., `card.content.year`). This avoids empty timelines.


>[!INFO] **Date Parsing Flexibility**
> The `YearExtractionBox` supports multiple date formats (e.g., `"Year 2020"`, `YYYY-MM-DD`) via regex patterns. The `TopTimeline.vue` component mirrors this logic in `extractYearFromCard()` for direct extraction.


>[!WARNING] **API Dependency**
> All data loading relies on `boxOrchestrator.execute()`, which abstracts API calls. If `CardsAPIBox` or `TimelinesAPIBox` fails, the entire workflow may stall. Error handling should be implemented at the orchestrator level.
