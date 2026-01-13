**Tags:** #Vue, #mixin, #UI, #utility, #notifications, #dialogs, #modal
**Created:** 2026-01-13
**Type:** code-notes

# UIUtilsMixin

## Summary

```
Provides Vue component utility mixin for notifications, dialogs, and modals.
```

## Details

> This mixin centralizes UI utility functionality in Vue components, enabling reusable notification systems (with auto-dismissal), confirmation dialogs, and a safe modal state management. It follows the single responsibility principle by handling only UI-related interactions. The `safeDetailsModal` computed property ensures modal state defaults to a safe fallback when undefined.

## Key Functions

### `showNotification`

Displays a temporary notification with customizable type and duration.

### `removeNotification`

Removes a specific notification by ID.

### `clearNotifications`

Clears all notifications from the component.

### `showConfirmation`

Opens a confirmation dialog with customizable text and callbacks.

### `confirmAction`

Executes the confirmation callback and closes the dialog.

### `safeDetailsModal`

Computed property ensuring modal state defaults to `{ show: false }` if undefined.

## Usage

```javascript
// In a Vue component:
export default {
  mixins: [UIUtilsMixin],
  methods: {
    handleConfirm() {
      this.showConfirmation('Delete Item?', 'Are you sure?', () => {
        this.deleteItem();
      });
    },
    showExampleNotification() {
      this.showNotification('Success!', 'success', 2000);
    }
  }
};
```

## Dependencies

> `Vue.js (for reactivity and event emission)`

## Related

- [[Vue]]
- [[Vue Notifications Pattern]]

>[!INFO] Important Note
> This mixin relies on Vue's reactivity system. Ensure the component emits `'notification-shown'` events for dynamic UI updates.

>[!WARNING] Caution
> Auto-dismissal (`duration`) may cause race conditions if the component unmounts before the timeout completes. Use `duration = 0` for permanent notifications.
