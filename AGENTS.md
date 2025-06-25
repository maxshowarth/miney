# Agent Instructions

This repository contains a small Streamlit application and accompanying tests. Follow these rules when making changes:

- **Testing**: Always run `pytest -q` and ensure it succeeds before committing.
- **Python Version**: Use Python 3.10 or newer.
- **Grid Size**: The grid should remain 50x50 unless future requirements say otherwise.
- **UI Framework**: Streamlit is used for the UI. Tests may mock Streamlit where necessary.
- **Modularity**: Keep code modular and add unit tests for new functionality.
- **Running the App**: Use `streamlit run app.py` from the repository root to start the interface.
- **Dependencies**: Install Python packages from `requirements.txt`.

Document any user-facing changes in the README when appropriate.
