**Tags:** #Vue.js, #Pinia, #UI State Management, #Dark Mode, #Modals, #Notifications, #Local Storage, #Tailwind CSS
**Created:** 2026-01-13
**Type:** documentation

# ui

## Summary

```
Manages UI state, including sidebar visibility, dark mode, modal handling, and notifications for a Vue.js application.
```

## Details

> This Pinia store handles core UI state and functionality such as toggling a collapsible sidebar, managing dark mode preferences (with persistence via `localStorage`), displaying modals, and showing notifications (success, error, info, warning). It uses Vue’s `ref` and `computed` for reactivity and integrates Tailwind CSS for dark mode styling. The store initializes dark mode preferences from `localStorage` or the system preference.

## Key Functions

### ``toggleSidebar()``

Toggles the sidebar visibility state.

### ``toggleDarkMode()``

Toggles dark mode and applies Tailwind’s `dark` class, saving the preference to `localStorage`.

### ``setDarkMode(dark)``

Explicitly sets dark mode state and applies Tailwind’s class, persisting the choice.

### ``openModal(modalName, modalData)``

Opens a modal with a given name and data.

### ``closeModal()``

Resets `currentModal` to `null`, closing any open modal.

### ``addNotification(notification)``

Adds a new notification (auto-dismissing after a duration).

### ``dismissNotification(id)``

Marks a notification as dismissed and removes it after a short delay.

### ``clearNotifications()``

Clears all active notifications.

### ``showSuccess(message, title)``

Convenience method to add a success notification.

### ``showError(message, title)``

Convenience method to add an error notification.

### ``showInfo(message, title)``

Convenience method to add an info notification.

### ``showWarning(message, title)``

Convenience method to add a warning notification.

### ``initDarkMode()``

Loads saved dark mode preference from `localStorage` or defaults to system preference.

## Usage

1. **Import and use the store**:
   ```javascript
   import { useUIStore } from '@/stores/ui'
   const uiStore = useUIStore()
   ```
2. **Toggle sidebar**:
   ```javascript
   uiStore.toggleSidebar()
   ```
3. **Toggle dark mode**:
   ```javascript
   uiStore.toggleDarkMode()
   ```
4. **Open a modal**:
   ```javascript
   uiStore.openModal('loginModal', { email: 'user@example.com' })
   ```
5. **Show notifications**:
   ```javascript
   uiStore.showSuccess('Task completed!')
   uiStore.showError('Failed to save data')
   ```
6. **Initialize preferences**:
   Call `initDarkMode()` in `App.vue` or `main.js` to load saved settings.

## Dependencies

> ``pinia``
> ``vue``
> ``localStorage` (built-in browser API)`
> ``Tailwind CSS` (for dark mode styling).`

## Related

- [[Vue Pinia Guide]]
- [[Vue]]
- [[Tailwind CSS Dark Mode]]

>[!INFO] Important Note
> The `darkMode` state is persisted to `localStorage` and applied via Tailwind’s `dark` class. Ensure your app’s root element has the `dark` class when dark mode is active.
>

>[!WARNING] Caution
> Auto-dismissed notifications (e.g., `addNotification`) rely on `setTimeout`. If the app crashes or loses focus, notifications may not dismiss as expected. Consider adding a cleanup mechanism for pending timers.
