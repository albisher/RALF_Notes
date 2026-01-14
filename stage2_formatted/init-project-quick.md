**Tags:** #bash-script, #project-initialization, #automation, #task-management
**Created:** 2026-01-13
**Type:** code-notes

# init-project-quick

## Summary

```
A script for rapid task management project setup with auto-confirmation.
```

## Details

> This script automates the initialization of a Task Master project by creating a `.taskmaster/` directory structure, setting up a default `tasks.json`, and applying predefined configurations without user interaction. It leverages environment variables for model configurations and uses the current directory name as the project identifier.

## Key Functions

### ``task-master init -y``

Initializes a Task Master project with auto-confirmation, skipping all prompts.

### `Directory Structure Creation`

Automatically generates `.taskmaster/` with nested subdirectories for configurations and tasks.

### `Default Configuration Setup`

Applies predefined defaults (e.g., project name, description, task structure) based on environment variables and directory naming.

### `Post-Initialization Commands`

Provides suggested next steps for AI model setup, PRD parsing, or task creation.

## Usage

Run the script via:
```bash
task-master init -y
```
Follow up with recommended commands (e.g., model setup, task creation) in the next steps section.

## Dependencies

> ``task-master` CLI tool (Task Master project framework)`
> ``bash` shell.`

## Related

- [[setup`]]
- [[parse-prd <file>`]]
- [[add-task create initial setup`]]

>[!INFO] **Auto-Confirmation**
> The `-y` flag skips all interactive prompts, making it ideal for CI/CD pipelines or rapid prototyping.

>[!WARNING] **Environment Dependency**
> Model configurations rely on existing environment variables; ensure they match expected defaults to avoid errors.
