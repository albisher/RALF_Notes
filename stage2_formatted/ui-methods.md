**Tags:** #UI, #notifications, #dialogs, #error-handling, #logging, #single-responsibility
**Created:** 2026-01-13
**Type:** code-notes

# ui-methods

## Summary

```
Handles UI notifications, dialogs, error logging, and confirmation prompts with dynamic durations and fallback mechanisms.
```

## Details

> `UiMethods` is a utility class managing UI interactions, including:
> - **Dynamic notifications** with auto-dismissal based on type (success/info = 3s, error/warning = 7s).
> - **Error logging** with fallback to `console.error` if a `LoggingBox` is unavailable.
> - **Confirmation dialogs** for user actions with optional cancellation and danger mode.
> - **Notification management** via `showNotification` and manual removal via `removeNotification`.
> - **Error log storage** (max 50 entries) for debugging.
> 
> The class uses `this.notifications` and `this.errorLog` arrays internally, with auto-cleanup timers and fallback logging.

## Key Functions

### ``showNotification(message, type, duration)``

Displays a temporary UI notification with auto-dismissal.

### ``logError(message, details, type)``

Logs errors to `errorLog` (with `LoggingBox` fallback) and triggers a notification.

### ``showConfirmation(title, message, onConfirm, onCancel, confirmText, danger)``

Opens a modal confirmation dialog.

### ``confirmAction()``

Executes the confirmed action and clears the dialog.

### ``removeNotification(index)``

Manually removes a notification from storage.

### ``clearErrorLog()``

Resets the error log history.

## Usage

1. **Initialize**: Attach `UiMethods` to a DOM object (e.g., `window.uiMethods = new UiMethods()`).
2. **Show Notifications**:
   ```js
   uiMethods.showNotification("Success!", "success");
   ```
3. **Log Errors**:
   ```js
   uiMethods.logError("Failed to load data", { error: "NetworkError" });
   ```
4. **Show Confirmation**:
   ```js
   uiMethods.showConfirmation(
     "Delete File?",
     "Are you sure?",
     () => { /* Confirm action */ },
     () => { /* Cancel action */ }
   );
   ```

## Dependencies

> ``window.loggingBox` (optional)`
> ``console` (fallback)`
> `DOM event handlers (for dialog rendering).`

## Related

- [[Error Handling System]]
- [[UI Component Library]]

>[!INFO] Dynamic Duration Logic
> Notification duration adjusts based on type: routine (3s) vs. critical (7s). This balances user experience and attention.

>[!WARNING] Error Log Size Limit
> The `errorLog` array caps at 50 entries to prevent memory bloat. Older entries are discarded.
