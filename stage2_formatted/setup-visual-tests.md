**Tags:** #Bash-Script, #Visual-Testing, #CI/CD-Setup, #Web-App-Testing, #Docker-Integration
**Created:** 2026-01-13
**Type:** code-notes

# setup-visual-tests

## Summary

```
Script to validate and prepare a web application environment for visual testing using Node.js, Docker, and npm.
```

## Details

> This script performs a series of checks and setup tasks to ensure a web application is ready for visual testing. It verifies Node.js installation and version, installs project dependencies, checks Docker container status, and creates directories for test outputs. The script also includes health checks for the web application to confirm it is operational before proceeding.

## Key Functions

### `Node.js version check`

Validates Node.js version meets the requirement (v16+).

### `Dependency installation`

Runs `npm install` to install project dependencies.

### `Docker container management`

Checks if Docker containers are running, starts them if needed, and waits for the web app to be ready via a health endpoint.

### `Directory creation`

Creates `test-screenshots` and `test-reports` directories for storing test artifacts.

### `Test execution guidance`

Provides instructions for running visual tests in different modes (visible browser, headless, CI/CD).

## Usage

1. Run the script in the project root directory:
   ```bash
   chmod +x setup-visual-tests
   ./setup-visual-tests
   ```
2. After setup, execute visual tests using:
   ```bash
   npm test                  # Interactive mode
   npm run test:headless     # Headless mode
   npm run test:ci          # CI/CD mode
   ```
3. Test outputs (screenshots/reports) will be saved in `./test-screenshots/` and `./test-reports/`.

## Dependencies

> ``node``
> ``npm``
> ``docker``
> ``docker-compose``

## Related

- [[Visual Testing Framework Documentation]]
- [[CD Guide]]

>[!INFO] Important Note
> This script assumes the web app is running on `http://localhost:8080`. If the endpoint differs, modify the `curl` health check URL accordingly.


>[!WARNING] Caution
> If Docker is not running, the script will attempt to start containers. Ensure Docker is installed and accessible before execution.
