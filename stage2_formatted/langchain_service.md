**Tags:** #story-generation, #LLM-integration, #memory-management, #time-position-aware, #dataclasses, #Redis, #Ollama, #External-AI
**Created:** 2026-01-13
**Type:** documentation-research

# langchain_service

## Summary

```
A LangChain service framework for advanced storytelling with context-aware memory, time/location tracking, and AI integration.
```

## Details

> This service implements a modular architecture for enhanced narrative generation using LangChain. It integrates with Ollama and external AI services (e.g., Perplexity/OpenAI) while maintaining temporal and spatial context through a custom `StoryContext` dataclass. The `PositionTimeMemory` class leverages Redis for distributed session storage, tracking story progression via Redis keys (`story_context`, `current_position`, `current_time`). Key components include:
> 1. **LLM Wrappers** (`OllamaLangChainLLM`, `ExternalLangChainLLM`) for seamless integration with LangChain’s LLM interface.
> 2. **Context Management** via `StoryContext` dataclass, storing metadata like location, time period, and world elements.
> 3. **Memory System** with Redis-backed persistence for session continuity across interactions.
> 
> The code abstracts API calls to AI services (e.g., Ollama/Perplexity) and applies stop sequences to truncate responses dynamically.

## Key Functions

### ``StoryContext``

Dataclass encapsulating narrative metadata (e.g., `location`, `timeline_events`).

### ``OllamaLangChainLLM``

LangChain-compatible wrapper for Ollama’s text generation API.

### ``ExternalLangChainLLM``

Wrapper for external providers (Perplexity/OpenAI), configurable via `provider` field.

### ``PositionTimeMemory``

Redis-backed memory manager for time/location-aware storytelling.

### ``load_memory_variables``

Returns Redis keys for context tracking.

## Usage

1. **Initialize LLM Wrappers**:
   ```python
   ollama_llm = OllamaLangChainLLM(ollama_service=OllamaService())
   external_llm = ExternalLangChainLLM(provider="perplexity")
   ```
2. **Create Context**:
   ```python
   context = StoryContext(
       location="Medieval Castle",
       time_period="12th Century",
       characters=["Knight", "Mage"]
   )
   ```
3. **Use Memory**:
   ```python
   memory = PositionTimeMemory(redis_client=redis.Redis())
   memory.context = context  # Update context via Redis
   ```
4. **Chain with LangChain**:
   ```python
   from langchain.chains import LLMChain
   chain = LLMChain(llm=external_llm, prompt=PromptTemplate.from_template("Tell a story..."))
   ```

## Dependencies

> ``langchain_core``
> ``pydantic``
> ``redis``
> ``ai_service``
> ``models` (DB models)`
> ``config``
> ``api_key_service`.`

## Related

- [[LangChain Core Documentation]]
- [[Redis Persistence Patterns]]
- [[Ollama API Reference]]

>[!INFO] Context Initialization
> By default, `PositionTimeMemory` initializes `location`/`time_period` to `"Unknown"` and generates a session ID via `datetime`. Override these values during instantiation for custom contexts.


>[!WARNING] Redis Dependency
> If `redis.Redis` is unavailable, `PositionTimeMemory` falls back to in-memory storage (default `session_id`). For distributed systems, ensure Redis is configured externally.
