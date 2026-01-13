**Tags:** #VueJS, #React, #UI-Component, #Modal, #Building-Details, #Single-Responsibility
**Created:** 2026-01-13
**Type:** code-notes

# details-modal-component

## Summary

```
A Vue.js modal component displaying detailed information about buildings, drones, or bases.
```

## Details

> `DetailsModalComponent` is a Vue.js template-based component designed to render detailed information in a modal dialog. It dynamically renders content based on the `detailsModal` prop, which includes `show`, `title`, and `data` (e.g., building attributes). The component uses conditional rendering (`v-if`) to display different sections (e.g., building details) and formats data like coordinates or dimensions. It emits a `close-modal` event when the close button is clicked or when clicking outside the modal.
> 
> The `formatPosition` helper function likely converts coordinate data into a readable format (e.g., latitude/longitude). The component adheres to a single responsibility principle, focusing solely on rendering details without additional logic.

## Key Functions

### ``template``

Vue.js template defining the modal structure with conditional rendering for different content types (e.g., `building`).

### ``@click.self``

Event handler for closing the modal when clicking outside the overlay.

### ``$emit('close-modal')``

Emits an event to notify parent components to close the modal.

### ``formatPosition(detailsModal.data.position)``

Helper function (not shown in snippet) to format positional data (e.g., coordinates).

## Usage

1. Import and use the component in a Vue.js application:
   ```javascript
   import DetailsModalComponent from './DetailsModalComponent.vue';
   ```
2. Pass a `detailsModal` prop with:
   - `show`: Boolean to control visibility.
   - `title`: String for the modal header.
   - `type`: String (e.g., `'building'`) to determine rendered content.
   - `data`: Object containing details (e.g., `name`, `position`, `size`).
3. Listen for `close-modal` events to handle modal closure.

## Dependencies

> `Vue.js (for reactivity and templating)`
> `likely Vuex or Pinia for state management of `detailsModal` props.`

## Related

- [[Vue]]
- [[Building Data Structure Documentation]]

>[!INFO] Dynamic Content Rendering
> The component uses `v-if` to conditionally render sections (e.g., building details). Ensure `detailsModal.data` is properly structured for all expected types (e.g., `building`, `drone`).

>[!WARNING] Missing Helper Logic
> The `formatPosition` function is referenced but not defined in the snippet. Implement it to handle coordinate formatting (e.g., converting raw coordinates to human-readable strings).

>[!WARNING] Fallback Values
> Defaults like `'Unknown'` or `'N/A'` are used for missing data. Consider logging or validating `detailsModal.data` before rendering to avoid unexpected UI behavior.
