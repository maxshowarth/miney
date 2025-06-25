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
From the repository root, launch the editor interface with:

```bash
streamlit run app.py
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
