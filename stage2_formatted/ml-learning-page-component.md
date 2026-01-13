**Tags:** #Vue, #MLLearning, #Component, #DataFetching, #Vuex, #Reactivity
**Created:** 2026-01-13
**Type:** code-notes

# ml-learning-page-component

## Summary

```
A Vue.js component for displaying ML learning data with interactive drone selection and data export capabilities.
```

## Details

> `MLLearningPageComponent` is a Vue.js single-responsibility component that renders an ML learning view when `currentView` is set to `'ml-learning'`. It acts as a wrapper around `MLLearningViewComponent`, passing props like `mlLearningData`, `selectedMLDrones`, and loading/error states. It emits events for data fetching, exporting, and selection management. The component uses Vue’s reactivity to handle dynamic updates via `v-model` for drone selection and emits custom events for external interactions.

## Key Functions

### ``MLLearningPageComponent``

Main component managing ML learning data display and event handling.

### ``MLLearningViewComponent``

Child component rendering the actual ML learning UI with drone selection and data visualization.

## Usage

```javascript
// Import and use in a Vue app:
import MLLearningPageComponent from './MLLearningPageComponent.vue';
new Vue({
  components: { MLLearningPageComponent },
  template: `<MLLearningPageComponent ... />`,
  data() { return { currentView: 'ml-learning' }; }
});
```
- **Props**: Required `currentView` (e.g., `'ml-learning'`), optional `mlLearningData`, `selectedMLDrones`, etc.
- **Emits**: Triggered via `@fetch-ml-learning-data`, `@export-selected-ml-data`, etc.

## Dependencies

> `Vue.js (v3+)`
> ``MLLearningViewComponent` (internal dependency)`

## Related

- [[Vue]]
- [[MLLearningViewComponent]]

>[!INFO] Single Responsibility
> This component **only** renders ML learning data; logic for fetching/processing data should be handled elsewhere (e.g., a Vuex store or API service).

>[!WARNING] Event Overload
> Emitting multiple events (e.g., `update:selected-ml-drones` + `@select-all-ml-drones`) may cause confusion. Clarify event names in documentation.
