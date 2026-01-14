**Tags:** #Bash-Script, #SSL-Certification, #Certbot, #Docker-Compose
**Created:** 2026-01-13
**Type:** code-script

# init-ssl

## Summary

```
Automates SSL certificate setup for a domain using Certbot and Docker.
```

## Details

> This script initializes SSL certificates for a specified domain using Certbot, leveraging Docker and Docker Compose to manage the process. It validates the domain, generates certificates via a webroot challenge, and ensures proper cleanup of existing containers before proceeding. The script relies on a preconfigured proxy service to handle the HTTP challenge.

## Key Functions

### ``./init-ssl.sh <domain-name> <email>``

Entry point to validate arguments, initialize directories, and orchestrate SSL certificate generation.

### ``docker-compose down``

Stops any running containers to prevent interference.

### ``docker-compose up -d proxy``

Temporarily starts only the proxy service for the webroot challenge.

### ``docker-compose run --rm certbot certonly``

Executes Certbot to generate SSL certificates using the provided domain and email.

## Usage

1. Save the script as `init-ssl.sh`.
2. Make it executable: `chmod +x init-ssl.sh`.
3. Run it with the domain name and email: `./init-ssl.sh example.com admin@example.com`.
4. After completion, restart all services: `docker-compose up -d`.

## Dependencies

> `Docker`
> `Docker Compose`
> `Certbot (installed via `apt install certbot` or similar).`

## Related

- [[none]]

>[!INFO] Important Note
> Ensure the domain’s DNS records (A/AAAA and CNAME for `www`) point to the proxy server’s IP before running this script.

>[!WARNING] Caution
> The script stops all containers before generating certificates. If services rely on persistent data, back up critical files before execution.
