**Tags:** #Bash-Script, #Web-Security, #SSL-Certificates, #Nginx-Configuration, #Certbot
**Created:** 2026-01-13
**Type:** code-notes

# setup-ssl-simple

## Summary

```
Automates SSL certificate generation and Nginx HTTPS configuration for web servers.
```

## Details

> This script automates the setup of SSL certificates (self-signed for development) and configures Nginx to enforce HTTPS. It includes directory creation, permission management, and generates a secure Nginx SSL configuration with TLS 1.2/1.3, modern cipher suites, and security headers. The script also handles ACME challenges for automated Let’s Encrypt certificate issuance (though self-signed here) and redirects HTTP traffic to HTTPS. It uses a placeholder `frontend`/`backend` proxy setup for web app routing.

## Key Functions

### `check_root`

Validates if the script is run as root.

### `create_ssl_directories`

Creates and secures SSL directories (`/nginx/ssl` and `/certbot`).

### `generate_self_signed_certificates`

Produces a self-signed TLS certificate and key for local development.

### `create_enhanced_nginx_ssl_config`

Generates a hardened Nginx SSL config with TLS 1.2/1.3, HSTS, and security headers.

### `print_status`

Color-coded logging for script progress/error messages.

## Usage

1. Run as root: `sudo ./setup-ssl-simple.sh`.
2. Set `DOMAIN_NAME` (e.g., `DOMAIN_NAME="example.com"`).
3. For production, replace self-signed certs with Let’s Encrypt via Certbot’s ACME challenge (handled in the HTTP 80 port).
4. Apply the generated Nginx config to `/etc/nginx/sites-available/` or similar.

## Dependencies

> ``openssl``
> ``certbot` (for ACME challenges)`
> ``nginx``
> ``Bash`.`

## Related

- [[Space Pearl Project Documentation]]
- [[Nginx SSL Best Practices Guide]]

>[!INFO] Important Note
> This script uses self-signed certificates for development. In production, replace them with Let’s Encrypt certificates via Certbot’s ACME challenge (e.g., `certbot nginx --webroot=/var/www/certbot`). The script includes an ACME challenge directory (`/certbot/www`) for this purpose.


>[!WARNING] Caution
> - **Permissions**: The script enforces restrictive permissions (e.g., `600` for keys). Ensure Nginx runs with the correct user (`www-data` or equivalent) and has access to the SSL directories.
> - **Backup**: The Nginx config is backed up with a timestamp (`default.conf.backup.YYYYMMDD_HHMMSS`). Overwrite at your own risk.
> - **TLS**: The config enforces TLS 1.2/1.3. Disable older protocols (e.g., TLS 1.0/1.1) in production to mitigate vulnerabilities.
