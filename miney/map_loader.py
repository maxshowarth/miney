import json
from pathlib import Path

from .grid import Grid, CellType


def load_grid(path: str | Path) -> Grid:
    """Load a grid configuration from a JSON file."""
    grid = Grid()
    path = Path(path)
    data = json.loads(path.read_text())

    for x, y in data.get("roads", []):
        grid.set_cell_type(x, y, CellType.ROAD)
    if "load" in data:
        x, y = data["load"]
        grid.set_cell_type(x, y, CellType.LOAD)
    if "dump" in data:
        x, y = data["dump"]
        grid.set_cell_type(x, y, CellType.DUMP)
    for x, y in data.get("obstacles", []):
        grid.set_cell_type(x, y, CellType.OBSTACLE)
    return grid
