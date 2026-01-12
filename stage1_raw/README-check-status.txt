### FILENAME
check_system_status

### TAGS
#system-monitoring, #cli-tool, #health-check, #docker, #webapp-status

### TYPE
code-notes

### SUMMARY
Tool checks real-time status of a web application, APIs, and Docker containers for operational health.

### DETAILS
This script provides a command-line interface to monitor the health of a web application system, including API status, simulation time, drone/building counts, Docker container statuses, and overall system state. It aggregates data from multiple sources (APIs, Docker, and internal state tracking) into a structured output, highlighting operational statuses and potential issues.

The script uses Python to interact with system APIs and Docker containers, displaying formatted results in a user-friendly console output. It includes a quick summary of system health and directs users to detailed logs for further inspection.

### KEY_FUNCTIONS
- **`check_system_status.py`**: Main script that orchestrates API, Docker, and system state checks.
- **API Health Check**: Retrieves and displays API status, running state, and simulation time.
- **System State Check**: Collects drone count, building count, mission state, and session status.
- **Docker Container Inspection**: Lists and verifies the status of all Docker containers in the system.

### DEPENDENCIES
Python 3, Docker CLI, HTTP requests library (likely `requests` or similar for API calls).

### USAGE
1. Navigate to the project directory containing `scripts/check_system_status.py`.
2. Run the script directly with `python3 scripts/check_system_status.py`.
3. For convenience, add an alias in your shell config (e.g., `.bashrc` or `.zshrc`) to simplify execution:
   ```bash
   alias check-status='cd /path/to/project && python3 scripts/check_system_status.py'
   ```
4. Execute the alias or script to generate a formatted status report.

### RELATED
[[System Architecture Docs]], [[Docker Configuration Guide]]

### CALLOUTS
>[!INFO]- Important Note
> The script assumes Docker is running and accessible from the current environment. Ensure Docker containers are properly started before execution.
>[!WARNING]- Caution
> If the API is not responding, the script may display misleading "ok" statuses for API health. Verify API availability manually if issues persist.