**Tags:** #naming-standard, #docker-migration, #simulator-refactoring, #documentation-update
**Created:** 2026-01-13
**Type:** documentation

# 0009-container-rename-complete

## Summary

```
Tracks completion of renaming the container from `quadcopter-simulator` to `hmrs-simulator` for clarity and accuracy.
```

## Details

> This document records the migration process of updating all references to the container name from `quadcopter-simulator` to `hmrs-simulator` to better reflect its broader functionality as a **Heterogeneous Multi-Robot System (HMRS)** simulator. The change ensures consistency across configuration files, documentation, and scripts while maintaining backward compatibility via a migration plan.

## Key Functions

### ``docker-compose.yml``

Updated container name to `hmrs-simulator`.

### ``run_live.sh``

Modified to use `docker compose run --rm simulator` instead of the old container name.

### ``0013-hmrs-simulator-tasks.md``

Renamed from `QUADCOPTER_SIMULATOR_TASKS.md` and updated content to reflect HMRS scope.

### ``0008-container-rename-plan.md``

Maintained old name for reference during migration.

## Usage

This file serves as a record of completed renaming tasks. To verify the change:
1. Check `docker compose ps` to confirm the container is named `hmrs-simulator`.
2. Run `docker compose run --rm simulator python verify_requirements.py` to test functionality.
3. Ensure no old references remain (e.g., `quadcopter-simulator` should only appear in `0008-container-rename-plan.md`).

## Dependencies

> `None (internal documentation and file updates only).`

## Related

- [[0008-container-rename-plan]]
- [[docker-compose]]

>[!INFO] Key Purpose
> The new name `hmrs-simulator` accurately describes the simulator’s support for diverse drone types (e.g., quadcopters, octocopters, fixed-wing), not just quadcopters.

>[!WARNING] Backward Compatibility
> Old references (e.g., `quadcopter-simulator`) are preserved in `0008-container-rename-plan.md` for reference but should not be used in production.
