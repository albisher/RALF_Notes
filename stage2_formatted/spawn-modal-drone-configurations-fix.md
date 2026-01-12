**Tags:** #vue, #javascript, #drone-configuration, #frontend, #reactivity, #api-integration, #modal-ui
**Created:** 2026-01-12
**Type:** code-notes

# app-data.js

## Summary

```
Fixes drone configuration loading for the spawn modal to ensure drone configurations are available immediately upon app startup.
```

## Details

> The `app-data.js` file contains logic for managing drone configurations. The issue was that the `droneConfigurations` array was initialized as empty and only loaded when navigating to the Config page, causing the spawn modal to display a message indicating no configurations were found. The fix involved adding a `loadDroneConfigurations()` call in the `mounted()` hook to load configurations silently at app startup, ensuring the data is available when the spawn modal opens.

## Key Functions

### `loadDroneConfigurations(silent)`

Loads drone configurations from the API with an optional `silent` parameter to suppress notifications.

### `mounted()`

Vue lifecycle hook that triggers configuration loading on app initialization.

## Usage

To use this fix, ensure the `loadDroneConfigurations(true)` is called in the `mounted()` hook of `app-data.js`. The configurations are loaded silently, and the `droneConfigurations` array is populated immediately, allowing the spawn modal to display available drones.

## Dependencies

> ``simulation/frontend/app.js``
> ``simulation/frontend/app-layout5.js``
> ``/api/drone-configurations``
> ``/app/data/drone_configs/drone_configurations.json``

## Related

- [[app]]
- [[app-layout5]]

>[!INFO] Silent Mode
> The `silent` parameter in `loadDroneConfigurations()` ensures no notifications are displayed during startup loading, making the process seamless for the user.

>[!WARNING] Reactivity Check
> Ensure Vue’s reactivity system properly updates the `droneConfigurations` prop in the parent components (`app.js` and `app-layout5.js`) after loading to avoid stale data in the modal. Verify the `mounted()` hook execution and prop binding in the browser console.
