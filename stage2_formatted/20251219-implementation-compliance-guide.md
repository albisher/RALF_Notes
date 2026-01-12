**Tags:** #compliance, #implementation, #architecture, #code-patterns, #logging, #open-source
**Created:** 2026-01-12
**Type:** documentation

# implementation-compliance-guide

## Summary

```
Step-by-step guide ensuring compliance with codebase standards for new feature implementations.
```

## Details

> This guide outlines structured compliance rules for implementing new features, bug fixes, or enhancements while adhering to strict architectural and coding standards. It emphasizes modularity (Box Architecture), componentization (Vue), and adherence to file length limits (Python <500 lines, JavaScript <300 lines). The document also enforces OOP principles, logging standardization via `LoggingBox`, and support for open-source map sources (OSM required, Google optional).

## Key Functions

### `New Box Implementation`

Follows single-responsibility principle with file naming conventions (`*_box.py`), class naming (`*Box`), and logging via `LoggingBox`.

### `Vue Componentization`

Encourages small, reusable Vue components with clear separation of concerns.

### `File Length Enforcement`

Enforces strict limits (<500 lines for Python, <300 lines for JS) to maintain modularity.

### `Logging Standardization`

Mandates use of `LoggingBox` instead of `print()` or `console.log()`.

### `Map Source Selection`

Supports OSM (required) and Google Maps (optional) with fallback mechanisms.

## Usage

1. **Pre-Implementation**: Review compliance assessments (`codebase-compliance-assessment.md`, `logging-mechanism-assessment.md`).
2. **Plan**: Use the checklist to structure new boxes/components, ensuring single responsibility and adherence to file length limits.
3. **Implement**: Follow the box/component patterns (e.g., `*_box.py` for Python, Vue components for JS).
4. **Log**: Use `LoggingBox` for all outputs to avoid non-compliant `print()` calls.
5. **Map Support**: Implement OSM as a primary source, with optional Google Maps fallback.

## Dependencies

> `- `LoggingBox` (internal logging standard)
- Open-source map libraries (OSM`
> `Google Maps)`

## Related

- [[20251219-codebase-compliance-assessment]]
- [[20251219-logging-mechanism-assessment]]
- [[20251219-reusability-usability-assessment]]

>[!INFO] Important Note
> **Single Responsibility Principle**: Every box/component must have one clear purpose. Avoid overloading files with unrelated logic.
>

>[!WARNING] Caution
> **File Length Limits**: Exceeding limits (e.g., >500 lines in Python) may violate compliance. Prefer breaking into smaller files if needed.
