**Tags:** #postgresql, #optimization, #database-configuration, #docker-compose, #bash-scripting
**Created:** 2026-01-13
**Type:** code-notes

# postgresql-optimization

## Summary

```
Automated PostgreSQL configuration script for optimizing database performance across multiple environments.
```

## Details

> This script generates optimized PostgreSQL configuration files for three distinct databases (main, OpenProject, and n8n) and creates Docker Compose overrides. It configures memory allocation, concurrency limits, write-ahead logging, and logging settings tailored to each workload. The script also includes initialization SQL scripts for creating indexes and extensions to enhance query performance.
> 
> The configurations balance performance, reliability, and resource efficiency by adjusting parameters like `shared_buffers`, `work_mem`, and `autovacuum` thresholds. It uses Docker Compose to apply these configurations dynamically.

## Key Functions

### ``print_status``

Displays colored status messages for script execution.

### ``postgresql-main.conf``

Main database configuration with high concurrency settings.

### ``postgresql-openproject.conf``

Optimized configuration for OpenProject with reduced memory allocation.

### ``postgresql-n8n.conf``

Lightweight configuration for n8n with minimal autovacuum workers.

### ``docker-compose.override.yml``

Docker Compose file applying the generated PostgreSQL configs.

### ``01-main-db-init.sql``

Initialization script for the main database (includes UUID and pg_trgm extensions).

### ``02-openproject-db-init.sql``

Initialization script for OpenProject (placeholder, incomplete).

## Usage

1. Run the script in a directory with write permissions.
2. It creates:
   - `postgresql-config/` directory with config files.
   - `docker-compose.override.yml` for Docker deployment.
   - `postgresql-config/init-scripts/` with initialization scripts.
3. Apply configurations by replacing default PostgreSQL configs in Docker containers with the generated files.

## Dependencies

> `bash`
> `Docker Compose`
> `PostgreSQL client tools`

## Related

- [[PostgreSQL Best Practices Guide]]
- [[Docker PostgreSQL Optimization]]
- [[OpenProject Database Requirements]]

>[!INFO] Important Note
> The script assumes PostgreSQL is running in Docker with the default port (5432). Adjust `listen_addresses` and `port` if using non-standard configurations.

>[!WARNING] Caution
> Changes to `max_connections` and memory settings may require manual adjustments if the system already has running databases. Test configurations in a staging environment first.
