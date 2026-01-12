**Tags:** #frontend, #drone-control-system, #ui/ux, #react-components, #navigation, #configuration-management
**Created:** 2026-01-12
**Type:** code-notes

# drones-control-page-implementation

## Summary

```
Implements a dedicated "Drones Control" page consolidating drone brand selection and configurations for improved organization and usability.
```

## Details

> This implementation refactors drone-related controls into a new `/dc/` page, replacing redundant sections from Master Controls and Config pages. The page features a two-column layout: the left column remains sticky for brand selection, while the right column dynamically adjusts for configurations and presets. Brand selection includes dropdowns for models and capabilities, while presets and configurations offer granular editing for motion, payload, communication, and squad assignments.

## Key Functions

### ``drones-control-view-component.js``

Main UI component rendering the two-column layout with brand selection and dynamic configurations.

### ``drones-control-page-component.js``

Page wrapper managing lifecycle and routing for the drones control page.

### ``url-routing-box.js``

Handles route mapping for `/dc/` endpoint.

### ``layout-navigation-box.js``

Adds a dedicated navigation item for the Drones Control page.

### ``master-controls-view-component.js``

Removed drone brand selection logic, streamlining remaining controls.

### ``drones-base-config-view-component.js``

Consolidated drone configurations, updating remaining sections (e.g., Swarm & Base Configuration).

## Usage

1. Access via `/dc/` URL.
2. Use the left column for brand/model selection and capabilities display.
3. Edit configurations in the right column via interactive cards or presets.
4. Navigate via the dedicated navigation item (🚁 icon).

## Dependencies

> `React components (e.g.`
> ``react-router-dom``
> ``react``
> ``react-dom`)`
> `frontend framework (e.g.`
> `Vue.js or similar)`
> `and UI libraries (e.g.`
> `Bootstrap`
> `Material-UI).`

## Related

- [[url-routing-box]]
- [[master-controls-view-component]]
- [[drones-control-page-component]]

>[!INFO] Sticky Brand Column
> The left column remains fixed for quick brand switching, improving efficiency for repetitive selections.

>[!WARNING] Data Migration
> Ensure existing drone configurations are migrated from Config/Master Controls before full deployment to avoid conflicts.
