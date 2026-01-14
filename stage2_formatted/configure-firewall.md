**Tags:** #firewall, #iptables, #docker, #security, #networking
**Created:** 2026-01-13
**Type:** code-notes

# configure-firewall

## Summary

```
Script automates iptables configuration for Docker-based security and port management.
```

## Details

> This script secures a Docker environment by enforcing strict iptables rules, enabling only necessary ports (e.g., SSH, frontend dev server, proxies), and managing Docker-specific traffic. It includes backup, rule generation, application, and persistent rule management via systemd. The script prioritizes security by defaulting policies to `DROP` and enforces stateful checks for allowed traffic.

## Key Functions

### `check_root`

Validates if the script is run as root.

### `backup_rules`

Saves current iptables rules to a timestamped backup file.

### `create_firewall_rules`

Generates a configuration file (`firewall-rules.conf`) with default `iptables` rules (e.g., `INPUT/DROP`, Docker network allowlists).

### `apply_firewall_rules`

Flushes existing rules and applies the generated configuration.

### `configure_docker_firewall`

Manually adds rules for Docker bridge traffic (e.g., `docker0` interface).

### `configure_port_forwarding`

Redirects external ports (e.g., `5174`, `8080`) to internal services via NAT (`PREROUTING`).

### `configure_docker_network_security`

Drops direct access to internal services (e.g., PostgreSQL, Redis) unless routed through proxies.

### `create_firewall_service`

Creates a systemd service (`space-pearl-firewall.servi`) to persist rules after reboots.

## Usage

1. Run as root: `sudo ./configure-firewall.sh`.
2. Script:
   - Backs up existing rules.
   - Generates/configures firewall rules.
   - Applies Docker-specific rules.
   - Sets up port forwarding.
   - Enforces network security.
   - Creates a systemd service for persistence.
3. Verify with `iptables -L -n` or `iptables -t nat -L -n`.

## Dependencies

> `iptables`
> `iptables-save`
> `systemd (for persistence)`
> `Docker (for network contexts).`

## Related

- [[Space Pearl Project Docker Setup]]
- [[iptables Best Practices Guide]]

>[!INFO] Important Note
> The script assumes Docker is already running with the specified networks (`172.16.0.0/12`, `172.17.0.0/16`). Adjust `DOCKER_NETWORK`/`DOCKER_BRIDGE` if misconfigured.

>[!WARNING] Caution
> Flushing rules (`iptables -F`) permanently removes all existing rules. Ensure backups exist before running. The `systemd` service may require manual activation (`systemctl daemon-reload && systemctl enable space-pearl-firewall`).
