**Tags:** #AI-driven-scene-generation, #character-interaction, #prompt-engineering, #box-module, #storytelling
**Created:** 2026-01-13
**Type:** code-module

# character_scene_generator

## Summary

```
Generates dynamic character interaction scenes using AI prompts for narrative storytelling.
```

## Details

> This module creates immersive character interactions by combining user-provided inputs (characters, location, time) with AI-generated dialogue and descriptions. It leverages an external AI orchestrator to produce scene text, preserving metadata like robotic elements and story context. The prompt dynamically constructs a narrative framework emphasizing human-machine symbiosis and predictable yet unique relationships.

## Key Functions

### `CharacterSceneGeneratorBox`

Core class handling scene generation logic, integrating user inputs and AI orchestration.

### `execute()`

Orchestrates AI-driven scene creation with configurable parameters (temperature, tokens, model).

### `AIServiceOrchestratorBox dependency`

Manages AI model invocation and error handling.

## Usage

1. Initialize with an optional `AIServiceOrchestratorBox` instance.
2. Call `execute()` with a `BoxInput` containing:
   - Required: `characters`, `location`, `time_period`
   - Optional: `robotic_elements`, `story_context`, `provider`, `temperature`, `max_tokens`
3. Output includes validated scene text and metadata.

## Dependencies

> ``Box``
> ``BoxInput``
> ``BoxOutput``
> ``AIServiceOrchestratorBox``
> ``logging``

## Related

- [[`core]]
- [[`ai_services]]

>[!INFO] Context Handling
> Context (e.g., prior story parts) is merged with `story_context` if missing, ensuring continuity.

>[!WARNING] AI Dependency
> Fails gracefully if AI orchestrator returns `success=False`, preserving input data structure.
