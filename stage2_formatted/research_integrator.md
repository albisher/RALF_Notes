**Tags:** #research-integration, #markdown-processing, #story-generation, #data-parsing, #file-handling
**Created:** 2026-01-13
**Type:** documentation-research

# research_integrator

## Summary

```
Handles loading, editing, and integrating research files into narrative prompts via Markdown parsing.
```

## Details

> The `ResearchIntegratorBox` class processes Markdown-formatted research files stored in a designated directory (`research/`). It supports three primary operations: loading research files, listing available research, and integrating research into story prompts. The system detects the project root automatically and validates file paths before parsing content. Research summaries can be edited, and the integrated prompt includes contextualized research input for AI-driven story generation.

## Key Functions

### ``execute``

Orchestrates operations based on input data (load, integrate, or list research).

### ``_load_research``

Reads and validates a research file, extracts metadata, and returns parsed content.

### ``_integrate_research``

Combines loaded research with user-provided context to generate an enhanced prompt.

### ``_list_research``

Scans the `research/` directory for `.md` files prefixed with `research_` and returns metadata.

### ``_parse_research_markdown``

(Inferred) Extracts structured data (e.g., title, summary, query) from Markdown content.

## Usage

1. **Initialize**: Create an instance with `project_root` (optional).
2. **Load Research**: Call `execute` with `operation="load_research"` and specify `research_file` or `research_id`.
3. **Integrate**: Use `operation="integrate"` with `research_file`, `research_id`, and optional `summary_edit`/`story_context`.
4. **List Research**: Call `execute` with `operation="list_research"` to retrieve a list of available research files.

## Dependencies

> ``..core.box_interface``
> ``logging``
> ``typing``
> ``os``

## Related

- [[research_markdown_parser]]
- [[core_box_interface]]

>[!INFO] Automatic Root Detection
> The class auto-detects the project root using `_detect_project_root()` if `project_root` is not provided.

>[!WARNING] File Validation
> If a file path is invalid or missing, the system returns a `success=False` response with an error message. Always validate `research_file`/`research_id` before integration.
