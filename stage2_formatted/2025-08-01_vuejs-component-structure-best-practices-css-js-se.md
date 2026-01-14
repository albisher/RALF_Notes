**Tags:** #VueJS, #ComponentStructure, #CSSSeparation, #JSSeparation, #BestPractices, #SingleFileComponents, #TemplateOrganization, #PiniaStateManagement, #3DGlobeIntegration, #VuetifyCSS, #TailwindCSS
**Created:** 2026-01-13
**Type:** documentation

# 2025-08-01_vuejs-component-structure-best-practices-css-js-se

## Summary

```
Best practices for organizing Vue.js components, separating CSS/JS, and structuring templates, tailored for projects using Vuetify, Tailwind CSS, and complex components like a 3D globe.
```

## Details

> This document outlines structured best practices for organizing Vue.js components, emphasizing separation of concerns between **template, script, and style** sections. It recommends a **feature-based folder structure** (e.g., `src/components/globe/`) to group related components, ensuring modularity and maintainability. For **CSS/JS separation**, it advocates using `<style scoped>` for component-specific styles, leveraging Tailwind utilities for utility-first design, and externalizing complex logic (e.g., 3D globe rendering) into dedicated modules. The template should remain declarative, with logic moved to `<script setup>` or computed properties. **Vuetify** and **Tailwind CSS** integration is optimized by prioritizing Vuetify for UI components and Tailwind for layout, while avoiding style conflicts through scoped styles and utility-first design.

## Key Functions

### `Feature-based folder structure`

Groups components by domain (e.g., `globe/`, `auth/`).

### ``<script setup>` syntax`

Enables concise, performant component logic handling lifecycle hooks (`onMounted`, `onUnmounted`).

### `Scoped styles (`<style scoped>`)`

Encapsulates component-specific CSS to prevent global leaks.

### `Pinia integration`

Manages centralized state for complex components (e.g., globe mode).

### `Dynamic components (`<component`

is>`)**: Allows flexible rendering of components (e.g., mode switches).

### `Slot-based content distribution`

Enables reusable, modular content insertion (e.g., alerts, modals).

### `External JS modules`

Isolates complex logic (e.g., `app/globe.js`) for the 3D globe, improving maintainability.

## Usage

1. **Organize components** by feature (e.g., `src/components/globe/` for 3D globe logic).
2. **Use `<script setup>`** for component logic, externalizing heavy logic (e.g., globe rendering) to modules.
3. **Apply scoped styles** (`<style scoped>`) for component-specific CSS, and use Tailwind utilities for layout.
4. **Leverage slots** for flexible content distribution (e.g., modals, alerts).
5. **Integrate Pinia** for state management, especially for dynamic components like the globe.
6. **Combine Vuetify and Tailwind**—use Vuetify for UI components, Tailwind for utility classes.

## Dependencies

> `Vue 3`
> `Pinia`
> `Vuetify`
> `Tailwind CSS`
> `Three.js (for 3D globe)`
> `WebGL (for rendering).`

## Related

- [[Vue 3 Component Best Practices Guide]]
- [[Pinia State Management Docs]]
- [[Tailwind CSS Documentation]]
- [[Vuetify Component Reference]]

>[!INFO] **Avoid Deep Nesting**
> Deeply nested folders (e.g., `src/components/globe/controls/`) reduce readability and maintainability. Keep components at one or two levels deep within feature folders.

>[!WARNING] **Inline Styles Risk**
> Inline styles (e.g., `<div style="color: red;">`) can break maintainability. Prefer scoped styles or utility classes (Tailwind/Vuetify) unless dynamically bound via `:style`.

>[!INFO] **Slot Conflicts**
> Overuse of slots can lead to unintended content rendering. Use slots sparingly for modular, reusable components (e.g., modals, alerts).

>[!WARNING] **Global CSS Pollution**
> Avoid global styles in `<style scoped>` blocks. Use a dedicated `global.css` file for resets, typography, or overrides.

>[!INFO] **Three.js/GL Integration**
> For 3D components (e.g., globe), externalize WebGL/Three.js logic to modules (e.g., `app/globe.js`) and manage lifecycle hooks (`onMounted`, `onUnmounted`) to avoid memory leaks.
