**Tags:** #PostgreSQL, #Docker, #Backup, #Bash, #Database
**Created:** 2026-01-13
**Type:** code-notes

# backup-databases

## Summary

```
Automates PostgreSQL database backup using Docker and timestamped SQL dumps.
```

## Details

> This script performs a full backup of PostgreSQL databases running in a Docker container (`space-pearl-db`). It uses `pg_dumpall` to export all databases, redirects output to a file with a timestamped name (`backup_YYYYMMDD_HHMMSS.sql`), and logs completion. The backup relies on Docker’s `exec` command to interact with the container.

## Key Functions

### ``docker exec space-pearl-db pg_dumpall``

Runs `pg_dumpall` inside the container to dump all PostgreSQL databases.

### ``> backup_$(date +%Y%m%d_%H%M%S).sql``

Redirects output to a file with a timestamped filename.

## Usage

1. Save the script as `backup-databases`.
2. Make it executable: `chmod +x backup-databases`.
3. Run it: `./backup-databases`.

## Dependencies

> `Docker`
> `PostgreSQL client tools (`pg_dumpall`)`
> `and the container `space-pearl-db` must be running.`

## Related

- [[none]]

>[!INFO] Important Note
> Ensure the PostgreSQL user (`postgres`) has permissions to dump databases. If authentication fails, verify credentials or container environment.

>[!WARNING] Caution
> The script overwrites existing backups with the same timestamp. Consider rotating backups or adding a backup directory (e.g., `backup_$(date +%Y%m%d)/`).
