**Tags:** #AI-driven-scene-generation, #ecosystem-modelling, #narrative-generation, #box-system-architecture
**Created:** 2026-01-13
**Type:** code-notes

# ecosystem_scene_generator

## Summary

```
Generates immersive ecosystem and building scenes using AI prompts and contextual inputs.
```

## Details

> This box integrates an AI orchestrator to dynamically create detailed environmental narratives by combining location data, optional buildings/plants, and temporal context. It constructs a prompt string from user inputs, passes it to the AI service, and returns a rendered scene text along with metadata. The system handles optional parameters like temperature and token limits for AI flexibility.

## Key Functions

### ``__init__``

Initializes the box with an optional AI orchestrator dependency and sets up metadata.

### ``execute``

Processes input data to generate a scene description via AI, validates results, and returns structured output.

## Usage

1. Pass input data (e.g., `{"location": "forest", "buildings": ["wooden_house"]}`) to `execute()`.
2. Retrieve `scene_text` and metadata (e.g., `provider="ollama"`).
3. Customize optional parameters like `temperature` or `max_tokens` for AI control.

## Dependencies

> ``AIServiceOrchestratorBox``
> ``BoxInput``
> ``BoxOutput``

## Related

- [[`core]]
- [[`ai_services]]

>[!INFO] Input Handling
> The code defaults to empty strings/lists for missing optional fields (e.g., `buildings` defaults to `[]`). Explicitly provide all required fields (e.g., `location`) to avoid silent failures.

>[!WARNING] AI Dependency
> Fails silently if `AIServiceOrchestratorBox` fails (e.g., network issues). Add retry logic or fallback logic for production use.
