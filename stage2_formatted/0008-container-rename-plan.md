**Tags:** #rename, #simulator, #docker, #documentation, #multi-robot, #drone, #system-update
**Created:** 2026-01-13
**Type:** documentation

# 0008-container-rename-plan

## Summary

```
Documentation outlining the rename of a container from `quadcopter-simulator` to `hmrs-simulator` to reflect broader drone support.
```

## Details

> This document details the rationale and steps for renaming the container from `quadcopter-simulator` to `hmrs-simulator`. The original name was misleading because the HMRS (Heterogeneous Multi-Robot System) simulation supports multiple drone types, including quadcopters, hexacopters, octocopters, and others. The update includes renaming the container and updating associated documentation files to reflect the broader scope of the simulation system.

## Key Functions

### `Container Renaming`

Updates the Docker container name from `quadcopter-simulator` to `hmrs-simulator`.

### `Documentation Updates`

Ensures all references to the old name are removed and replaced with the new name across multiple files.

### `Task File Renaming`

Renaming `QUADCOPTER_SIMULATOR_TASKS.md` to `HMRS_SIMULATOR_TASKS.md`.

## Usage

1. **Rename Container**: Update the `docker-compose.yml` file to reflect the new container name.
2. **Update Documentation**: Review and replace all instances of `quadcopter-simulator` with `hmrs-simulator` in the listed files.
3. **Rename Task File**: Update the filename from `QUADCOPTER_SIMULATOR_TASKS.md` to `HMRS_SIMULATOR_TASKS.md`.

## Dependencies

> `- Docker Compose (`docker-compose.yml`)
- Scripts (`run_live.sh`)
- Multiple documentation files in `README.md``
> ``docs/docker/``
> `and `docs/guides/``

## Related

- [[0013-hmrs-simulator-tasks]]
- [[0001-docker-readme]]

>[!INFO] Important Note
> The rename is part of a broader effort to accurately reflect the HMRS system’s support for multiple drone types, not just quadcopters. Ensure all references are updated consistently across documentation and scripts to avoid confusion.


>[!WARNING] Caution
> Double-check all references in documentation files to avoid incomplete updates. Inconsistent naming could lead to confusion during system operation or documentation review.
