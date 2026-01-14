**Tags:** #archived-components, #ui-design, #legacy-code
**Created:** 2026-01-13
**Type:** documentation

# ARCHIVE_README

## Summary

```
Documentation for archived UI components removed from the current `index.html` implementation.
```

## Details

> This README explains why UI components in the `components/` directory were removed and how they were integrated into the current `index.html` file. The components were loaded via `<script>` tags but never utilized, as all functionality is now implemented inline. The `index.html` contains a self-contained Vue.js application with embedded styles and API client logic.

## Key Functions

### ``components/` directory`

Contains archived UI components (e.g., `boxes.js`, `link-box.js`) that were loaded but unused.

### ``index.html``

Self-contained Vue.js app with inline logic, styles, and API integration.

## Usage

- **Future Reuse**: If components are needed again, move them back to `ui-beta/components/` and uncomment `<script>` tags in `index.html`.

## Dependencies

> `none (components were standalone`
> `now fully embedded in `index.html`)`

## Related

- [[components]]
- [[timeline-story-workflow-v7]]

>[!INFO] Component Integration
> Components were loaded via `<script>` tags but never referenced in `index.html`, indicating they were never actively used.

>[!WARNING] Inline Migration
> All functionality was migrated inline to avoid external dependencies, reducing maintenance overhead.
