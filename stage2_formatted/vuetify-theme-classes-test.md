**Tags:** #vuetify, #theme-management, #dark-mode, #frontend-testing, #axios, #web-components
**Created:** 2026-01-13
**Type:** code-test

# vuetify-theme-classes-test

## Summary

```
Tests Vuetify theme class application for dark mode across UI cards via API and frontend checks.
```

## Details

> This script verifies Vuetify’s dark theme classes (`v-theme--dark`) are correctly applied to UI cards (e.g., `v-card`) when dark mode is enabled. It fetches a local API endpoint, logs test outcomes, and validates visual changes (e.g., background color transitions) via browser dev tools. The test relies on `uiStore.isDarkMode` to dynamically bind classes, ensuring cards respond to both Tailwind and Vuetify’s dark mode system.

## Key Functions

### ``testVuetifyThemeClasses()``

Orchestrates API calls, logs test progress, and validates dark mode application across cards.

### ``axios.get()``

Fetches the local application to confirm it loads (with HTTPS agent bypass for testing).

### ``uiStore.isDarkMode``

Conditional logic to apply `v-theme--dark` dynamically.

## Usage

1. Run via Node.js: `node vuetify-theme-classes-test.js`.
2. Expected: API loads, logs confirm dark mode fixes, and UI cards update to dark backgrounds when toggled.
3. Verify via browser dev tools (`Computed Styles`) to confirm `v-theme--dark` classes are applied.

## Dependencies

> ``axios``
> ``https` (Node.js built-in)`
> ``uiStore` (presumably a Vuex/Pinia store managing theme state).`

## Related

- [[Pinia Theme Store]]
- [[Vuetify Documentation: Theming]]
- [[Tailwind CSS Dark Mode Guide]]

>[!INFO] Important Note
> The script assumes `uiStore.isDarkMode` is accessible globally. If not, replace with a Vuex/Pinia getter or inject it via a provider.

>[!WARNING] Caution
> `rejectUnauthorized: false` disables HTTPS validation—use only in development/testing environments.
