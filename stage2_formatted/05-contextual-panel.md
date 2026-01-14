**Tags:** #Vue.js, #Dynamic UI, #Contextual Information, #Timeline Visualization, #Event Management, #State Management
**Created:** 2026-01-13
**Type:** documentation

# 05-contextual-panel

## Summary

```
Design and implementation details for a **contextual information panel** that dynamically updates based on a slider position, displaying relevant events, cards, and settings.
```

## Details

> This design iteration focuses on creating a **contextual panel** that adjusts content (events, cards, settings) based on the user’s slider position in a timeline. The panel is structured into collapsible sections, ensuring efficient space usage while providing relevant information. The system filters data within a configurable ±5-year range, dynamically updating the displayed events and cards. When an event is selected, an editor appears, allowing modifications. The implementation uses Vue.js for reactivity and state management, with modular components for events, cards, and settings.

## Key Functions

### `PanelSection`

Displays collapsible sections with titles and counts.

### `EventList`

Shows filtered events with click handlers for selection.

### `CardGrid`

Displays a compact grid of cards within a collapsible section.

### `TimelineSettingsQuick`

Provides quick access to settings via a modal.

### `EventEditorCompact`

Compact editor for editing selected events.

### `getEventsAtYear(year)`

Filters events within ±5 years of the selected year.

### `getCardsAtYear(year)`

Filters cards within ±5 years of the selected year.

### `watch(sliderPosition)`

Updates panel content when slider position changes.

## Usage

1. **Initialize the Panel**: Mount the `ContextualPanel` component in a Vue app with a slider and event/card data.
2. **Set Slider Position**: Update `sliderPosition` to trigger dynamic updates.
3. **Handle Event Selection**: Use `@event-selected` to trigger editor logic.
4. **Configure Settings**: Use `@edit` to open a modal for settings adjustments.

## Dependencies

> `Vue.js (3.x)`
> `Pinia (state management)`
> `Vuex (optional for complex state)`
> `Tailwind CSS (for styling)`
> `Event/Card data arrays (local or API-based).`

## Related

- [[Design Iteration 4: Timeline Slider]]
- [[Vue]]
- [[State Management Patterns]]

>[!INFO] Dynamic Filtering
> The ±5-year range ensures relevant content is always visible, but this can be adjusted via configuration. Efficient filtering (e.g., pre-sorting data by year) improves performance.

>[!WARNING] Empty States
> When no events/cards exist within the range, the panel displays empty states (e.g., "No events at this time"). Ensure placeholder UI is clear to avoid confusion.
