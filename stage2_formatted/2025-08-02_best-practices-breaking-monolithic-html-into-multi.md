**Tags:** #modularization, #vuejs, #web-components, #monolithic-code, #3d-visualization, #2d-map-integration, #encapsulation, #reusability, #design-patterns
**Created:** 2026-01-13
**Type:** research-notes

# 2025-08-02_best-practices-breaking-monolithic-html-into-multi

## Summary

```
Explores 2025 best practices for splitting monolithic HTML into modular Vue components for 3D globe and 2D map visualizations.
```

## Details

> The document outlines modern approaches to modularizing monolithic HTML files by breaking them into reusable Vue components (`GlobeView.vue`, `MapView.vue`). Key principles include encapsulation via Shadow DOM (or Vue’s component system), small, focused components, clear APIs via props/events, and separation of markup logic. The context applies to wrapping existing JavaScript visualizations (`app/globe.js`, `app/map.js`) into Vue components, emphasizing reusability, maintainability, and dynamic data handling.

## Key Functions

### ``GlobeView.vue``

Renders and manages a 3D globe visualization (Three.js), accepting dynamic props (e.g., biome settings) and emitting user interaction events.

### ``MapView.vue``

Handles a 2D map (D3.js), using Vue’s reactivity to update dynamically via props and subcomponents for controls/tooltips.

### ``Vue Template Separation``

Uses `<template>` tags or Vue’s single-file component structure to isolate complex HTML markup from JavaScript logic.

### ``Design Tokens/CSS Variables``

Centralizes styling (e.g., biome colors, spacing) for consistency across components.

### ``Reusable Utility Modules``

Encapsulates shared logic (e.g., coordinate transformations) to avoid duplication.

## Usage

1. **Component Creation**: Wrap existing JS visualizations in Vue components (e.g., `GlobeView.vue` for `app/globe.js`).
2. **Data Flow**: Pass dynamic data via props (e.g., biome extrusion height) and emit events for interactivity.
3. **Template Management**: Separate static HTML into Vue templates or HTML `<template>` tags.
4. **Styling**: Apply design tokens/CSS variables for consistent theming.
5. **Fallbacks**: Implement polyfills for legacy browser support if needed.

## Dependencies

> `Vue.js`
> `Three.js (for globe)`
> `D3.js (for map)`
> `Web Components (if using native standards)`
> `CSS custom properties.`

## Related

- [[Vue]]
- [[Web Components Guide 2025]]
- [[Modular Web Development Patterns]]

>[!INFO] **Encapsulation Priority**
> Encapsulating globe/map logic in Vue components ensures isolation from parent app code, reducing conflicts and improving maintainability. Shadow DOM (or Vue’s internal rendering) prevents unintended side effects from global styles or scripts.

>[!WARNING] **Avoid Over-Componentization**
> Splitting into too many tiny components can increase complexity. Balance modularity with focus—e.g., group related controls (e.g., legends, zoom tools) into subcomponents of `MapView.vue` rather than creating separate files.
