**Tags:** #validation, #docker, #configuration-check, #json-validation, #api-testing
**Created:** 2026-01-13
**Type:** code-script

# validate-continue

## Summary

```
Validates the configuration and operational state of a **Continue** container and its supporting files.
```

## Details

> This script performs a multi-step validation of the **Continue** system by:
> 1. Checking if the **Continue** Docker container is running.
> 2. Validating required configuration files (JSON-based) for syntax correctness.
> 3. Ensuring critical environment variables (`PERPLEXITY_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) are set.
> 4. Testing API endpoint accessibility via `curl`.

## Key Functions

### ``docker ps | grep "space-pearl-continue"``

Checks if the Continue container is running.

### ``jq . "$file"``

Validates JSON syntax in config files (`.continue/*-config.json`).

### ``curl -s http`

//localhost:8080/health`**: Tests API endpoint health.

### `Environment variable checks (`-n "${!var}"`)`

Verifies required env vars are set.

## Usage

Run in a shell to validate:
```bash
./validate-continue
```
Outputs status checks (✅/❌/⚠️) for each validation step.

## Dependencies

> ``docker``
> ``jq``
> ``curl``

## Related

- [[none]]

>[!INFO] Important Note
> **`jq` must be installed** for JSON validation. Install via `apt install jq` (Debian/Ubuntu) or `brew install jq` (macOS).

>[!WARNING] Caution
> **Docker must be running** before executing this script. If the container is missing, the script will prompt to start it with `docker-compose up continue`.
