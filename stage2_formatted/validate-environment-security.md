**Tags:** #security-validation, #environment-check, #bash-script, #docker-validation
**Created:** 2026-01-13
**Type:** documentation

# validate-environment-security

## Summary

```
Validates environment security by checking file permissions, Docker Compose configurations, and secrets directory structure.
```

## Details

> This script performs security and structural validation of an environment, focusing on:
> 1. **File permissions** (e.g., ensuring secrets are restricted to `600`).
> 2. **Docker Compose** (syntax, environment variable usage, and secrets file validation).
> 3. **Secrets directory structure** (required subdirectories and files, including API keys with placeholder tolerance).
> 4. **Placeholder checks** (flagging files with placeholder values like `CHANGE_ME` or `TODO`).
> 
> The script uses colored output (`INFO`, `SUCCESS`, `WARNING`, `ERROR`) for clarity and exits on critical failures (`set -e`).

## Key Functions

### `validate_file_permissions`

Checks if a file has the correct permissions (e.g., `600` for secrets).

### `check_for_placeholders`

Detects placeholder values (e.g., `your-placeholder-here`) in files.

### `validate_docker_compose`

Validates Docker Compose syntax, environment variable usage, and secrets configuration.

### `validate_secrets_structure`

Ensures required secrets directories/files exist and are properly secured.

## Usage

1. Run the script directly:
   ```bash
   ./validate-environment-security.sh
   ```
2. Customize paths (e.g., `secrets/` or `docker-compose.yml`) if needed.
3. Use as part of a CI/CD pipeline to enforce security checks.

## Dependencies

> ``docker-compose``
> ``stat``
> ``grep``
> `Bash built-ins (e.g.`
> ``command -v`).`

## Related

- [[environment-security-checklist]]
- [[docker-security-best-practices]]

>[!INFO] Important Note
> **API Keys**: Files under `api_keys/` are allowed to contain placeholders initially (e.g., `perplexity_api_key.txt` with `your-api-key-here`). These should be replaced before production.

>[!WARNING] Caution
> **Permissions**: Files with `600` permissions (e.g., `postgres_main_password.txt`) must **not** be readable by others. Misconfiguration could expose secrets.
