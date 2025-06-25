# Project Requirements

This document summarizes the key requirements for the Miney simulation.

## Technical Constraints
- **Language**: Python 3.10+
- **UI**: Streamlit (preferred) or Gradio
- **Visualization**: 50x50 grid
- **Pathfinding**: A* algorithm
- **Tests**: pytest

## Functional Requirements
1. **Map Representation**
   - Grid with cell types: empty, road, load, dump, obstacle.
   - User can draw roads and select load/dump cells.
2. **Truck Simulation**
   - Trucks have an ID, position, state, and route.
   - Spawn at the load point and move between load and dump.
3. **Pathfinding**
   - Use A* to compute routes avoiding obstacles.
   - Recalculate paths if the road network changes.
4. **Simulation Controls**
   - Start, reset, and add trucks via the UI.
5. **Configuration**
   - Tick rate and delays should be configurable via a file.
6. **Visualization**
   - Display grid with colored cells and moving trucks.

These requirements are a condensed version of the instructions provided during project setup and should guide future development.
