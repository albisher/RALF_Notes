**Tags:** #backend-integration, #api-design, #box-pattern, #database-management, #ui-backend-coordination
**Created:** 2026-01-13
**Type:** architecture

# plan.plan

## Summary

```
Plans for integrating a production UI backend system using a box-based architecture for database operations and API endpoints.
```

## Details

> This document outlines a comprehensive integration plan for a UI-backend system, focusing on completing missing components like API boxes, storage boxes, and an API client module. The architecture employs a box-based pattern for modular database operations (CRUD) and API endpoints, ensuring maintainability and scalability. The backend uses existing database models (e.g., `Card`, `Timeline`, `TimelineEvent`) with relationships managed via storage boxes (e.g., `TimelineUpdateBox`, `TimelineDeleteBox`). The UI connects via a centralized `api-client.js` module, replacing mock data with real API calls, and includes comprehensive error handling and loading states.

## Key Functions

### `TimelineManagementAPIBox`

Handles CRUD operations for timelines and their events via box-based storage boxes.

### `StoryManagementAPIBox`

Manages story generation and persistence, storing elements as specialized `Card` records with `is_story_element=True`.

### `API Client Module (`api-client.js`)`

Centralized frontend abstraction layer for all backend API endpoints, including error handling and JWT token management.

### `TimelineUpdateBox/DeleteBox`

Storage boxes for updating/deleting timelines, integrated into `TimelineManagementAPIBox`.

### `StoryChainOrchestratorBox`

Legacy logic for story generation (to be migrated to box-based architecture).

## Usage

1. **Backend Development**:
   - Implement missing API boxes (e.g., `StoryGenerationBox`) following the box pattern.
   - Register boxes in `backend/app.py` for routing.
   - Ensure storage boxes (e.g., `TimelineUpdateBox`) are integrated into API boxes.

2. **Frontend Development**:
   - Replace mock data in `ui-beta` with calls to the centralized `api-client.js`.
   - Use the client’s methods (e.g., `api.timelines.list()`) to interact with backend APIs.
   - Handle loading/error states via the client’s error management system.

## Dependencies

> `Django backend framework`
> `SQLAlchemy (ORM)`
> `Flask (for API blueprints)`
> ``ui-beta` frontend module (JavaScript)`
> `existing database models (`Card``
> ``Link``
> ``Timeline``
> `etc.)`
> `and box-based storage/box pattern implementation.`

## Related

- [[Backend Architecture Notes]]
- [[Database Schema Design]]
- [[UI-Backend Mock Data Replacement]]

>[!INFO] Box-Based Pattern
> The box pattern modularizes database operations (e.g., `TimelineReadBox`) and API endpoints, enabling independent updates and reusability. Each box encapsulates CRUD logic for specific entities (e.g., `Card`, `TimelineEvent`).


>[!WARNING] Legacy Story Logic
> The current `StoryChainOrchestratorBox` uses a non-box-based approach. **Critical**: Migrate this logic to the box pattern in Phase 2 to align with the architecture’s consistency. This avoids technical debt and ensures uniformity across the system.
