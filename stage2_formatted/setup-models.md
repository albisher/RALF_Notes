**Tags:** #interactive-configuration, #ai-model-setup, #task-master, #provider-selection, #api-key-management
**Created:** 2026-01-13
**Type:** tutorial

# setup-models

## Summary

```
Configures AI model providers for Task Master via an interactive CLI workflow.
```

## Details

> This script automates the setup of AI model providers (e.g., OpenAI, Claude, Perplexity) by prompting users through a guided workflow. It detects existing configurations, validates API keys, and recommends optimal provider combinations based on user needs. The process includes optional fallback configurations and post-setup testing.

## Key Functions

### ``task-master models --setup``

CLI entry point to trigger the interactive setup.

### `Environment Check`

Detects existing API keys and current configurations.

### `Provider Selection`

Guides user to choose primary, research, and fallback providers.

### `API Key Validation`

Tests key format and connectivity before saving.

### `Smart Recommendations`

Suggests optimal provider combinations (e.g., Claude + Perplexity).

### `Configuration Storage`

Supports multiple storage methods (env vars, `.env`, `.taskmaster/config`).

## Usage

1. Run `task-master models --setup` in terminal.
2. Follow prompts to select providers and enter API keys.
3. Validate connectivity and test providers post-setup.

## Dependencies

> ``task-master` CLI library (core dependency)`
> `optional: `python-dotenv` (for `.env` support).`

## Related

- [[Task Master Documentation]]
- [[AI Provider Integration Guide]]

>[!INFO] Important Note
> **Primary Provider is Mandatory**: Without a main provider, the system will fail core operations. Ensure you select a provider with active API keys.
>

>[!WARNING] Caution
> **Key Security**: Avoid hardcoding keys in scripts. Use environment variables or `.env` files securely (e.g., `.taskmaster/config` with restricted permissions).
