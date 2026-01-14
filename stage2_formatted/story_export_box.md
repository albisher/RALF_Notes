**Tags:** #data-processing, #export-format, #markdown, #html, #json, #text-generation
**Created:** 2026-01-13
**Type:** code-notes

# story_export_box

## Summary

```
Handles conversion of story data into JSON, Markdown, or HTML formats for export.
```

## Details

> The `StoryExportBox` class extends the `Box` interface to provide functionality for exporting structured story data into different formats. It processes an input containing a story object and a specified format (JSON, Markdown, or HTML), then converts it into the corresponding string representation. The core logic involves validating the input, applying the appropriate conversion method, and returning the result with metadata (mime type, extension, and format). Helper methods `_toMarkdown` and `_toHTML` format the story elements into Markdown and HTML structures, respectively.

## Key Functions

### ``constructor()``

Initializes the box with metadata (version, dependencies, input/output schemas).

### ``_executeInternal(inputData)``

Core execution method that routes the story to the correct format conversion based on the input.

### ``_toMarkdown(story)``

Converts story elements into Markdown-formatted text with headers for each page.

### ``_toHTML(story)``

Converts story elements into HTML with structured page divs and titles.

## Usage

1. Instantiate `StoryExportBox` and pass a story object with `title`, `elements` (array of pages), and `page_number` (optional).
2. Call `_executeInternal` with an input containing `operation`, `story`, and `format` (e.g., `'markdown'`).
3. Output includes `content` (formatted string), `mimeType`, `extension`, and `format`.

## Dependencies

> ``../core/box_interface.js` (Box class and related utilities like `BoxOutput``
> ``BoxErrorCode``
> ``BoxErrorCategory`).`

## Related

- [[None]]

>[!INFO] Input Validation
> The input schema enforces `story` as a required object and `format` as one of `['json', 'markdown', 'html']`. Missing or invalid fields trigger validation errors.

>[!WARNING] Error Handling
> Uncaught exceptions during conversion (e.g., malformed story data) propagate as `EXECUTION_FAILED` errors, preserving the original error object.
