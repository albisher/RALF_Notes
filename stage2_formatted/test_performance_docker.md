**Tags:** #docker, #performance-test, #bash-script, #automation, #testing
**Created:** 2026-01-13
**Type:** code-notes

# test_performance_docker

## Summary

```
Script automates performance testing inside Docker containers for initialization and step execution.
```

## Details

> This Bash script orchestrates performance testing within a Docker environment. It executes three phases: an initialization speed test (3 runs), a step performance test (1000 steps with 3 drones), and generates a full report without API calls. The script leverages a Python module (`test_performance.py`) for execution, with conditional flags (`--init-only`, `--step-only`, `--no-api`) to control test execution.

## Key Functions

### `test_performance_docker`

Orchestrates the entire testing workflow in Docker.

### ``python test_performance.py --init-only``

Runs initialization speed tests (3 iterations).

### ``python test_performance.py --step-only``

Executes step performance tests (1000 steps, 3 drones).

### ``python test_performance.py --no-api``

Generates a report without API dependencies.

## Usage

1. Build and run a Docker container with the script’s dependencies.
2. Execute the script directly:
   ```bash
   ./test_performance_docker
   ```
3. Monitor output for test phases and final report.

## Dependencies

> `python3`
> `Docker`
> ``test_performance.py` (custom script)`

## Related

- [[none]]

>[!INFO] Important Note
> Ensure the Docker container has `python3` and the `test_performance.py` script installed before running. The script assumes the container has network access to execute tests.

>[!WARNING] Caution
> The `--step-only` flag may consume significant resources (1000 steps × 3 drones). Test in a controlled environment to avoid overloading systems.
