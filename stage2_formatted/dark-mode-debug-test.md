**Tags:** #dark-mode, #debugging, #frontend, #axios, #vue/vuetify
**Created:** 2026-01-13
**Type:** code-notes

# dark-mode-debug-test

## Summary

```
Debugs dark mode functionality in a web application by checking for UI elements and structural indicators.
```

## Details

> This script uses `axios` to fetch the application’s HTML response from a local server (`localhost:8443`) and performs string-based checks for dark mode indicators. It logs whether UI store references, dark mode toggle buttons (e.g., weather icons), CSS dark mode classes, and Vuetify components exist. The script also provides manual debugging steps and expected locations for the dark mode toggle. Error handling is included for API failures.

## Key Functions

### ``debugDarkMode()``

Orchestrates the dark mode validation by fetching HTML and checking for key indicators.

### ``axios.get()``

Fetches the application’s HTML response with a relaxed HTTPS certificate validation.

## Usage

1. Run the script in a Node.js environment.
2. It logs findings about dark mode elements and suggests manual debugging steps.
3. Expected to be used in a development environment to verify dark mode functionality.

## Dependencies

> ``axios``
> ``node:https` (for `httpsAgent`)`

## Related

- [[none]]

>[!INFO] Important Note
> The script uses `rejectUnauthorized: false` for local HTTPS testing, which may not be secure for production. Use a valid certificate in production.

>[!WARNING] Caution
> String-based checks (`html.includes()`) are not foolproof. For precise debugging, inspect the DOM directly in browser DevTools.
