**Tags:** #critical-findings, #database-integration, #api-validation, #static-data-bypass, #frontend-security
**Created:** 2026-01-13
**Type:** code-review-summary

# REVIEW_FINDINGS_SUMMARY

## Summary

```
Analyzes UI component issues in `ui-beta` folder, focusing on external dependencies, API compliance, and data integrity violations.
```

## Details

> The review identifies critical issues in `ui-beta` where external paths, static data workarounds, and missing validation violate design patterns. Key problems include hardcoded external references (e.g., map viewer URLs), bypassing database integration via `cards-data.js`, and incomplete error handling in box components. The code fails compliance checks for proper world filtering and static data elimination, posing risks for incorrect data loading and security vulnerabilities.

## Key Functions

### ``loadCards()` (cardview.html)`

Loads cards from `cards-data.js` instead of database API.

### ``validateInput()` (api boxes)`

Missing parameter validation for `world_id` in `cards_api_box.js`.

### ``getMapViewerUrl()` (config.js)`

External dependency reference in `ui-explorations` path.

### ``api-client.js``

Lacks world name validation alongside `world_id` checks.

### ``Box` base class`

All boxes extend it, but some fail validation consistency.

## Usage

The codebase should:
1. Replace static `cards-data.js` with database API calls.
2. Validate world names alongside `world_id` in API calls.
3. Remove external paths (e.g., `ui-explorations`) and use environment variables.
4. Enhance error messages with operation context.

## Dependencies

> ``vue.js``
> ``material-icons``
> ``google-fonts` (CDN)`
> ``js/config.js``
> ``js/boxes/*``
> ``js/api-client.js``
> ``ui-beta/data/cards-data.js``
> ``ui-beta/ui-explorations/mapviewer-iteration-overlay`.`

## Related

- [[Code Review: Box Method Compliance]]
- [[Database API Integration Guide]]
- [[Frontend Security Best Practices]]

>[!INFO] Critical Workaround
> The `cards-data.js` file acts as a bypass for database integration, risking inconsistent data. **Must replace with API calls** to ensure real-time data.

>[!WARNING] Security Risk
> Hardcoded URLs (e.g., `http://localhost:8888/ui-explorations`) expose frontend to path manipulation attacks. **Sanitize or remove external references.**
