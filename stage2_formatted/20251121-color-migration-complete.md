**Tags:** #color-standardization, #css-variables, #ui-design, #accessibility, #migration, #frontend-development
**Created:** 2026-01-13
**Type:** documentation

# 20251121-color-migration-complete

## Summary

```
Documentation for a complete color standardization migration project, replacing hardcoded colors with centralized CSS variables across UI components.
```

## Details

> This migration project standardized all UI colors by replacing hardcoded values with CSS variables from a centralized `color-scheme.css` file. The process involved 7 stage components, 4 shared components, and 3 CSS files, replacing over 100 color instances. The implementation focused on semantic color usage (e.g., stage accents by entity type) and accessibility compliance (WCAG AA contrast ratios).

## Key Functions

### `GenerateStage.vue`

Primary stage component using unified button and text colors.

### `TimelineStage.vue`

Event-based UI with consistent hover/focus states.

### `SidebarNavigation.vue`

Active state and gradient background standardized.

### `WorkflowPage.vue`

SVG map colors preserved as hex values (non-CSS-variable-compatible).

### `color-scheme.css`

Centralized CSS variables for all color definitions.

### `ToastNotification.vue`

Semantic color variables for notification types (success/error/warning/info).

## Usage

1. **Apply**: Replace hardcoded colors in components with CSS variables (e.g., `--button-primary`).
2. **Test**: Verify consistency across all 8 pages (7 stages + workflow) using browser dev tools.
3. **Extend**: Use the centralized `color-scheme.css` for future theming (light/dark mode).

## Dependencies

> ``ui-beta``
> `Vue.js`
> `CSS modules`
> `browser dev tools (for contrast testing)`
> `and potentially a configuration object for SVG map colors.`

## Related

- [[20251121-color-scheme-design]]
- [[20251121-accessibility-guidelines]]
- [[20251121-ui-component-docs]]

>[!INFO] SVG Limitation
> SVG attributes (e.g., `fill="#1a4d7a"`) cannot use CSS variables directly. These colors are preserved as hex values for compatibility. Consider extracting them to a JavaScript config object referencing CSS variables via `getComputedStyle()` for dynamic updates.

>[!WARNING] Special Cases
> Hardcoded gold (`#ffd700`) for key years is intentionally retained as a semantic design choice. Override with caution to avoid visual disruptions.
