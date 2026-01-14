**Tags:** #markdown, #file-system, #research-management, #project-structure, #logging, #hashing
**Created:** 2026-01-13
**Type:** documentation-research

# research_storage

## Summary

```
Stores research results in a structured Markdown file within a project directory.
```

## Details

> This `ResearchStorageBox` class handles saving research outputs (e.g., AI-generated findings) to a project’s `research/` folder. It validates input data (e.g., `research_text`, `summary`, `query`) and formats it as Markdown with a timestamp-based filename. The system detects the project root automatically via common indicators (e.g., `README.md`) or defaults to the current working directory. A SHA-256 hash of the topic ensures uniqueness in filenames, while sanitization prevents invalid characters. Errors are logged via `logging` and returned as a `BoxOutput` failure.

## Key Functions

### ``execute(input_data`

BoxInput)`**: Processes input data, validates requirements, generates a Markdown file, and returns metadata (file path, hash, content).

### ``_detect_project_root()``

Recursively locates the project root by checking for file indicators (e.g., `package.json`, `.git`) up to 10 levels above the current file.

### ``__init__(project_root`

Optional[str])`**: Initializes the storage path (defaults to auto-detection) and creates the `research/` directory if missing.

## Usage

1. **Initialize**: Pass a `project_root` (optional) or let it auto-detect.
2. **Call `execute()`**: Provide a `BoxInput` with required fields (`research_text`, `summary`, `query`).
3. **Retrieve Results**: The output includes the saved file path, hash, and formatted Markdown content.

## Dependencies

> ``os``
> ``logging``
> ``datetime``
> ``hashlib``
> ``Box``
> ``BoxInput``
> ``BoxOutput` (from `..core.box_interface`).`

## Related

- [[research_management_system]]
- [[project_structure_guide]]

>[!INFO] Auto-Detection Limitation
> If no project indicators are found, it defaults to the current working directory. For monorepos, ensure common files (e.g., `package.json`) exist in the root.

>[!WARNING] Sanitization Edge Case
> The topic sanitization truncates to 50 chars and replaces invalid characters with underscores. Overly long topics may still cause filename collisions (mitigated by the SHA-256 hash).
