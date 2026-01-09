# test_output

RAW MODEL OUTPUT (JSON error):

```text
The provided document is a comprehensive knowledge base for the WindowCleanner simulation platform. Here's a structured summary of its key aspects:

---

### **Core Architecture**
1. **Docker Setup**:
   - 4 containers: frontend, backend, database, simulator.
   - Uses `docker-compose.yml` for orchestration.
   - **Critical**: Docker Desktop must be running (`open -a "Docker Desktop"`).

2. **Backend**:
   - **Main Server**: `hmrs_simulation_live.py` (handles all API routes).
   - **Language**: Python 3.10+.
   - **Key Features**:
     - RESTful API endpoints (56 total).
     - Session persistence via PostgreSQL.
     - Master controller (`master_coordinator.py`) for drone coordination.

3. **Frontend**:
   - **Framework**: Vue.js 3 (no CLI, direct file serving).
   - **Key Files**:
     - `frontend/app-data.js` (main logic).
     - `frontend/app-component.js` (Vue.js components).
   - **Visualization**: 3D/2D plots via `plot-2d-box.js`/`plot-3d-box.js`.

---

### **Drone Types**
- **Scout**: Mapping drones.
- **Overseer**: Quality control.
- **Tanker-Mule**: Logistics.
- **Tanker-Lifeline**: Emergency support.
- **Factory**: `hmrs_drone_spawner.py` spawns drones.

---

### **Key Components**
- **Boxes**: 43 modular components (e.g., `advanced_lidar_box.py`, `logging_box.py`).
- **Vendor Adapters**: Abstract base (`base_vendor_adapter.py`) with concrete implementations (e.g., `dji_adapter.py`).
- **Physics**: PyBullet for simulation.

---

### **Mission Workflow**
1. **Setup**: Spawn drones and buildings.
2. **Mapping**: Scout drones scan buildings.
3. **Cleaning**: Overseer drones clean windows.
4. **QA**: Tanker-Mule drones verify results.
5. **Completion**: Tanker-Lifeline drones handle emergencies.

---

### **API Endpoints**
- **Critical**:
  - `/api/health` (check system status).
  - `/api/spawn` (spawn drones).
  - `/api/command` (control drones).
  - `/api/buildings/spawn-random` (create buildings).

---

### **Known Issues**
1. **LoggingBox Bug**: Non-critical; commands still execute despite HTTP 500 errors.
   - **Fix**: Ignore error or use web UI.

2. **JavaScript Syntax Errors**: Fixed in `frontend/app-data.js` (2026-01-02).

---

### **Quick Start**
1. **Start Containers**:
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```
2. **Access UI**: `open http://localhost:5007`.

---

### **Documentation**
- **Analysis**: `analysis/0001-get-simulation-running-now.md` (quick start).
- **Workflow**: `analysis/0002-window-cleaning-mission-workflow.md` (step-by-step).
- **Vendor Onboarding**: `analysis/0003-vendor-onboarding-tutorial.md`.

---

### **Troubleshooting**
- **Containers**: Check logs with `docker compose logs -f backend`.
- **API Issues**: Verify `/api/health` returns `"running": true`.
- **Blank Page**: Hard refresh (`Cmd+Shift+R`) or check JavaScript syntax.

---

### **Key Files**
| File                          | Purpose                                                                 |
|-------------------------------|------------------------------------------------------------------------|
| `hmrs_simulation_live.py`      | Main backend server.                                                   |
| `frontend/app-data.js`        | Frontend logic (Vue.js data/methods).                                   |
| `swarm/master_coordinator.py`  | Master controller for drone coordination.                               |
| `swarm/hmrs_drone_spawner.py`  | Drone factory.                                                          |
| `docker/docker-compose.yml`    | Container orchestration.                                               |

---

### **Success Metrics**
✅ **Operational**: All 4 containers healthy.
✅ **Functional**: Drones spawn and move.
✅ **Documented**: Clear workflows and troubleshooting guides.

---
This platform is a robust simulation environment for window cleaning drones, leveraging modular design, real-time visualization, and session persistence.
```