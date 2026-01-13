**Tags:** #file-organization, #scenario-management, #directory-structure, #test-reorganization
**Created:** 2026-01-13
**Type:** documentation

# REORGANIZATION_SUMMARY

## Summary

```
Document summarizing the reorganization of scenario-related files into a structured `/scenarios/` directory.
```

## Details

> This document outlines the reorganization of all scenario files into a centralized `/scenarios/` directory, divided into subdirectories like `exploration/` and `production/`. The process included moving existing files, updating paths in Python scripts, and creating new documentation (e.g., READMEs) to reflect the new structure. Legacy locations may still contain old files, which can be cleaned up later.

## Key Functions

### `README.md`

Main catalog and prioritization guide for the reorganized scenarios.

### `exploration/README.md`

Documentation for exploration test scenarios.

### `production/README.md`

Documentation for production test scenarios.

### `production/reconnaissance-mapping/README.md`

Subdirectory for reconnaissance-mapping tests.

### `documentation/README.md`

Directory for scenario documentation files.

## Usage

1. **Run Scenarios**: Execute scripts from the project root using updated paths (e.g., `python scenarios/exploration/simple_exploration_test.py`).
2. **Documentation**: Refer to `README.md` files in each subdirectory for setup and usage instructions.
3. **Cleanup**: Review legacy locations (`/simulation/scripts/scenarios/`, `/assessment/tests/scenarios/`) for old files if needed.

## Dependencies

> `- Python scripts (`simple_exploration_test.py``
> ``autonomous_exploration_test.py``
> `etc.)
- Docker (for containerized environment updates)
- Assumptions of existing test frameworks and logging systems`

## Related

- [[None]]

>[!INFO] Important Note
> All active scenario files are now centralized in `/scenarios/`. Legacy files in `/simulation/scripts/scenarios/` and `/assessment/tests/scenarios/` may still exist but are not actively maintained.


>[!WARNING] Caution
> Ensure all Docker paths and import statements are updated in Python files to avoid runtime errors. Verify log file paths in visualization scripts match the new directory structure.
