**Tags:** #folder-structure, #architecture, #vuejs, #box-pattern, #css-organization, #deprecation
**Created:** 2026-01-13
**Type:** documentation

# FOLDER_STRUCTURE_CONVENTION

## Summary

```
Defines a standardized folder structure and conventions for the `ui-beta` Vue.js application, enforcing modular design with the Box pattern and CSS organization.
```

## Details

> This document outlines a strict folder structure for the `ui-beta` application, ensuring consistency across developers. It mandates the use of the Box pattern for business logic, separating concerns into boxes, components, and pages. CSS files must reside exclusively in `/src/styles/` to avoid duplication, with deprecated root-level styles removed post-migration. The structure emphasizes modularity, reusability, and adherence to Vue.js best practices.

## Key Functions

### `BoxOrchestrator`

Orchestrates execution of Box pattern implementations.

### `BoxInterface/BoxInput/BoxOutput`

Base classes defining the Box pattern contract.

### `api-client.js`

Abstracts API communication for service layer.

### `color-scheme.css`

Centralized CSS variables for theming.

### `common.css`

Shared styles for reusable UI elements.

## Usage

1. Developers must place all business logic in `/src/boxes/` following the Box pattern.
2. Vue components must use `BoxOrchestrator` to execute boxes, avoiding direct API calls.
3. CSS files must be imported from `/src/styles/` using relative paths.
4. Deprecated `/styles/` directory must be cleaned up during migration.

## Dependencies

> `Vue.js`
> `JSDoc`
> `CSS modules`
> `Webpack (or similar bundler)`
> `Node.js (for utility scripts).`

## Related

- [[FolderStructureMigrationGuide]]
- [[VueComponentBestPractices]]

>[!INFO] Box Pattern Enforcement
> All business logic must be encapsulated in Box classes. Components delegate execution to `BoxOrchestrator`, ensuring separation of concerns.

>[!WARNING] CSS Migration Risk
> Ignoring the `/src/styles/` requirement risks duplicate styles and breaking builds. Enforce this rule strictly during development.

>[!INFO] Deprecated Files Warning
> Files in `/styles/` are deprecated. Remove them immediately to avoid conflicts during refactoring.

>[!WARNING] Component Scope
> Components should be small and focused. Overly complex components may violate single-responsibility principles, leading to maintainability issues.
