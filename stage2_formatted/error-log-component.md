**Tags:** #Vue.js, #React, #ErrorHandling, #UIComponent, #Logging
**Created:** 2026-01-13
**Type:** code-notes

# error-log-component

## Summary

```
A Vue.js component for displaying and managing error logs with toggle and clear functionality.
```

## Details

> The `ErrorLogComponent` is a Vue.js template-based component designed to render and manage error logs. It dynamically displays errors in a structured panel, showing error type, timestamp, and message. The component supports toggling visibility and clearing the log via emitted events. The `errorLog` prop is an array of error objects, each containing `type`, `timestamp`, `message`, and optional `details`. The `errorLogVisible` prop controls whether the log panel is visible by default (set to `true`).

## Key Functions

### ``formatErrorTime(timestamp)``

Converts a timestamp string into a formatted time string (e.g., `HH:MM:SS`).

### ``errorLog` prop`

Required array of error objects to display.

### ``errorLogVisible` prop`

Boolean flag to toggle visibility (defaults to `true`).

### ``@click`

$emit('clear-error-log')`**: Emits an event to clear the error log.

### ``@click`

$emit('toggle-error-log')`**: Toggles visibility of the error log panel.

## Usage

1. Import and use the component in a Vue.js application:
   ```javascript
   import ErrorLogComponent from './ErrorLogComponent.vue';
   ```
2. Pass an array of error objects as `errorLog`:
   ```html
   <ErrorLogComponent :errorLog="errors" />
   ```
3. Handle emitted events in parent components:
   ```javascript
   methods: {
       handleClear() { this.errors = []; },
       handleToggle() { this.errorLogVisible = !this.errorLogVisible; }
   },
   ```
4. Connect events:
   ```html
   <ErrorLogComponent
       :errorLog="errors"
       @clear-error-log="handleClear"
       @toggle-error-log="handleToggle"
   />
   ```

## Dependencies

> `Vue.js (for reactivity and templating)`
> `Vuex (implicitly via `v-if`/`v-for` and event emission).`

## Related

- [[Vue]]
- [[Vue]]

>[!INFO] Important Note
> The component relies on `errorLog` being an array of objects with at least `timestamp` and `message` properties. Missing `type` or `details` will default to `'Error'` or omit details, respectively.


>[!WARNING] Caution
> Avoid emitting `toggle-error-log` without a parent state to prevent unintended visibility toggles. Ensure `errorLog` is properly initialized to avoid rendering errors when empty.
