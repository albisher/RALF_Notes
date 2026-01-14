**Tags:** #card-system, #api-integration, #validation, #async-operations
**Created:** 2026-01-13
**Type:** code-notes

# card_box

## Summary

```
Manages card operations (create/update/list/get/delete) with type validation and error handling for a card-stage system.
```

## Details

> The `CardBox` class extends `Box` to handle card-related operations via an API client (`CardsAPIBox`). It validates input data (e.g., card types) before delegating to the `CardsAPIBox` for execution. The system supports CRUD operations (`create`, `update`, `list`, `get`, `delete`) with configurable schemas for input/output validation. Errors are categorized (e.g., `INVALID_FIELD_VALUE`, `API_ERROR`) and returned via `BoxOutput`.

## Key Functions

### ``constructor(apiClient)``

Initializes `CardBox` with an API client and validates dependencies (e.g., `CardsAPI`).

### ``_executeInternal(inputData)``

Orchestrates operation execution (switch-case logic) and validates inputs (e.g., card type) before delegating to `CardsAPIBox`.

### ``CardsAPIBox``

External API wrapper for delegated operations (e.g., `create`, `update`).

## Usage

1. Instantiate `CardBox` with an API client.
2. Call `_executeInternal` with an input object containing `operation` (e.g., `'create'`) and relevant params (e.g., `cardData`).
3. Handle returned `BoxOutput` (success/error).

## Dependencies

> ``../core/box_interface.js``
> ``../api/cards_api_box.js``
> ``../../services/config.js``
> ``Box``
> ``BoxInput``
> ``BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`.`

## Related

- [[`Box` architecture]]
- [[`CardsAPIBox` documentation]]

>[!INFO] Input Validation
> Card type validation occurs via `config.CARD_TYPES` (default: `Object.values(config.CARD_TYPES || {})`). Missing `card_type` defaults to `cardData.type`.

>[!WARNING] Error Handling
> External API errors default to `BoxErrorCode.API_ERROR`. Customize error codes (e.g., `INVALID_FIELD_VALUE`) for granular feedback.
