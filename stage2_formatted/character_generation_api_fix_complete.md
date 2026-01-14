**Tags:** #api-fix, #character-generation, #module-imports, #deterministic-hashing, #backend-development
**Created:** 2026-01-13
**Type:** documentation

# character_generation_api_fix_complete

## Summary

```
Fixes character generation API module import conflicts to resolve 500 errors and ensure consistent module loading for hashed character assets.
```

## Details

> The fix resolves a module import conflict where two conflicting character generator modules (`/app/generators/Characters/characters.py` and `/app/generators/Creatures/Characters/characters.py`) caused the API to load the wrong module, resulting in inconsistent responses. The solution uses absolute import paths via `importlib.util` to dynamically load the correct module, ensuring deterministic character generation with consistent output structures. The fix applies to three endpoints: `/api/characters/generate`, `/api/characters/generate/hash`, and `/api/characters/generate/random`.

## Key Functions

### ``generate_character_description``

Generates a structured character description with personality traits, background, and physical attributes.

### ``hash_input``

Computes a deterministic hash for character seeds to ensure reproducibility.

### ``importlib.util.spec_from_file_location``

Dynamically imports the correct module path for absolute resolution.

### ``backend/app.py``

Updated endpoints to use absolute imports instead of relative paths.

## Usage

1. **API Endpoints**:
   - Use `/api/characters/generate` with a JSON payload containing a `seed` to generate a character.
   - Use `/api/characters/generate/hash` with a `seed` to generate a character deterministically via hashing.
   - Use `/api/characters/generate/random` to generate a random character without a seed.

2. **Testing**:
   - Run `curl` commands provided in the documentation to verify API responses.
   - Ensure the backend container (`space-pearl-backend`) is running and accessible at `http://localhost:5173`.

## Dependencies

> ``os``
> ``importlib.util``
> ``json` (Python standard libraries)`
> ``PostgreSQL` (database backend)`
> ``JWT` (authentication).`

## Related

- [[character_generation_api_fix_complete]]
- [[app]]
- [[simple-screenshot-test]]

>[!INFO] **Deterministic Hashing**
> The `hash_input` function ensures consistent character generation by using a seed-based hashing algorithm, preventing variations in output across runs.


>[!WARNING] **Module Path Validation**
> Always verify module paths in development environments, as misconfigured paths can lead to import errors. Use absolute paths (`os.path.join`) to avoid conflicts.
