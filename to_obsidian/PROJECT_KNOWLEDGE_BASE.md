# PROJECT_KNOWLEDGE_BASE

RAW MODEL OUTPUT (JSON error):

```text
The Window Cleanner simulation platform is a comprehensive system designed for window cleaning drone operations, featuring a modular architecture with 43 box components, 4 drone types, and 56 API endpoints. Here's a concise summary of its key aspects:

### Core Features:
1. **Modular Architecture**:
   - **43 Box Components**: Each handles specific functions (e.g., sensor processing, path planning, weather simulation).
   - **Box System**: Enables easy integration of new functionalities without disrupting existing code.

2. **Drone Types**:
   - **Scout**: Maps buildings and gathers data.
   - **Overseer**: Manages cleaning operations and ensures safety.
   - **Tanker-Mule**: Delivers cleaning materials and equipment.
   - **Tanker-Lifeline**: Provides support and emergency services.

3. **Simulation Environment**:
   - **Dockerized Architecture**: Uses 4 containers (frontend, backend, database, simulator).
   - **Real-Time Visualization**: Frontend (Vue.js) provides interactive 3D simulation.
   - **Session Persistence**: Uses PostgreSQL for saving simulation states.

4. **API Endpoints**:
   - **56 Endpoints**: Enable programmatic control of drones and simulation.
   - **RESTful + Socket.IO**: Supports both RESTful requests and real-time updates.

5. **Vendor Agnostic Design**:
   - **Base Vendor Adapter**: Abstracts vendor-specific logic, allowing integration with different drone systems.

### Workflow Example:
1. **Setup**: Spawn drones and configure the simulation environment.
2. **Mapping**: Scout drones map buildings and collect data.
3. **Cleaning**: Overseer drones manage cleaning operations.
4. **Quality Assurance**: Overseer drones ensure the cleaning meets standards.
5. **Completion**: Tanker drones deliver materials and support.

### Known Issues:
- **LoggingBox Parameter Mismatch**: A minor bug causing HTTP 500 errors for some API commands, but non-critical as commands still execute.
- **Docker Desktop Requirement**: Must be running to start containers.

### Quick Start:
1. Start Docker Desktop.
2. Run containers:
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```
3. Access the web interface at `http://localhost:5007`.

### Documentation:
- **Quick Start Guide**: `analysis/0001-get-simulation-running-now.md`
- **Mission Workflow**: `analysis/0002-window-cleaning-mission-workflow.md`
- **Vendor Onboarding**: `analysis/0003-vendor-onboarding-tutorial.md`
- **System Validation**: `analysis/0005-system-validation-results.md`

This system is well-structured for testing and simulating window cleaning operations, with a focus on modularity and extensibility.
```