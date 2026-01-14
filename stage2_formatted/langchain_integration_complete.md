**Tags:** #LangChain, #Flask, #Storytelling, #AI-Integration, #Redis, #MemoryManagement, #Chatbot, #PositionTimeAwareness, #WorldGeneration
**Created:** 2026-01-13
**Type:** documentation

# langchain_integration_complete

## Summary

```
LangChain integration for a Flask-based storytelling system enhances narrative generation with chat capabilities, memory management, and temporal/contextual awareness.
```

## Details

> This code file documents a complete integration of LangChain into a Flask backend to enable advanced story generation. The system leverages Ollama for language model capabilities, implements a custom memory system (`PositionTimeMemory`) to track story context by location and time, and integrates REST APIs for story and chat functionality. The implementation uses Redis for persistent session storage, ensuring continuity across API calls. Key features include position/time-aware storytelling, multi-part narrative generation, and conversational chat with AI-driven storytelling.

## Key Functions

### `OllamaLangChainLLM`

Wraps OllamaService for LangChain compatibility.

### `PositionTimeMemory`

Manages story context with location/time relationships.

### `Flask API Endpoints (`langchain_bp.py`)`

Handles story generation, chat, and session management.

### `Prompt Templates`

Specialized templates for story introductions, character scenes, and ecosystem scenes.

### `Redis Integration`

Persists session memory across requests with automatic cleanup via TTL.

## Usage

1. **Initialize Story**: Use `POST /api/langchain/story/start` with world context (e.g., `world_id`, `initial_location`, `time_period`).
2. **Continue Story**: Call `POST /api/langchain/story/continue` with additional context.
3. **Chat**: Send messages via `POST /api/langchain/chat` with a `session_id` to maintain conversation history.
4. **Query Elements**: Retrieve story elements by location/time using `GET /api/langchain/elements/by-location` or `GET /api/langchain/elements/by-time`.
5. **Manage Sessions**: Check status with `GET /api/langchain/session/status` or clear memory with `DELETE /api/langchain/session/clear`.

## Dependencies

> `langchain>=0.1.0`
> `langchain-community>=0.0.10`
> `langchain-core>=0.1.0`
> `Redis`

## Related

- [[Backend Architecture]]
- [[World Generation System]]

>[!INFO] **Session Isolation**
> Redis-based memory storage ensures session isolation, preventing conflicts between concurrent story/chat sessions.

>[!WARNING] **Rate Limiting**
> The system enforces a rate limit of 20 calls per minute per user to prevent abuse, as integrated with the existing rate-limiting system.
