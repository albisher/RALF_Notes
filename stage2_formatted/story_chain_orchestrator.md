**Tags:** #orchestration, #story-generation, #multi-part-story, #box-system, #AI-assisted-creation
**Created:** 2026-01-13
**Type:** code-notes

# story_chain_orchestrator

## Summary

```
Manages multi-part story generation by coordinating three core components: introduction, character scenes, and ecosystem scenes.
```

## Details

> The `StoryChainOrchestratorBox` class acts as a central controller for generating complete narratives by sequentially processing inputs through three specialized generators (`StoryIntroductionGeneratorBox`, `CharacterSceneGeneratorBox`, and `EcosystemSceneGeneratorBox`). It dynamically selects which story components to include based on user-provided flags (`include_intro`, `include_character_scene`, `include_ecosystem_scene`) and merges results into a cohesive output. The orchestrator maintains an evolving context (`current_context`) to pass relevant narrative state between stages, ensuring continuity. It supports optional external API integration via `use_external_api` and `external_provider`, defaulting to `ollama`.

## Key Functions

### ``__init__``

Initializes the orchestrator with optional dependencies (defaulting to new instances if none provided) and sets up metadata for the `Box` interface.

### ``execute``

Orchestrates the full story generation workflow by:

## Usage

1. **Initialization**: Create an instance of `StoryChainOrchestratorBox` with optional preconfigured generators.
2. **Execution**: Pass input data (e.g., `world_data`, `session_id`) via `execute()` to generate a complete story.
3. **Customization**: Use boolean flags (`include_intro`, etc.) to exclude optional story components.
4. **Context Handling**: The orchestrator dynamically updates `current_context` to preserve narrative continuity across stages.

## Dependencies

> ``..core.box_interface``
> ``.story_introduction_generator``
> ``.character_scene_generator``
> ``.ecosystem_scene_generator``

## Related

- [[AI Story Generation Framework]]
- [[Box System Architecture]]

>[!INFO] Context Propagation
> The `current_context` dictionary is updated incrementally after each story part (introduction → character scenes → ecosystem scenes). This ensures that later generators receive updated narrative context, enabling dynamic storytelling where characters/locations evolve across parts.

>[!WARNING] Dependency Fallback
> If a generator (e.g., `StoryIntroductionGeneratorBox`) is not provided during initialization, the orchestrator defaults to a new instance. This may introduce slight variations in output if the default generator’s logic differs from a custom one. Always pass explicit dependencies for deterministic results.
