**Tags:** #vuejs, #hierarchical-navigation, #sidebar-component, #asset-management, #character-robot-system, #reactive-ui, #vue-router, #api-integration, #ui-transitions, #mobile-friendly
**Created:** 2026-01-13
**Type:** documentation

# hierarchical_sidebar_implementation

## Summary

```
Implements a Vue.js hierarchical sidebar navigation system for managing assets with expandable submenus, specialized components for character/robot management, and API-driven asset operations.
```

## Details

> This implementation creates a modular, Vue.js-based hierarchical sidebar (`App.vue`) with expandable "Assets" submenu items (World, Plant, Building, Character, Robot). The system uses Vue Router for nested routing and maintains reactive state for smooth UI transitions. Key components include `AssetsLayout.vue` for secondary asset navigation and asset-specific components like `BuildingAssets.vue` and `CharacterAssets.vue`, which handle specialized logic for character personality/behavior and robot physical embodiment. The architecture supports automatic robot body creation when a robot character is created, linking mental/behavioral data to physical assets via API calls.

## Key Functions

### ``App.vue``

Main sidebar with expandable Assets menu and submenu items.

### ``AssetsLayout.vue``

Secondary sidebar for asset type navigation with nested routes.

### ``BuildingAssets.vue``

Building-focused asset management (type selection, creation, grid display).

### ``CharacterAssets.vue``

Character personality/behavior management with 18 predefined traits and robot body auto-generation.

### ``WorldAssets.vue``

Generic asset management reused across asset types.

### ``routerStructure``

Hierarchical Vue Router setup for nested asset routes.

### ``loadBuildingAssets``

API call to fetch and filter building assets.

### ``createBuilding`/`createRobotBody``

API functions for creating new assets with linked data.

## Usage

1. **Initialize**: Set up Vue Router with the provided route structure.
2. **Render Sidebar**: Include `App.vue` in your main layout.
3. **Access Assets**: Navigate via the expandable Assets menu to specific asset types (e.g., `/assets/character`).
4. **Create Assets**: Use the asset-specific components (e.g., `CharacterAssets.vue`) to create or edit assets.
5. **API Integration**: Call `apiService` methods (e.g., `generateElement`) to interact with the backend.

## Dependencies

> ``vue-router``
> ``vue``
> ``v-icon` (from Vuetify)`
> ``apiService` (custom backend API wrapper)`
> ``vuetify` (UI components).`

## Related

- [[Hierarchical Navigation Patterns]]
- [[Vue]]
- [[Character-Robot Data Model]]
- [[Backend API Specifications]]

>[!INFO] **Reactive State Management**
> The `assetsMenuOpen` state variable controls the expand/collapse animation of the Assets submenu. Ensure it is properly managed to avoid stale state during transitions.


>[!WARNING] **API Error Handling**
> The `loadBuildingAssets` and `createBuilding` functions include basic error handling, but critical API failures (e.g., network issues) should be caught at a higher level to prevent UI crashes. Consider adding retry logic for transient errors.


>[!INFO] **Robot Body Auto-Generation**
> The automatic robot body creation logic assumes the `apiService` supports linked data. Verify the backend API can handle nested asset creation with character references before deploying.
