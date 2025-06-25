# Miney

Miney is a toy simulation of haul trucks moving on a 50x50 grid. The current codebase contains the grid model and a basic Streamlit UI for editing the grid.
See `PROJECT_REQUIREMENTS.md` for the full project specification.

## Requirements
- Python 3.10+
- [Streamlit](https://streamlit.io)
- [pytest](https://docs.pytest.org/) (for running tests)

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

## Testing
Run unit tests with:

```bash
pytest -q
```
