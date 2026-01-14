**Tags:** #Flask, #API, #Database, #Card Management, #JWT Authentication, #Blueprint, #Database Operations
**Created:** 2026-01-13
**Type:** documentation

# card_management_bp

## Summary

```
Manages card creation, listing, editing, and deletion via a Flask blueprint with JWT authentication.
```

## Details

> This `CardManagementAPIBox` class implements a Flask blueprint for handling CRUD operations on cards. It uses specialized boxes (`CardBuilderBox`, `CardUniquenessBox`, etc.) to abstract database interactions and business logic. The blueprint registers routes for listing cards (GET) and creating cards (POST) with JWT authentication. It validates uniqueness before saving cards and delegates database operations to `CardReadBox`, `CardWriteBox`, etc. Error handling and logging are integrated for robustness.

## Key Functions

### ``CardManagementAPIBox``

Core class initializing all card management components and routes.

### ``list_cards``

Fetches cards filtered by `user_id`, `world_id`, and `card_type` using `CardReadBox`.

### ``create_card``

Builds a card using `CardBuilderBox`, checks uniqueness via `CardUniquenessBox`, then saves via `CardWriteBox`.

### ``_card_to_dict``

Helper method (not shown in snippet) to convert `Card` objects to dictionaries for uniqueness checks.

### ``_register_routes``

Registers Flask blueprint routes for `/` with GET/POST methods.

## Usage

1. Initialize `CardManagementAPIBox` in your Flask app.
2. Register the blueprint with `app.register_blueprint(card_box.blueprint)`.
3. Use endpoints:
   - `GET /api/cards` → List cards (with optional `world_id`/`card_type` filters).
   - `POST /api/cards` → Create a new card (requires JWT token and card data).

## Dependencies

> ``flask``
> ``flask-jwt-extended``
> ``SQLAlchemy``
> ``CardBuilderBox``
> ``CardUniquenessBox``
> ``CardImageGeneratorBox``
> ``CardTemplateBox``
> ``CardReadBox``
> ``CardWriteBox``
> ``CardUpdateBox``
> ``CardDeleteBox``
> ``BoxInput`.`

## Related

- [[`card_builder_box]]
- [[`card_uniqueness_box]]
- [[`card_read_box]]
- [[`core.box_interface]]

>[!INFO] Uniqueness Check
> The `create_card` method checks for duplicates using `CardUniquenessBox` before saving, comparing `uniqueness_signature`, `card_name`, and spatial/temporal hashes (`location_hash`, `time_hash`). This prevents accidental duplicates across worlds or locations.


>[!WARNING] Large Limit Warning
> The `list_cards` route defaults to a `limit` of 1000, which may need adjustment for large datasets. Consider dynamic limits or pagination for scalability.
