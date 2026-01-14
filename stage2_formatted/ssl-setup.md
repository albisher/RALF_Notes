**Tags:** #SSL, #TLS, #Nginx, #Certbot, #ReverseProxy, #Security, #Docker, #Automation
**Created:** 2026-01-13
**Type:** documentation

# ssl-setup

## Summary

```
Configures SSL/TLS termination for Space Pearl application using Nginx and Certbot for secure HTTPS deployment.
```

## Details

> This document outlines the SSL/TLS setup for the Space Pearl application, leveraging Nginx as a reverse proxy with SSL termination and Certbot for automated certificate management via Let’s Encrypt. The system supports both development (self-signed certificates) and production (Let’s Encrypt) environments. Certificates are renewed automatically every 12 hours, with Nginx reloaded post-renewal to maintain security. Security headers and CORS policies are enforced to mitigate common web vulnerabilities.

## Key Functions

### ``nginx/nginx.conf``

Main Nginx configuration file defining SSL termination and routing rules.

### ``nginx/default.conf``

Server block for SSL termination, auto-generated from a template.

### ``certbot/certbot`

latest`**: Docker container managing Let’s Encrypt certificates via ACME challenges.

### ``scripts/setup-ssl.sh``

Script to generate SSL certificates (self-signed for dev, Let’s Encrypt for prod).

### ``scripts/init-ssl.sh``

Initializes Let’s Encrypt certificates with domain validation.

### ``scripts/renew-ssl.sh``

Renews certificates and reloads Nginx for production.

### ``scripts/generate-dev-certs.sh``

Creates self-signed certificates for development.

### ``scripts/test-ssl.sh``

Validates SSL configuration and certificate integrity.

## Usage

1. **Development**:
   - Run `./scripts/setup-ssl.sh development` to generate self-signed certs.
   - Start services with `docker-compose up -d`; access via `https://localhost:8443`.

2. **Production**:
   - Run `./scripts/setup-ssl.sh production <domain>` to configure Certbot.
   - Initialize certs with `./scripts/init-ssl.sh <domain> <email>`.
   - Start services and ensure HTTPS is enforced.

## Dependencies

> `Docker`
> `Docker Compose`
> `Nginx`
> `Certbot`
> `Let’s Encrypt`
> `Python (for Certbot).`

## Related

- [[Space Pearl Architecture]]
- [[Nginx SSL Guide]]
- [[Certbot Best Practices]]

>[!INFO] **Certificate Auto-Renewal**
> Certificates are renewed every 12 hours via `certbot renew --force-renewal` and trigger an Nginx reload to maintain HTTPS availability.


>[!WARNING] **Self-Signed Certs in Dev**
> Development uses self-signed certificates; users may encounter browser warnings. Test with `-k` flag in `curl` to bypass validation.
