**Tags:** #AI-integration, #Flask-Blueprint, #Rate-limiting, #Ollama-API, #World-Generation
**Created:** 2026-01-13
**Type:** documentation

# ai_bp

## Summary

```
Manages AI-driven text and world content generation endpoints for a Flask application with authentication and rate limiting.
```

## Details

> This file defines a Flask Blueprint (`ai_bp`) for handling AI-generated content through three endpoints:
> 1. **Text Generation** – Creates AI-generated text via Ollama or an external API.
> 2. **World Content Generation** – Produces world-specific content (e.g., lore, NPCs) using a world’s metadata.
> 3. **Related Content Generation** – Expands content by generating related items (e.g., synonyms, expansions) based on a hash-based relationship.
> 
> The endpoints enforce JWT authentication and rate limiting (e.g., 10 requests/minute for text generation). They dynamically switch between Ollama (local LLM) and external providers (e.g., Perplexity) based on configuration.

## Key Functions

### ``generate_text()``

Processes a text prompt, validates inputs, and returns AI-generated output with metadata.

### ``generate_world_content()``

Creates world-specific content (e.g., quests, descriptions) tied to a user’s `World` object.

### ``generate_related_content()``

Expands content by generating related items (e.g., alternate versions, expansions) using a hash-based relationship.

### ``ai_service.check_ollama_health()``

Checks if Ollama is running before proceeding with local LLM calls.

### ``rate_limit_decorator``

Limits API calls to prevent abuse (e.g., 10 calls/minute for text generation).

## Usage

1. **Initialize the Blueprint**:
   ```python
   from ai_bp import ai_bp
   app.register_blueprint(ai_bp)
   ```
2. **Call Endpoints**:
   - **Text Generation**: `POST /api/ai/generate-text` with `prompt`, `model`, etc.
   - **World Content**: `POST /api/ai/generate-world-content` with `world_id`, `content_type`.
   - **Related Content**: `POST /api/ai/generate-related-content` with `base_hash`, `relation_type`.

## Dependencies

> ``flask``
> ``flask-jwt-extended``
> ``models` (SQLAlchemy `db``
> ``World``
> ``WorldElement`)`
> ``ai_service` (Ollama integration)`
> ``request``
> ``jsonify``
> ``logging`.`

## Related

- [[`ai_service]]
- [[`models]]
- [[`flask-jwt-extended` documentation]]

>[!INFO] **Ollama Dependency**
> If `use_external_api=False`, the endpoint checks `ai_service.check_ollama_health()` before proceeding. If Ollama is unavailable, it returns a 503 error.

>[!WARNING] **Rate Limiting**
> Exceeding rate limits (e.g., 10 requests/minute) triggers a 429 response. Always handle errors gracefully in client code.
