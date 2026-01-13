**Tags:** #VueJS, #UIComponent, #SessionManagement, #DropdownMenu, #Reactivity
**Created:** 2026-01-13
**Type:** code-notes

# header-component

## Summary

```
A Vue.js header component managing session selection with dropdown functionality and status display.
```

## Details

> This component renders an application header displaying the station name and a session dropdown menu. It uses Vue’s reactivity to toggle a dropdown menu when clicked, filtering sessions based on a search query. The dropdown includes a refresh button to reload sessions and visually distinguishes active sessions (green) from inactive ones (gray). Session selection is triggered via the dropdown menu.

## Key Functions

### ``showSessionDropdown``

Toggles visibility of the session dropdown menu.

### ``status.sessionId``

Tracks the currently selected session ID (active/inactive state).

### ``filteredSessions``

Stores filtered sessions based on search input.

### ``sessionSearchQuery``

Handles user input for session filtering.

### ``@click` handlers`

Trigger dropdown toggle and session selection logic.

## Usage

1. Import and use the component in a Vue template:
   ```html
   <HeaderComponent @load-sessions="refreshSessions" />
   ```
2. Provide `status` and `filteredSessions` via props or Vuex store.
3. Handle session selection via dropdown events.

## Dependencies

> `Vue.js (for reactivity and event handling)`
> `Vuex (likely for state management of `status` and `filteredSessions`).`

## Related

- [[Vue]]
- [[Session Management Pattern]]

>[!INFO] Reactive State Management
> Ensure `status.sessionId` and `filteredSessions` are properly synchronized with Vuex or props to avoid stale data.

>[!WARNING] Dropdown Positioning
> The dropdown’s `position: absolute` relies on parent container positioning; ensure parent has `position: relative` to avoid layout issues.
