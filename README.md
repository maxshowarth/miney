# Miney

Miney is a toy simulation of haul trucks moving on a 50x50 grid. The application currently displays a predefined map with a single road, load zone and dump zone.
See `PROJECT_REQUIREMENTS.md` for the full project specification.

## Requirements
The project requires Python 3.10 or newer and the following packages:

- [Streamlit](https://streamlit.io)
- [pytest](https://docs.pytest.org/)
- [NumPy](https://numpy.org/) (math utilities)
- [NetworkX](https://networkx.org/) (future pathfinding)
- [PyYAML](https://pyyaml.org/) (configuration files)

## Setup
Create and activate a virtual environment, then install the dependencies listed
in `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the app
From the repository root, launch the editor interface in development mode so
changes are picked up automatically:

```bash
streamlit run app.py --server.runOnSave=true
```

If everything is working you should see a 50x50 grid rendered as a single
image, not a matrix of buttons. A grey road runs across the middle row with a
green cell at the far left (the load zone) and a red cell at the far right (the
dump zone). The layout is loaded from `maps/simple_map.json` and can be replaced
with other map files.

## Testing
Run unit tests with:

```bash
pytest -q
```

## Simulation
The `miney.simulation` module contains a simple truck engine. Trucks follow a
pre-computed looped route from the load cell to the dump cell and back again.
Each truck waits for a configurable number of ticks at the load and dump
locations before continuing its journey.

## Project Details
This project involves developing a Python-based, interactive 2D mine simulation application. The app models haul trucks moving between a loading ground and dumping ground on a user-defined road network within a 50×50 grid. The simulation will be visualized in a Streamlit or Gradio interface and allow basic controls (start, reset, add trucks). Truck motion is governed by pathfinding logic. This tool is intended for demonstration purposes and educational use.

The agent is expected to break the project into appropriately sized tasks and implement them incrementally, submitting changes as a series of pull requests. Each PR must include comprehensive unit tests and should be reviewable from a TDD perspective. Tasks should follow a test-driven development strategy: define the tests, then implement the functionality, and finally verify that all tests pass.

📦 Technical Constraints
Language: Python 3.10+

UI Framework: Streamlit (preferred) or Gradio for 2D visualization and interactivity

Visualization: Grid-based (50x50); click-and-drag interface to define roads

Pathfinding: A* or Dijkstra’s algorithm

Tests: pytest (recommended)

Modularity: Code must be organized and extensible (e.g., future support for underground mines or real telemetry)

📋 Functional Requirements
1. Map Representation
Represent the mine as a 50×50 2D grid.

Each cell has a type:

"empty" – unused terrain

"road" – drivable area

"load" – loading station (1 cell only in v1)

"dump" – dumping station (1 cell only in v1)

"obstacle" – non-drivable terrain

Provide an interface to click and drag cells to mark them as "road".

Loading and dumping locations should be user-selectable from the grid.

2. Truck Simulation
Each truck must be an object with the following properties:

id – unique identifier

position – (x, y) grid coordinates

state – one of ["idle", "loading", "hauling", "dumping", "returning"]

route – list of waypoints from load → dump → load

Trucks should:

Spawn at the load point

Follow the computed path to the dump point

Wait a few seconds (configurable) at load/dump

Loop their route indefinitely

Initial version supports 1 loading and 1 dumping cell only.

3. Pathfinding
Use A* algorithm to determine a path from load → dump → load.

Path must avoid obstacles and remain only on "road" cells.

Must recalculate path if road network changes mid-simulation.

4. Simulation Controls
UI must support:

Start simulation

Reset grid and trucks

Add truck (starts at load zone)

Optionally display truck ID and state

Trucks update position once per simulation tick (e.g., 500ms or configurable)

5. Configuration
Simulation parameters (tick rate, number of trucks, load/dump delay) configurable via a config.yaml or JSON file.

6. Visualization
The UI must show:

Grid with clearly color-coded cell types

Trucks moving in real time

Optional overlays: truck IDs, states, route paths

Framework: Use Streamlit unless otherwise directed

✅ Non-Functional Requirements
No internet connection should be required after install.

Designed to run on a standard laptop (no GPU required).

Code must be modular and testable.

Pathfinding, simulation, UI, and config should be separate modules.

🧪 Test Strategy
Unit tests must be included for:

Grid and cell logic

Pathfinding algorithm (A*)

Truck lifecycle and state transitions

UI component functions (mocking Streamlit as needed)

All PRs must pass tests before merge.

TDD: Tests should be written before or alongside the implementation.

PRs without tests will be rejected.

🔀 Development Process Instructions for Codex
Break the project down into multiple self-contained units of work. Each unit should be implemented in a separate pull request.

Each PR should contain relevant code, tests, and documentation (as needed).

PRs should be no larger than necessary and logically scoped (e.g., one PR for grid logic, another for truck logic, etc.)

Use test-driven development. Each feature should be introduced alongside its tests. You may implement tests first (TDD style) or concurrently.

Ensure each PR passes all tests before considering the task complete.

Consider this a production codebase:

Use idiomatic Python

Include type hints

Write clear docstrings

Follow PEP8 standards

Suggested PR breakdown (flexible):

PR #1: Grid model with road/obstacle/load/dump types and click/drag UI for editing

PR #2: Truck entity and basic simulation engine (without pathfinding)

PR #3: A* pathfinding module and routing engine

PR #4: Integrate truck motion using pathfinding logic

PR #5: Add UI controls (start, reset, add truck)

PR #6: Add configuration management (config file support)

PR #7: Add overlays (truck ID, state)

PR #8: Polish UI and refactor code

PR #9+: Add full unit test coverage where not yet implemented
