**Tags:** #story-generation, #backend-integration, #world-building, #Ollama-API, #automation
**Created:** 2026-01-13
**Type:** code-script

# generate_story

## Summary

```
Automates story generation by creating a virtual world with assets, then prompts an AI (Ollama) to craft a narrative using those elements.
```

## Details

> This script orchestrates a multi-step workflow:
> 1. Authenticates with a backend API to create a secure world environment.
> 2. Populates the world with predefined characters, buildings, and robots using a timestamped name for uniqueness.
> 3. Retrieves all elements (characters, buildings, robots) to construct a cohesive story prompt.
> 4. Uses Ollama (via backend) to generate a narrative based on the populated world data.
> 
> The backend acts as an intermediary, handling authentication, world management, and AI integration while the script manages the data flow between components.

## Key Functions

### `create_test_user()`

Logs in with hardcoded credentials to obtain an authentication token.

### `create_world_with_assets(token)`

Creates a world and populates it with characters, buildings, and robots using the provided token.

### `generate_comprehensive_story(world_id, headers)`

Fetches world elements, constructs a story prompt, and delegates narrative generation to Ollama via the backend.

## Usage

1. Run the script to:
   - Authenticate with the backend.
   - Generate a unique world with assets.
   - Retrieve elements to craft a story prompt.
   - Generate and save the story to `../generated_stories/`.
2. Ensure the backend is running and accessible at `http://backend:5000` with the required API endpoints.

## Dependencies

> `requests`
> `urllib3`
> `datetime`
> `pathlib`
> `json (standard Python libraries)
Ollama backend service (running on `http://backend:5000`)`

## Related

- [[backend_api_documentation]]
- [[ollama_integration_guide]]

>[!INFO] World Naming Convention
> Names include a timestamp (`%Y%m%d_%H%M%S`) and a suffix (`Story Colony Alpha`) to ensure uniqueness across runs.

>[!WARNING] Security Note
> SSL verification is disabled (`session.verify = False`) for simplicity, but this may expose the script to man-in-the-middle attacks. Use in trusted environments only.
