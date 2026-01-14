**Tags:** #docker-compose, #nginx, #ssl-certificates, #certbot, #lets-encrypt, #reverse-proxy, #automatic-renewal, #http-https-redirection
**Created:** 2026-01-13
**Type:** documentation

# 2025-08-17_ssl-configuration-with-certbot-in-docker-compose-n

## Summary

```
Configures SSL/TLS with Certbot in Docker Compose for Nginx reverse proxy, including automatic renewal and HTTP-to-HTTPS redirection.
```

## Details

> This document outlines a Docker Compose setup for Nginx with SSL/TLS certificates managed by Certbot (Let’s Encrypt). The solution involves:
> 1. **Adding a Certbot container** to auto-obtain and renew certificates via webroot challenge.
> 2. **Configuring Nginx** to redirect HTTP traffic to HTTPS and proxy requests securely via TLS.
> 3. **Automating renewal** with a loop in the Certbot container (every 12 hours) and optional Nginx reload post-renewal.
> 4. **Mounting shared volumes** for challenge files and certificates between containers.
> 
> The setup ensures compliance with modern security standards, including TLS 1.2/1.3 and proper certificate storage.

## Key Functions

### ``certbot` container`

Manages SSL certificate lifecycle (renewal, validation).

### ``nginx` service`

Handles HTTP-to-HTTPS redirection, SSL termination, and backend proxying.

### ``docker-compose.yml``

Orchestrates container dependencies and volume mounts.

### ``certbot renew` loop`

Automates certificate renewal before expiration.

### `Nginx reload script`

Applies updated certificates post-renewal.

## Usage

1. Place the `docker-compose.yml` snippet in your project directory.
2. Run `docker-compose up -d` to start containers.
3. Manually obtain initial certificates with `docker-compose run --rm certbot certonly`.
4. Certificates auto-renew every 12 hours; reload Nginx via `docker-compose exec proxy nginx -s reload` if needed.

## Dependencies

> ``nginx:latest``
> ``certbot/certbot:latest``
> `Docker Compose`
> `Let’s EncEncrypt API.`

## Related

- [[Docker Compose Best Practices]]
- [[Nginx SSL Configuration Guide]]
- [[Let’s Encrypt API Documentation]]

>[!INFO] Critical Challenge Files
> Nginx must serve `/var/www/certbot/.well-known/acme-challenge/` for Certbot’s HTTP-01 challenge validation. Ensure this path is mounted and writable by both containers.


>[!WARNING] Certificate Expiry
> Certificates expire every 90 days. While Certbot auto-renews, monitor renewal logs (`docker-compose logs certbot`) to detect failures. Test HTTPS access post-renewal.
