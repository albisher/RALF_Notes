**Tags:** #Nginx, #SSL/TLS, #Certbot, #Docker, #ReverseProxy, #SecurityHeaders, #CORS, #ACMEChallenge, #AutomaticRenewal
**Created:** 2026-01-14
**Type:** documentation

# ssl_nginx_certbot_implementation

## Summary

```
Implements SSL/TLS encryption for a Space Pearl application using Nginx and Certbot for secure HTTPS termination and certificate management.
```

## Details

> This implementation secures the application via Nginx as a reverse proxy, enforcing HTTPS with automatic certificate renewal via Certbot. It includes development and production workflows, Docker integration, and comprehensive security headers. The setup involves self-signed certificates for local testing and Let’s Encrypt certificates for production, with automated renewal and challenge validation.

## Key Functions

### ``scripts/setup-ssl.sh``

Configures SSL for either development or production environments, generating certificates or using templates.

### ``scripts/init-ssl.sh``

Initializes Let’s Encrypt certificates by running Certbot with a webroot plugin for domain validation.

### ``nginx/nginx.conf``

Main Nginx configuration file defining upstream services, logging, and performance optimizations.

### ``nginx/default.conf.template``

Production-ready template for domain-specific SSL/TLS configurations.

### ``nginx/default.conf``

Dynamically generated server block for HTTPS termination and security headers.

### ``scripts/renew-ssl.sh``

Automates certificate renewal and reloads Nginx post-successful renewal.

### ``scripts/generate-dev-certs.sh``

Creates self-signed certificates for local development with 365-day validity.

### ``scripts/test-ssl.sh``

Validates SSL/TLS functionality, redirects, security headers, and API endpoints.

## Usage

1. **Development**:
   - Run `./scripts/setup-ssl.sh development` to generate self-signed certs.
   - Start containers with `docker-compose up -d`.
   - Access via `https://localhost:8443` (HTTPS) or `http://localhost:8080` (redirects).

2. **Production**:
   - Configure domain in `setup-ssl.sh` and run `./scripts/init-ssl.sh <domain> <email>`.
   - Certificates auto-renew every 12 hours via `renew-ssl.sh`.

## Dependencies

> ``certbot/certbot:latest``
> `Docker Compose`
> `Nginx`
> `OpenSSL`
> `Let’s Encrypt ACME API.`

## Related

- [[Nginx SSL Configuration Guide]]
- [[Certbot Best Practices]]
- [[TLS Setup]]

>[!INFO] **Development Certs**
> Self-signed certificates are valid for 365 days and include `localhost`/`127.0.0.1` in SAN for local testing. Avoid trusting these in production.


>[!WARNING] **Webroot Plugin**
> Certbot’s webroot plugin requires files in `/certbot/www/` matching ACME challenges. Ensure this directory is writable by the Certbot container.
