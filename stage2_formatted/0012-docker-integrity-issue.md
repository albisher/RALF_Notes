**Tags:** #docker, #symlink, #compose, #integration, #troubleshooting, #linux, #desktop, #container
**Created:** 2026-01-13
**Type:** documentation

# 0012-docker-integrity-issue

## Summary

```
Documentation outlining Docker Desktop's integrity check for the `compose-bridge` symlink and steps to resolve issues affecting Docker operations.
```

## Details

> This document describes a Docker Desktop integrity issue where the `compose-bridge` symlink is incorrectly pointing to a Docker Desktop resource path instead of the expected `/usr/local/bin` location. Docker Desktop regularly validates these symlinks to ensure proper binary linking. The issue can disrupt `docker compose` commands, Docker Desktop startup, and container operations. The document provides three solutions: using Docker Desktop’s built-in repair tool, manually fixing the symlink, or reinstalling Docker Desktop. Verification steps confirm the fix’s success.

## Key Functions

### `Docker Desktop Repair`

Automatically corrects symlink issues.

### `Manual Symlink Removal`

Clears incorrect symlinks before reinstallation.

### `Docker Compose Version Check`

Validates `compose` functionality post-fix.

### `Docker Info`

Ensures the Docker daemon is operational.

## Usage

1. **Identify Issue**: Check via Docker Desktop’s integrity check or manual `ls -l /usr/local/bin/compose-bridge`.
2. **Apply Solution**: Use Repair (preferred), manual removal, or reinstallation.
3. **Verify**: Run `docker info`, `docker compose version`, and test container operations.

## Dependencies

> `Docker Desktop`
> `Docker CLI tools`
> `Linux system binaries (e.g.`
> ``rm``
> ``docker`).`

## Related

- [[0013-docker-troubleshooting]]
- [[0012-multi-container-architecture]]
- [[0010-docker-fix-verification]]

>[!INFO] Important Note
> **Symlink Validation**: Docker Desktop’s integrity checks are critical for container operations. Ignoring this issue may lead to persistent failures.
>

>[!WARNING] Caution
> **Manual Fix Risks**: Incorrect symlink removal can break Docker CLI access. Always verify before applying manual fixes.
