**Tags:** #Vue, #CompositionAPI, #UI-Library, #Theming, #Vuetify
**Created:** 2026-01-13
**Type:** code-notes

# useVuetifyTheme

## Summary

```
Manages Vuetify theme switching via Composition API in a Vue.js application.
```

## Details

> This utility function injects the `vuetify` dependency from the Vue context and provides a method to dynamically toggle between light and dark themes. It leverages Vue’s Composition API with `inject` to access the Vuetify instance, then updates the global theme mode (`dark`/`light`) via `vuetify.theme.global.name.value`. The function returns a single method (`setVuetifyTheme`) to programmatically switch themes.

## Key Functions

### `useVuetifyTheme`

Initializes and exposes theme-switching logic via Composition API.

### `setVuetifyTheme`

Internal helper that updates the Vuetify theme mode (`isDark` flag determines theme).

## Usage

```javascript
import { useVuetifyTheme } from './useVuetifyTheme'
import { inject } from 'vue'

const vuetify = inject('vuetify')
const themeUtils = useVuetifyTheme()

// Toggle theme dynamically
themeUtils.setVuetifyTheme(true) // Dark mode
themeUtils.setVuetifyTheme(false) // Light mode
```

## Dependencies

> ``vue``
> ``vuetify``

## Related

- [[Vue Composition API Guide]]
- [[Vuetify Theme Documentation]]

>[!INFO] Dependency Check
> Ensure `vuetify` is properly injected into the component (e.g., via `<script setup>` or `provide/inject`). Without it, `setVuetifyTheme` will silently ignore calls.

>[!WARNING] Scope Limitation
> This function only affects the **global theme** (`vuetify.theme.global`). For per-component theming, use Vuetify’s `provide`/`inject` for scoped styles.
