**Tags:** #AI #Configuration #TaskMaster #ModelManagement, #Backend #CLI #FallbackSystems
**Created:** 2026-01-13
**Type:** documentation

# view-models

## Summary

```
Displays and validates AI model configurations for Task Master, including primary, research, and fallback providers with status checks.
```

## Details

> This module provides a command-line interface (`task-master models`) to inspect the current AI model setup for Task Master. It categorizes configurations into **Main Provider** (primary task generation), **Research Provider** (enhanced research mode), and **Fallback Provider** (backup fallback). Each provider lists its model ID/name, API key status, and designated use case. The visual output includes a status bar with emoji indicators (✅/⚠️) and a list of available models. Post-execution, it triggers recommendations for missing configurations or clarifies benefits of underutilized features.

## Key Functions

### ``task-master models` CLI command`

Executes the model configuration display.

### `Status validation`

Checks API key presence and model availability per provider role.

### `Visual feedback`

Renders a formatted table with emoji-based status indicators.

### `Recommendation engine`

Suggests next actions (e.g., "Suggest setup" for missing keys).

## Usage

1. Run `task-master models` in terminal.
2. Observe the structured output showing provider statuses and available models.
3. Use recommendations to configure missing components or optimize usage.

## Dependencies

> ``task-master-core` (CLI framework)`
> ``ai-provider-utils` (model/API key validation)`
> ``ui-formatting` (visual output rendering).`

## Related

- [[TaskMaster CLI Reference]]
- [[AI Provider Documentation]]
- [[Configuration Guide]]

>[!INFO] Important Note
> Missing API keys for any provider will trigger a warning (⚠️) and prompt setup guidance in subsequent interactions.
> Example: `Main: ⚠️ Missing key → "Configure API key for claude-3-5-sonnet?"`

>[!WARNING] Caution
> Fallback providers are optional but critical for system resilience. Unconfigured fallbacks may cause task failures if primary providers degrade.
