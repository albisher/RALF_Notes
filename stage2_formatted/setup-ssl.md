**Tags:** #SSL, #Nginx, #Certbot, #Web-Security, #Bash-Scripting
**Created:** 2026-01-13
**Type:** code-notes

# setup-ssl

## Summary

```
Automates SSL certificate generation and Nginx HTTPS configuration for web projects.
```

## Details

> This script automates the setup of SSL certificates (self-signed for development) and configures Nginx to enforce HTTPS. It includes directory creation, permission management, and generates a secure Nginx SSL configuration with best-practice security headers. The script supports both self-signed certificates and integrates with Certbot for automated Let’s Encrypt certificate issuance (though self-signed is used here for development).

## Key Functions

### `check_root`

Validates if the script is run as root.

### `create_ssl_directories`

Creates and secures SSL-related directories (`nginx/ssl` and `certbot`).

### `generate_self_signed_certificates`

Produces a self-signed TLS certificate and key for local development.

### `create_enhanced_nginx_ssl_config`

Generates a secure Nginx SSL configuration with HTTPS enforcement, ACME challenge support, and security headers.

## Usage

1. Run as root (`sudo ./setup-ssl.sh`).
2. Set `DOMAIN_NAME` (defaults to `localhost`).
3. For development: Script generates self-signed certs in `nginx/ssl/`.
4. For production: Replace self-signed certs with Let’s Encrypt certificates from Certbot.

## Dependencies

> `OpenSSL`
> `Nginx`
> `Certbot (optional for production)`
> `Bash.`

## Related

- [[Space Pearl Project Documentation]]
- [[Nginx SSL Configuration Guide]]

>[!INFO] Important Note
> This script uses self-signed certificates for development. In production, replace these with certificates from a trusted CA (e.g., Let’s Encrypt) and ensure proper domain validation.

>[!WARNING] Caution
> Running as non-root may fail due to permission restrictions for SSL key files. Always validate Nginx configuration after running this script.
