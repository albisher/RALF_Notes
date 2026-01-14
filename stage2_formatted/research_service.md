**Tags:** #AI-integration, #Research-service, #Natural-language-processing, #Perplexity-API, #Context-aware
**Created:** 2026-01-13
**Type:** documentation

# research_service

## Summary

```
A modular research service that interfaces with Perplexity’s MCP to generate structured research outputs with summaries for narrative integration.
```

## Details

> The `ResearchServiceBox` class acts as a wrapper around Perplexity’s AI service, processing user queries with optional story context to produce formatted research outputs. It dynamically constructs prompts by embedding the input query and optional narrative context, then delegates execution to Perplexity’s service. The response is parsed to extract a concise summary and detailed findings, defaulting to the first paragraph if no explicit summary is found. Error handling ensures robustness for missing queries or API failures.

## Key Functions

### ``execute()``

Orchestrates the research workflow by combining input data, context, and Perplexity’s API call, then formats the response into structured outputs.

### ``__init__()``

Initializes the service with a Perplexity service dependency (defaults to `PerplexityServiceBox` if none provided).

## Usage

1. Pass a `BoxInput` object containing:
   - `query`: Required research topic.
   - Optional: `story_context`, `model`, `temperature`, `max_tokens`, `api_key`.
2. Call `execute()` to generate structured research outputs with `research_text` and `summary`.

## Dependencies

> ``PerplexityServiceBox``
> ``Box``
> ``BoxInput``
> ``BoxOutput` (from `..core.box_interface` and `..ai_services.perplexity_service`).`

## Related

- [[`PerplexityServiceBox`]]
- [[`Box`]]
- [[BoxOutput`]]

>[!INFO] Context Handling
> The service prioritizes `story_context` in the prompt, ensuring narrative relevance. If missing, it defaults to a generic research format.

>[!WARNING] Parsing Edge Cases
> If the response lacks a `SUMMARY:` marker, it truncates the first paragraph as a fallback. Overly long paragraphs may result in truncated summaries.
