**Tags:** #browser-testing, #ui-visibility, #frontend-validation, #simulation-ui, #plotly-visualization
**Created:** 2026-01-12
**Type:** documentation

# ui-visible-vs-working-checklist

## Summary

```
A checklist comparing UI elements that are visually present versus those that function correctly in a browser-based simulation application.
```

## Details

> This document outlines a structured comparison of UI elements in a web-based simulation dashboard, distinguishing between what users can *see* (based on rendered HTML/CSS) and what *actually works* (API responses, backend logic, and interactive functionality). The checklist is divided into sections like Header, Navigation Tabs, and Simulation View, with subcomponents (e.g., Left Sidebar, Logs) to ensure comprehensive validation. It uses browser tools, API testing, and code inspection to validate both visual and functional aspects of the UI.

## Key Functions

### `Header Section`

Displays title, session controls, and replay buttons.

### `Main Navigation Tabs`

Active tab highlighting via styling.

### `Simulation View Page (Left Sidebar)`

- **Quick Actions**: Start/Pause/Stop buttons.

### `Spawn Drone Section`

Drone positioning and command inputs.

### `Command Section`

Drone command execution logic.

### `Buildings Section`

Building management (spawn/delete/save).

### `Simulation View Page (Right Sidebar)`

- **Communication Logs**: Real-time log filtering and refresh.

### `Master Controls Page`

- **GPS & Location**: Dynamic map integration and location inputs.

### `Time Restrictions`

Time-based simulation controls.

## Usage

This checklist is used during browser testing to validate UI consistency between design specs and actual implementation. Testers compare rendered UI elements against functional endpoints (e.g., session creation, command execution) to ensure seamless user experience.

## Dependencies

> `Plotly.js (for 3D/2D visualization)`
> `Docker (for backend environment)`
> `browser tools (Chrome DevTools)`
> `API testing frameworks (e.g.`
> `Postman)`
> `backend services (simulation logic).`

## Related

- [[ui-design-specs]]
- [[backend-api-endpoints]]
- [[simulation-dashboard-architecture]]

>[!INFO] Important Note
> **Visual vs. Functional Discrepancies**: The checklist explicitly separates UI visibility (e.g., dropdown menus) from backend/API functionality (e.g., session creation). Missing a "✅" in a section may indicate a bug in rendering or logic, requiring debugging in both frontend and backend layers.


>[!WARNING] Caution
> **Dynamic Content**: Elements like the 3D/2D plots or logs rely on JavaScript/Plotly.js. If these fail to render, verify:
> - Plotly.js is loaded and initialized.
> - Backend provides real-time data (e.g., session logs).
> - No CSS/JS errors block rendering (e.g., `console.log` for errors).
