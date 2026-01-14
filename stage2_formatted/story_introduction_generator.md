**Tags:** #AI-Assisted-Generation, #Storytelling, #Worldbuilding, #Prompt-Engineering, #NLP
**Created:** 2026-01-13
**Type:** documentation

# story_introduction_generator

## Summary

```
Creates dynamic story introductions using AI to contextualize world details and characters.
```

## Details

> This box integrates an AI service orchestrator to dynamically generate immersive story openings by combining world metadata (name, description, location, time period) and character details. It constructs a structured prompt that emphasizes setting immersion and character introduction, then delegates generation to an external AI model. The system validates AI responses and returns structured metadata alongside the generated text.

## Key Functions

### `StoryIntroductionGeneratorBox`

Core class handling prompt construction and AI orchestration.

### ``__init__``

Initializes with optional AI orchestrator dependency and sets default parameters.

### `execute`

Orchestrates prompt generation, AI invocation, and result processing.

### `AIServiceOrchestratorBox`

External dependency for AI model execution (via `self.ai_orchestrator`).

### `prompt construction`

Dynamically builds narrative context from input data (e.g., `world_name`, `characters`).

## Usage

1. Pass input data containing `world_name`, `world_description`, `location`, `time_period`, and `characters`.
2. Optionally specify `provider`, `model`, `temperature`, or `max_tokens`.
3. Retrieve `introduction_text` and metadata (e.g., `world_hash`) from the output.

## Dependencies

> ``AIServiceOrchestratorBox``
> ``logging``
> ``typing` (standard libraries)`
> ``BoxInput``
> ``BoxOutput` (custom interfaces).`

## Related

- [[`core]]
- [[`ai_services]]

>[!INFO] Contextual Prompting
> The prompt dynamically adjusts based on input data, ensuring relevance to the provided world and characters. Missing values default to generic placeholders (e.g., "Unknown World").

>[!WARNING] AI Dependency
> Fails silently if the AI orchestrator returns an unsuccessful response. Validate `ai_result.success` before trusting `introduction_text`.
