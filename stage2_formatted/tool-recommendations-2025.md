**Tags:** #AI-integration, #project-management, #workflow-orchestration, #open-source-tools, #docker-stack, #vuejs-python, #self-hosting, #world-building, #code-assistance
**Created:** 2026-01-13
**Type:** documentation

# tool-recommendations-2025

## Summary

```
Provides 2025 tool recommendations for a Space Pearl world-building application leveraging Vue.js, Python, Docker, and AI, focusing on open-source, self-hosted solutions.
```

## Details

> This document offers a curated selection of open-source tools optimized for a **Space Pearl** project, combining AI-driven story generation with a **Vue.js + Python + Docker** backend. It prioritizes flexibility, cost-efficiency, and seamless integration with existing infrastructure. The recommendations emphasize **self-hosted solutions** to avoid vendor lock-in, with a focus on **code assistance, project management, and workflow orchestration**. The stack is designed to support dynamic AI-driven world-building while maintaining full control over data and infrastructure.

## Key Functions

### `Continue`

AI-assisted code generation and completion for Vue.js/Python development via Perplexity API.

### `OpenProject`

Self-hosted project management with REST API for automation, Docker support, and enterprise-grade features.

### `n8n`

Open-source workflow automation tool for orchestrating AI API calls (e.g., Perplexity, OpenAI) with custom code nodes.

### `Docker Compose`

Orchestrates deployment of Continue, OpenProject, and n8n in isolated containers for scalability.

### `AI Integration Workflows`

Predefined chains (e.g., world research → story generation) triggered by project events (e.g., new task in OpenProject).

## Usage

1. **Deploy Tools**:
   - Install Continue via VS Code or CLI, configure with Perplexity API key.
   - Deploy OpenProject via Docker with `docker-compose.yml` (e.g., `openproject_data` volume for persistence).
   - Deploy n8n via Docker with encrypted credentials for API key management.
2. **Integrate Workflows**:
   - Use OpenProject’s REST API to trigger n8n workflows (e.g., "New World Creation" → AI chain).
   - Leverage Continue’s API to generate code snippets for Vue.js/Python features.
3. **Monitor Costs**: Track Perplexity API usage separately; all other tools are free (self-hosted).

## Dependencies

> `Docker`
> `Docker Compose`
> `OpenProject Docker image`
> `n8n Docker image`
> `Perplexity API key`
> `OpenAI API key (if used)`
> `existing Vue.js/Python backend.`

## Related

- [[Space Pearl Backend Architecture]]
- [[AI Story Generation Protocols]]
- [[Dockerized Open-Source Stacks]]

>[!INFO] **Self-Hosting Advantage**
> By deploying Continue, OpenProject, and n8n in Docker, the project avoids subscription costs and retains full control over data privacy. This aligns with Space Pearl’s emphasis on autonomy and customization.


>[!WARNING] **API Key Security**
> Store API keys (Perplexity/OpenAI) in Docker environment variables **never** in plaintext files. Use n8n’s credential storage or a secrets manager (e.g., Vault) for sensitive data. Leaked keys could expose AI-generated content to unauthorized access.
