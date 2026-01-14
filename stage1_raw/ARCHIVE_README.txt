### TAGS
#archived-components
#ui-design
#legacy-code

### TYPE
documentation

### SUMMARY
Documentation for archived UI components removed from the current `index.html` implementation.

### DETAILS
This README explains why UI components in the `components/` directory were removed and how they were integrated into the current `index.html` file. The components were loaded via `<script>` tags but never utilized, as all functionality is now implemented inline. The `index.html` contains a self-contained Vue.js application with embedded styles and API client logic.

### KEY_FUNCTIONS
- **`components/` directory**: Contains archived UI components (e.g., `boxes.js`, `link-box.js`) that were loaded but unused.
- **`index.html`**: Self-contained Vue.js app with inline logic, styles, and API integration.

### DEPENDENCIES
none (components were standalone, now fully embedded in `index.html`)

### USAGE
- **Future Reuse**: If components are needed again, move them back to `ui-beta/components/` and uncomment `<script>` tags in `index.html`.

### RELATED
[[ui-beta/components]], [[ui-explorations/iterations/iteration-10/mockups/timeline-story-workflow-v7.html]]

### CALLOUTS
>[!INFO]- Component Integration
> Components were loaded via `<script>` tags but never referenced in `index.html`, indicating they were never actively used.
>[!WARNING]- Inline Migration
> All functionality was migrated inline to avoid external dependencies, reducing maintenance overhead.