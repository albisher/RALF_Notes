**Tags:** #Vue-component, #React-component, #UI-layout, #Navigation, #Simulation-app, #Sidebar
**Created:** 2026-01-13
**Type:** code-notes

# app-component

## Summary

```
Manages application layout with sidebar navigation for a simulation application.
```

## Details

> This component (`MainAppComponent`) defines a Vue/React-like layout for a simulation application using a sidebar navigation pattern. It encapsulates the application state management and integrates a header component with simulation controls and a sidebar navigation component. The template includes two main sections: a header with simulation controls and a sidebar with navigation items and drone management. The sidebar handles view changes and drone commands, while the header manages session and replay functionalities.

## Key Functions

### ``handleViewChange``

Triggers view navigation based on sidebar selections.

### ``startSimulation`/`pauseSimulation`/`resetSimulation``

Manages simulation lifecycle events.

### ``sendCommandFromForm``

Processes drone commands via the command form.

### ``handleQuickSpawn`/`handleNewSession``

Quick actions for drone spawning and session creation.

### ``loadSessions`/`selectSession``

Handles session loading and selection.

### ``onReplayTimeUpdate`/`onUpdateGpsPosition``

Updates replay controls and GPS data.

## Usage

1. Import and render `MainAppComponent` in the root of your application.
2. Bind state properties (`navItems`, `currentView`, `status`, etc.) to parent state management.
3. Connect event handlers (`@nav-change`, `@start-simulation`, etc.) to handle UI interactions.

## Dependencies

> ``<header-component>``
> ``<nav-sidebar-component>``
> ``<simulation-page-component-layout5>``
> `Vue/React core libraries (e.g.`
> `Vuex for state management if applicable).`

## Related

- [[React state management system]]
- [[Header Component Documentation]]
- [[Sidebar Navigation Component]]
- [[Simulation Page Component]]

>[!INFO] **Single Responsibility**
> This component manages layout and state but delegates UI rendering to child components. Avoid overloading it with logic—keep navigation and simulation controls separate.

>[!WARNING] **State Management**
> Ensure parent components inject required state (e.g., `sessions`, `drones`) via props or context. Missing props may cause rendering errors.
