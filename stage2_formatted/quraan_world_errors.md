**Tags:** #error-handling, #date-parsing, #historical-data, #database-errors, #backend-debugging, #iso-format, #quran-world, #timeline-functionality
**Created:** 2026-01-14
**Type:** code-notes

# quraan_world_errors

## Summary

```
Identifies production errors in Quraan World script, focusing on timestamp parsing failures for historical dates and configuration warnings for Redis/Ollama.
```

## Details

> The script detects two primary issues: **1)** `_parse_timestamp` in `CardWriteBox` fails to parse pre-1900 dates (e.g., `610-01-01`), causing `None` storage and timeline inaccuracies; **2)** unconfigured Redis passwords trigger warnings in LangChain and reset services, and missing Ollama URL defaults to a Docker-specific host. These errors stem from insufficient validation for historical date formats and misconfigured external dependencies.

## Key Functions

### ``_parse_timestamp` (in `CardWriteBox`)`

Attempts to parse dates but fails for non-ISO formats (e.g., `YYYY-MM-DD` with years < 1900).

### ``Redis` (backend)`

Requires password authentication; missing config causes warnings in memory/reset services.

### ``Ollama` (AI service)`

Defaults to `host.docker.internal` if URL isn’t set, limiting cross-platform compatibility.

## Usage

To resolve:
1. **Fix `_parse_timestamp`**: Update logic to support `YYYY-MM-DD` for years < 1900.
2. **Configure Redis**: Set password in `docker-compose.yml` or env vars.
3. **Set Ollama URL**: Define `OLLAMA_BASE_URL` if AI features are enabled.

## Dependencies

> `- `CardWriteBox` (backend/boxes/storage): Core component for timestamp handling.
- `Redis` (external): Used by LangChain and reset services.
- `Ollama` (AI): Optional dependency for AI features.`

## Related

- [[Quraan World Backend Architecture]]
- [[Database Schema for CardWriteBox]]

>[!INFO] Important Note
> Historical dates like `610-01-01` (First revelation) are critical for Qur’an studies. Parsing failures break timeline validation, requiring immediate fixes in `_parse_timestamp`.

>[!WARNING] Caution
> Redis warnings may degrade performance in memory-heavy operations. Configure passwords *before* production deployment to avoid silent failures.
