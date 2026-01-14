**Tags:** #security-validation, #network-isolation, #docker-validation, #port-mapping
**Created:** 2026-01-13
**Type:** code-script

# validate-port-mappings

## Summary

```
Validates port mappings, security configurations, and network isolation for a Dockerized application stack.
```

## Details

> This script checks Docker Compose port mappings to ensure internal services (e.g., PostgreSQL, Redis) are not exposed externally, verifies network isolation via internal networks and proxy configurations, and validates Nginx proxy setups. It uses `bash` with color-coded output to log validation results, including warnings for missing files or misconfigurations. The script also tests port accessibility (e.g., `localhost:5174`) against predefined rules (e.g., frontend ports should be open, internal ports should be blocked).

## Key Functions

### `print_status`

Displays colored status messages (INFO, SUCCESS, WARNING, ERROR) for validation steps.

### `test_port`

Checks if a specified port is open/blocked on `localhost` using `timeout` and `bash -c`.

### `validate_docker_compose_ports`

Scans `docker-compose.yml` for exposed ports, checks against `INTERNAL_PORTS`, and validates a security override file.

### `validate_network_isolation`

Ensures Docker Compose includes internal networks, network aliases, and proper proxy networking configurations.

### `validate_nginx_config`

Verifies Nginx config files exist and contain upstream/proxy_pass directives.

## Usage

1. Run the script from the project root:
   ```bash
   ./validate-port-mappings.sh
   ```
2. It checks:
   - Docker Compose port mappings (exposed ports, internal services).
   - Network isolation (internal networks, proxy configs).
   - Nginx proxy configurations.
3. Outputs colored logs with success/error/warnings.

## Dependencies

> ``bash``
> ``grep``
> ``timeout``
> ``awk` (for parsing `docker-compose.yml`/`nginx.conf`).`

## Related

- [[Space Pearl Project Docker Setup]]
- [[Security Configuration Guide]]

>[!INFO] Important Note
> The script assumes `docker-compose.yml` and `nginx/default.conf` exist in the project root. Missing files trigger errors.

>[!WARNING] Caution
> Hardcoded ports (`FRONTEND_PORT`, `INTERNAL_PORTS`) may need updates if the application’s port assignments change.
