**Tags:** #password-generation, #security-tools, #bash-scripting, #environment-configuration, #openssl
**Created:** 2026-01-13
**Type:** code-script

# generate-secure-passwords

## Summary

```
Generates secure passwords and secret keys for a software project using OpenSSL, then creates a `.env` file for deployment.
```

## Details

> This script leverages OpenSSL to produce cryptographically strong passwords and keys (32–64 characters) for various security-sensitive components (JWT, databases, API keys). It dynamically constructs a `.env` file with placeholder values for sensitive credentials, enforces strict file permissions (`600`), and provides colored feedback via `print_status()`. The script checks for OpenSSL availability and exits with an error if missing. It also includes security warnings about secure storage and rotation.

## Key Functions

### ``print_status()``

Displays colored status messages (SUCCESS, ERROR, WARNING, INFO).

### ``generate_password()``

Creates a 32-character password using `openssl rand -base64` (filtered to exclude `=+/`).

### ``generate_secret_key()``

Generates a 64-character hexadecimal key with `openssl rand -hex`.

### ``.env file creation`

Populates environment variables for JWT, databases (PostgreSQL/OpenProject/n8n), and APIs with auto-filled secrets.

## Usage

1. Run the script in a terminal:
   ```bash
   chmod +x generate-secure-passwords.sh
   ./generate-secure-passwords.sh
   ```
2. Copy the generated `.env` file into your project directory.
3. Replace placeholder API keys (`your-perplexity-api-key-here`) with actual values.
4. Use the script in CI/CD pipelines or deployment workflows.

## Dependencies

> ``openssl``
> ``bash` (standard libraries)`
> ``date` (for timestamp in `.env`).`

## Related

- [[Security Best Practices for Environment Variables]]
- [[OpenSSL Usage Guide]]
- [[Docker Secrets Documentation]]

>[!INFO] Important Note
> **Never commit `.env` to version control**—it contains all generated secrets. Use `.gitignore` to exclude it.
>

>[!WARNING] Caution
> **Test passwords in a staging environment** before production deployment. Rotate keys periodically to mitigate risk.
