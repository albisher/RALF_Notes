**Tags:** #docker, #networking, #dns, #multi-network, #isolation, #security
**Created:** 2026-01-13
**Type:** documentation

# network-architecture

## Summary

```
Defines a Docker-based multi-network architecture for secure container communication with custom DNS aliases.
```

## Details

> This document outlines a **multi-network Docker setup** for the Space Pearl tool stack, featuring isolated networks (`space-pearl-public`, `space-pearl-app`, `space-pearl-data`, `space-pearl-tools`) for secure internal communication. Each network uses a **bridge driver**, with `public` accessible from the host and others isolated. **DNS aliases** (e.g., `frontend`, `backend`) replace hardcoded IPs, ensuring stability and reducing dependency on IP changes. Services communicate via these aliases (e.g., `backend → db:5432`), while external access is restricted to minimal ports (`8080`, `8443`, `5173`). Security is enforced via **network isolation**, **proxy routing**, and **DNS-based resolution**, preventing direct host access to internal services.

## Key Functions

### ``space-pearl-public``

Host-accessible services (frontend, proxy, certbot).

### ``space-pearl-app``

Internal app communication (backend, proxy).

### ``space-pearl-data``

Database/cache isolation (db, cache, backend).

### ``space-pearl-tools``

External tool services (openproject, n8n, continue).

### `DNS aliases`

Resolve service names (e.g., `backend-db-client`) for container-to-container communication.

### `Proxy (`proxy` service)`

Routes traffic securely via Nginx.

## Usage

1. Deploy containers using `docker-compose` with the specified networks.
2. Use DNS aliases (e.g., `docker exec -it <container> ping backend`) for internal communication.
3. Expose only required ports (`8080`, `8443`) externally via the proxy.
4. Validate configurations with `./scripts/validate-network-aliases.sh`.

## Dependencies

> `docker`
> `docker-compose`
> `docker network plugins (bridge driver)`
> `DNS resolver (host system).`

## Related

- [[docker-compose]]
- [[network-troubleshooting-guide]]
- [[security-policy]]

>[!INFO] **Network Isolation**
> Internal networks (`app`, `data`, `tools`) are isolated from the host, requiring containers to communicate via DNS aliases (e.g., `backend → db`). This prevents unauthorized host access to services like databases or caches.


>[!WARNING] **Port Exposure**
> Only ports `8080`, `8443`, and `5173` are exposed to the host. Misconfiguration here could expose internal services. Always validate with `validate-network-aliases.sh` before deployment.
