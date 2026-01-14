**Tags:** #SQLAlchemy, #EagerLoading, #DatabaseQuery, #WorldDataLoader, #RelationshipMapping, #Pagination, #SecurityCheck
**Created:** 2026-01-13
**Type:** documentation-research

# world_load_box

## Summary

```
Efficiently loads a world and its associated content (cards, elements, timelines) using SQLAlchemy eager loading for optimized database queries.
```

## Details

> This `WorldLoadBox` class implements a box (likely a component in a framework like FastAPI or similar) that loads a world and its nested content (cards, elements, timelines, and events) with configurable inclusion and pagination. It uses SQLAlchemy’s `selectinload` and `joinedload` for efficient relationship handling, ensuring minimal database queries. The class validates user access, serializes world data, and conditionally loads requested subcomponents (e.g., paginates cards if specified).

## Key Functions

### ``WorldLoadBox``

Core class handling world data loading with configurable eager loading.

### ``execute()``

Main method that processes input data, validates requirements, and fetches world content.

### ``World.query.filter_by()``

Base query for world validation (security check).

### ``Card.query.filter_by()``

Loads cards with optional pagination.

### ``WorldElement.query.filter_by()``

Loads world elements.

### ``Timeline.query``

(Incomplete) Loads timelines with nested events (not fully implemented in snippet).

## Usage

1. Instantiate `WorldLoadBox` with a name (default: `'world_load'`).
2. Call `execute()` with an `BoxInput` object containing:
   - `world_id` (required): ID of the world to load.
   - `user_id` (required): User ID for security validation.
   - `include` (optional): List of subcomponents to load (default: `['cards', 'elements', 'timelines', 'events']`).
   - `paginate_cards` (optional): If `True`, paginates cards if count exceeds `card_limit`.
   - `card_limit` (optional): Max cards to load (default: `100`).
3. Return `BoxOutput` with serialized world data, subcomponents, and statistics.

## Dependencies

> ``sqlalchemy``
> ``sqlalchemy.orm``
> ``models.db``
> ``models.World``
> ``models.Card``
> ``models.WorldElement``
> ``models.Timeline``
> ``models.TimelineEvent``
> ``..core.box_interface` (custom framework components).`

## Related

- [[WorldModel (Core model definitions for `World`]]
- [[`Card`]]
- [[`WorldElement`]]
- [[etc]]
- [[output handling).]]

>[!INFO] Eager Loading Strategy
> Uses `selectinload` for one-to-many relationships (e.g., cards, elements) and `joinedload` for nested events (timeline hierarchy). This minimizes database roundtrips by loading related data in a single query.


>[!WARNING] Security Validation
> **Critical**: Always validate `world_id` and `user_id` before proceeding. Invalid inputs return a `BoxOutput` with `success=False` and an error message.
