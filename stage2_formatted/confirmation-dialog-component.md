**Tags:** #Vue, #UI-Component, #Dialog, #Confirmation, #SingleResponsibility
**Created:** 2026-01-13
**Type:** code-notes

# confirmation-dialog-component

## Summary

```
A Vue.js component for displaying a confirmation dialog with cancel/confirm actions.
```

## Details

> This component implements a reusable confirmation dialog UI using Vue.js. It renders a modal overlay with a title, message, and two buttons (Cancel and Confirm). The dialog is conditionally rendered based on the `show` prop, which defaults to `false`. The `danger` prop dynamically applies a visual style to the confirm button if set to `true`. It emits `confirm` and `cancel` events to handle user interactions.

## Key Functions

### ``template``

Renders the dialog UI with conditional logic for styling and button actions.

### ``props``

Defines configurable inputs:

### ``show``

Controls visibility (boolean).

### ``title``

Sets the dialog title (string).

### ``message``

Displays the confirmation message (string).

### ``confirmText``

Customizes the confirm button text (string).

### ``danger``

Applies a red styling class to the confirm button (boolean).

### ``emits``

Handles user events:

### ``confirm``

Emitted when the confirm button is clicked.

### ``cancel``

Emitted when the overlay or cancel button is clicked.

## Usage

```javascript
// Import and use in a Vue component:
import ConfirmationDialogComponent from './ConfirmationDialogComponent.vue';

// In a parent component:
this.$refs.dialog.show = true; // Show dialog
this.$refs.dialog.$emit('confirm'); // Handle confirmation
```

## Dependencies

> `Vue.js (for reactivity and templating).`

## Related

- [[Vue]]
- [[Single Responsibility Principle in UI Components]]

>[!INFO] Event Emission
> Users must explicitly handle `confirm`/`cancel` events in parent components to avoid memory leaks.

>[!WARNING] Overlay Click Handling
> The `@click.self` directive prevents accidental dismissals when clicking outside the dialog. Ensure parent components do not interfere with event propagation.
