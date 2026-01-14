**Tags:** #CSS-variables, #Theme-system, #UI-design, #Color-hierarchy, #Accessibility, #Light-theme
**Created:** 2026-01-13
**Type:** documentation

# THEME_SYSTEM

## Summary

```
A unified CSS variable-based theme system for the Space Pearl application, defining color palettes, usage patterns, and design principles for consistent UI styling.
```

## Details

> The **Space Pearl Theme System** employs a CSS variables-driven approach to maintain visual consistency across all UI components. It organizes colors into structured categories—**Primary Theme Colors, Backgrounds, Text, Borders, Semantic Indicators, and Stage Accents**—each with predefined variables for reusable styling. The system prioritizes **Sky Blue (#87CEEB)** as the primary brand color while ensuring semantic distinction through subtle stage accents and status indicators. Design principles emphasize **consistency, light theme focus, and accessibility**, with migration guidance for replacing hardcoded colors.

## Key Functions

### `Color Hierarchy Definition`

Maps CSS variables to color roles (e.g., `--primary`, `--success`).

### `Usage Patterns`

Documents how colors apply to buttons, cards, borders, and text.

### `Design Principles`

Outlines consistency, stage differentiation, and theme focus rules.

### `Migration Guide`

Provides step-by-step replacements for legacy color codes.

### `Future Improvements`

Lists potential enhancements (e.g., dark mode, spacing variables).

## Usage

1. **Apply Variables**: Replace hardcoded colors with CSS variables (e.g., `background: var(--primary)`).
2. **Follow Patterns**: Use predefined patterns for buttons, cards, and text (e.g., `border: 1px solid var(--border-color)`).
3. **Adhere to Principles**: Maintain visual hierarchy and consistency across components.

## Dependencies

> `CSS variables (e.g.`
> ``var(--primary)`)`
> `external CSS modules (`enhanced-forms.css``
> ``common.css`).`

## Related

- [[Space Pearl CSS Variables Reference]]
- [[Space Pearl Design System Overview]]

>[!INFO] **CSS Variables Mandatory**
> All UI elements must use the theme’s CSS variables (e.g., `--bg-primary`) to ensure consistency. Avoid hardcoding colors to prevent visual drift.

>[!WARNING] **Stage Accents Subtle**
> Stage accents (e.g., `--stage-timeline-accent`) should be used sparingly—only for borders or hints, not backgrounds. Overuse risks visual clutter.
