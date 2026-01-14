**Tags:** #AI-driven-story-generation, #backend-integration, #space-colony-simulation, #prompt-engineering, #requests-library
**Created:** 2026-01-13
**Type:** code-notes

# generate_story_simple

## Summary

```
Script generates a simplified space colony story using an AI backend with modular prompts for structured narrative creation.
```

## Details

> This script automates story generation by interacting with a backend API to:
> 1. Authenticate and create a virtual world (space colony) with predefined assets (characters, buildings, robots).
> 2. Break story creation into four logical parts (introduction, character interactions, crisis, conclusion).
> 3. Use simplified prompts to avoid API timeouts by limiting complexity.
> 4. Combine generated segments into a cohesive narrative while preserving metadata (world details, elements, model info).
> 
> The workflow follows a RESTful API pattern, handling authentication, data retrieval, and conditional generation based on element types.

## Key Functions

### `create_test_user()`

Authenticates with backend using hardcoded credentials.

### `create_world_with_assets()`

Creates a colony world and populates it with static elements (characters, buildings, robots).

### `generate_simple_story()`

Orchestrates the entire story generation process by:

### `generate_text_part()`

Delegates individual prompt processing to an external AI service via the backend.

## Usage

1. Execute script to:
   - Create a test user
   - Generate a space colony world
   - Populate it with assets
   - Generate a story using simplified prompts
2. Output includes:
   - World metadata
   - Generated story segments
   - Story structure statistics
   - Model information

## Dependencies

> `requests`
> `urllib3`
> `ai_service (local module)`
> `backend API (http://backend:5000)`

## Related

- [[AI Service Documentation]]
- [[Backend API Specifications]]

>[!INFO] Authentication Note
> Uses hardcoded credentials ('test'/'passtest') for demonstration only. Production should use secure credentials management.

>[!WARNING] Security Warning
> SSL verification is disabled (`session.verify = False`) for simplicity. In production, implement proper certificate validation.

>[!CAUTION] Prompt Complexity
> Simplified prompts are intentionally limited to avoid API timeouts. For longer stories, consider incremental generation with smaller chunks.
