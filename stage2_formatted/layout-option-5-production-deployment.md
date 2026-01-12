**Tags:** #production-deployment, #sidebar-navigation, #layout-option-5, #frontend-development, #vue-components, #css-styles
**Created:** 2026-01-12
**Type:** code-notes

# layout-option-5

## Summary

```
Deploys a new sidebar navigation layout (Option 5) to a production frontend application.
```

## Details

> This document outlines the deployment of **Layout Option 5**, a sidebar navigation redesign for a simulation application. The update includes structural changes to `index.html`, `app.js`, and `app-component.js`, while introducing new JavaScript classes (`LayoutNavigationBox`) and Vue components (`NavSidebarComponent`). The layout replaces traditional tabs with a persistent sidebar, enhancing user navigation. New CSS (`layout5.css`) and simulation-specific components (`simulation-page-component-layout5.js`) were created to support the redesign. The deployment leverages Docker for containerized frontend serving, ensuring static files are correctly routed via Nginx.

## Key Functions

### ``LayoutNavigationBox``

Manages navigation state via an OOP class.

### ``NavSidebarComponent``

Implements the Vue-based sidebar UI for navigation.

### ``simulation-page-component-layout5``

Handles the simulation page rendering under the new layout.

### ``layout5.css``

Applies styles specific to Layout Option 5.

## Usage

To deploy, navigate to the `simulation/docker` directory and run:
```bash
docker compose up -d --build frontend
```
The frontend container serves `index.html` from `/usr/share/nginx/html/` and includes all new layout files.

## Dependencies

> `Vue.js framework`
> `Nginx`
> `Docker Compose`
> `existing frontend components (Plot3DBox`
> `Plot2DBox`
> `etc.).`

## Related

- [[frontend]]
- [[docker]]

>[!INFO] Important Note
> New files (`layout-navigation-box.js`, `nav-sidebar-component.js`, etc.) must be included in the frontend build process to ensure compatibility with the updated layout.

>[!WARNING] Caution
> Breaking changes in `app.js` and `app-component.js` may require adjustments to existing code that relies on tab-based navigation. Test thoroughly before production deployment.
