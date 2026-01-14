### TAGS
#markdown
#task-management
#README-generation
#automation
#documentation
#sprint-tracking

### TYPE
documentation

### SUMMARY
Generates a professionally formatted README.md from task data with customizable filters and visual elements.

### DETAILS
This script exports task information into a structured README.md file, incorporating project metadata, task statuses, priorities, and subtasks. It dynamically formats sections like "Project Header," "Task Sections," and "Visual Elements" based on provided arguments (e.g., `--pending`, `--with-subtasks`). The output includes progress bars, status badges, and GitHub-flavored markdown for clarity. It supports intelligent grouping by feature, sprint, or priority and provides post-sync features like diff preview and backup.

### KEY_FUNCTIONS
- **`sync-readme`**: Core function to generate/update README.md with task data.
- **`argument parsing`**: Filters tasks by status (`pending`), subtasks, priority, or sprint.
- **`README header generation`**: Creates a dynamic project summary with task counts and progress percentages.
- **`task section formatting`**: Organizes tasks into status-based or priority-based sections with visual indicators.
- **`visual enhancements`**: Adds progress bars, badges, and checkboxes for readability.
- **`custom grouping`**: Supports grouping by feature, sprint, developer, or priority.
- **`post-sync utilities`**: Includes diff preview, backup, and commit reminders.

### DEPENDENCIES
`task-master` (core CLI tool), GitHub-flavored markdown parser (built-in), Bash scripting (for argument handling).

### USAGE
Run via CLI:
```bash
task-master sync-readme [--with-subtasks] [--status=<pending|in-progress|completed>] [--by-priority]
```
Example:
```bash
task-master sync-readme --pending --with-subtasks
```
Outputs a formatted README.md with pending tasks and subtask details.

### RELATED
[[`task-master` documentation]], [[`GitHub README best practices`]], [[`Agile sprint templates`]]

### CALLOUTS
>[!INFO]- **Dynamic Updates**
> Automatically updates the README.md timestamp (`Last Updated`) with the current date/time after generation.
>
>[!WARNING]- **Backup Required**
> The script suggests backing up the existing README.md before overwriting to avoid data loss. Always verify the diff preview before committing.