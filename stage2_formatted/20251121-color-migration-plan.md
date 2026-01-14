**Tags:** #color-standardization, #UI-migration, #CSS-variables, #WCAG-compliance, #Vue-components, #Design-system
**Created:** 2026-01-13
**Type:** documentation

# 20251121-color-migration-plan

## Summary

```
Standardizes inconsistent color schemes across 8 UI pages using CSS variables for UI/UX consistency and accessibility.
```

## Details

> This document outlines a phased migration plan to replace hardcoded hex colors with CSS variables in a Vue-based UI system. The goal is to enforce a unified color system while preserving semantic distinctions for content types (e.g., characters, locations). The plan addresses contrast issues, timeline inconsistencies, and sidebar active states, ensuring compliance with WCAG accessibility standards.

## Key Functions

### ``color-scheme.css``

Defines foundational CSS variables for colors, gradients, and contrast ratios.

### ``GenerateStage.vue``

Contains hardcoded purple colors that need replacement with CSS variables for consistency.

### ``TimelineStage.vue``

Uses inconsistent blue shades; standardizes with a timeline-specific gradient (`--bg-timeline`).

### ``WorldStage.vue``

Replaces green hardcoded colors with `--location` variable for content-specific elements.

### ``SidebarNavigation.vue``

Requires unified active state styling via `--sidebar-active-bg`, `--sidebar-active-color`.

### ``CSS Variables Migration Script``

Automates replacement of legacy hex codes with CSS variables (e.g., `#9c27b0` → `var(--robot)`).

## Usage

1. **Phase 1**: Add new CSS variables to `color-scheme.css` (e.g., `--stage-generate-accent`, `--button-primary`).
2. **Phase 2**: Audit Vue components (e.g., `GenerateStage.vue`) for hardcoded colors and replace them with CSS variables.
3. **Phase 3**: Test contrast ratios using tools like Axe DevTools to ensure compliance.
4. **Phase 4**: Deploy changes incrementally across pages (e.g., TimelineStage first, then shared components).

## Dependencies

> `Vue.js (3.x)`
> `SCSS/Vue-style CSS preprocessors`
> `CSS variables (native or via libraries like `css-vars-pony`)`
> `WCAG contrast-checking tools (e.g.`
> `Axe DevTools).`

## Related

- [[Color Theory Cheat Sheet]]
- [[WCAG 2]]
- [[Vue CSS Variables Guide]]

>[!INFO] **Critical Contrast Check**
> Before deploying any changes, verify all text elements meet WCAG AA contrast ratios (minimum 4.5:1). Use tools like [Axe DevTools](https://www.deque.com/axe/) to automate checks.


>[!WARNING] **Partial Rollout Risk**
> Replacing hardcoded colors in shared components (e.g., `SidebarNavigation`) without testing may break UI consistency. Test in a staging environment first.


>[!INFO] **Timeline Consistency**
> The timeline’s orange (`--event`) color is already correctly used; avoid over-standardizing it unless semantic clarity is compromised.
