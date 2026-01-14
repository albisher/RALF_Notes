**Tags:** #flask, #api, #timeline-management, #jwt-authentication, #database-querying
**Created:** 2026-01-13
**Type:** documentation

# timeline

## Summary

```
Manages user timelines with event tracking in a Flask-based application using JWT authentication.
```

## Details

> This file defines a Flask Blueprint (`timeline_bp`) for handling CRUD operations on timelines and their associated events. It uses SQLAlchemy for database interactions and Flask-JWT-Extended for authentication. The routes support fetching all timelines, creating new timelines, and retrieving specific timelines with their events, all secured with JWT validation.

## Key Functions

### `get_timelines`

Fetches all timelines for the authenticated user, ordered by creation date (newest first), including event counts.

### `create_timeline`

Creates a new timeline linked to a validated world, ensuring uniqueness and user ownership.

### `get_timeline`

Retrieves a specific timeline and its associated events, enriching event data with linked world elements if present.

## Usage

1. **GET `/api/timelines`**: Retrieve all timelines for the authenticated user.
2. **POST `/api/timelines`**: Create a new timeline with required fields (name, world_id).
3. **GET `/api/timelines/<int:timeline_id>`**: Retrieve a specific timeline and its events.

## Dependencies

> `Flask`
> `Flask-JWT-Extended`
> `SQLAlchemy (db)`
> `datetime`
> `models (Timeline`
> `TimelineEvent`
> `World`
> `WorldElement)`

## Related

- [[Flask-JWT-Extended Documentation]]
- [[SQLAlchemy ORM Guide]]
- [[World and Timeline Model Definitions]]

>[!INFO] Authentication Requirement
> All endpoints require a valid JWT token in the request headers. The `jwt_required` decorator enforces this.

>[!WARNING] Database Rollback on Error
> If an exception occurs during `create_timeline`, the database session is rolled back to maintain consistency.
