**Tags:** #Security-Vulnerabilities, #Architecture-Failures, #XSS, #Insecure-Storage, #Input-Validation, #CSRF, #Code-Quality, #Monolithic-Codebase, #Tight-Coupling
**Created:** 2026-01-13
**Type:** code-review

# STRICT_CODE_REVIEW

## Summary

```
Critical security flaws and architectural violations in a UI-beta application, requiring immediate fixes to prevent data breaches and ensure maintainability.
```

## Details

> The codebase suffers from severe security risks, including **unprotected XSS vulnerabilities** (via `innerHTML` without sanitization) and **insecure token storage** (JWT in `localStorage` without encryption or `httpOnly` cookies). Architecturally, it violates best practices by using a **2368-line monolithic `index.html`** instead of modular components from a defined `js/boxes/` directory, leading to tight coupling and untestable components. Missing **CSRF protection**, **input validation**, and **Content Security Policy (CSP)** headers further exacerbate risks. The code also exposes sensitive data via `console.log` statements and lacks proper error handling.

## Key Functions

### ``api-client.js``

Handles authentication (hardcoded credentials, insecure token storage).

### ``index.html` (lines 1743–2010)`

Direct DOM manipulation with user-controlled data (XSS risk).

### ``cardview.html` (lines 976–1032)`

Unvalidated API response mapping to DOM elements.

### ``GenerateBox` (unused in main app)`

Defined in `js/boxes/` but never utilized.

### ``localStorage`/`console.log``

Exposes tokens and internal logic in production.

## Usage

The code is a **frontend UI** (likely a web map or dashboard) that fetches and renders data from an API. It violates separation of concerns by embedding logic in `index.html` and lacks modular components (e.g., `GenerateBox`). Security risks require sanitization, CSP headers, and secure token handling.

## Dependencies

> `- Vue.js (for reactivity)
- `zod` (for input validation`
> `if not already included)
- `sanitize-html`/`sanitize-svg` (for XSS protection)
- Backend API (for token storage/validation)`

## Related

- [[Project-Architecture-Docs]]
- [[Security-Policy]]
- [[Code-Review-Template]]

>[!INFO] **Critical Refactor Needed**
> The monolithic `index.html` (2368 lines) must be split into modular components using the `js/boxes/` directory. Replace inline logic with `GenerateBox`/`BoxInterface` for maintainability.

>[!WARNING] **XSS Risk in DOM Manipulation**
> All `innerHTML` assignments (e.g., `mapLayer.innerHTML = userData`) must use `DOMParser` + sanitization to prevent script injection. Example:
> ```javascript
> const parser = new DOMParser();
> const doc = parser.parseFromString(userData, 'image/svg+xml');
> const sanitized = sanitizeSVG(doc);
> mapLayer.innerHTML = sanitized.body.innerHTML;
> ```
