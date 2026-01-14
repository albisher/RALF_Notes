**Tags:** #VueJS, #ContentSecurityPolicy, #DevelopmentMode, #HotModuleReplacement, #CSPAlternatives, #EvalSecurity, #ViteBuildTool, #TemplateCompilation, #SecurityBestPractices
**Created:** 2026-01-13
**Type:** research-notes

# 2025-08-02_vuejs-development-mode-eval-csp-alternatives-2025

## Summary

```
Explores Vue.js 2025 alternatives to `eval()` in development mode to comply with Content Security Policies (CSP) while maintaining functionality.
```

## Details

> This document examines how Vue.js leverages `eval()` in development mode for features like dynamic template compilation, HMR, and debugging. It highlights CSP conflicts with `eval()` and provides 2025-compliant alternatives, including pre-compiling templates, using Vite’s CSP-friendly build system, and configuring CSP with nonces. The focus is on balancing security with developer experience in Vue 3 projects.

## Key Functions

### `Dynamic Template Compilation`

Runtime evaluation of templates (avoid in CSP environments).

### `Hot Module Replacement (HMR)`

Real-time code updates (replaced with Vite’s native ES modules).

### `Source Maps`

Debugging with original source code (enabled via modern build tools).

### `CSP Nonce Hashing`

Secure inline script execution (temporary workaround).

### `Pre-compiled Template Builds`

Static template rendering (production best practice).

## Usage

1. **For Development**: Use Vite’s native HMR and pre-compile templates during build.
2. **For Production**: Deploy a runtime-only Vue build with pre-compiled templates and strict CSP headers.
3. **Debugging**: Rely on Vue Devtools and source maps instead of runtime `eval()`.

## Dependencies

> `Vue.js 3`
> `Vite`
> `Vue Devtools`
> `Nginx (for CSP headers)`
> `modern build tools (e.g.`
> `Webpack/Vite plugins).`

## Related

- [[Vue]]
- [[Vite Configuration Guide]]
- [[Content Security Policy Best Practices 2025]]
- [[Vue]]

>[!INFO] **Pre-compilation is Mandatory**
> In CSP environments, **never** use runtime template compilation with `eval()`. Pre-compile templates during build (e.g., via `vue-cli` or Vite) to avoid CSP violations.
>

>[!WARNING] **CSP Nonces Are Temporary**
> Using CSP nonces for inline scripts (e.g., `unsafe-inline`) is a security risk. Prefer static template compilation or Vite’s CSP-compliant HMR for long-term solutions.
