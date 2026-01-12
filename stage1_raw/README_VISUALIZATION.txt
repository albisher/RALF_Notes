### README_VISUALIZATION
README_VISUALIZATION

### TAGS
#documentation, #visualization, #simulation, #docker, #interactive-graphics, #matplotlib, #3d-plots

### TYPE
documentation

### SUMMARY
Exploration visualization guide for running simulations and generating interactive 3D plots.

### DETAILS
This `README_VISUALIZATION` provides instructions for executing a simulation in Docker, generating quad-view (Top, Side, Front, Isometric) visualizations, and enabling interactive 3D plot windows. It outlines dependencies, troubleshooting steps, and file structures for a LiDAR data exploration workflow.

### KEY_FUNCTIONS
- **`run_and_visualize.sh`**: Orchestrates simulation execution in Docker, logs copying, and visualization generation.
- **`visualize_exploration.py`**: Produces quad-view PNGs and opens interactive 3D plot windows (Top/Side/Front/Isometric).
- **`simple_exploration_test.py`**: Core simulation script for LiDAR data processing.

### DEPENDENCIES
matplotlib, PyQt5, Docker, X11 forwarding (Linux/macOS), Python 3.x

### USAGE
1. Install dependencies (`matplotlib`, `PyQt5`).
2. Run `./scenarios/exploration/run_and_visualize.sh` to execute simulation and generate visualizations.
3. Open generated PNGs and interactive 3D plots for exploration.

### RELATED
[[Dockerfile]], [[simulation_scenarios]], [[LiDAR_data_processing]]

### CALLOUTS
>[!INFO]- Interactive Plots Requirement
> Interactive 3D plots require `matplotlib` and `PyQt5` installed locally. Docker X11 forwarding is needed for Linux/macOS if running inside containers.

>[!WARNING]- X11 Forwarding Note
> On macOS, X11 forwarding is complex; prefer local installation of `matplotlib` to avoid compatibility issues.