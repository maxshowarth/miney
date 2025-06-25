from __future__ import annotations

from typing import List

import streamlit as st

from .grid import Grid, CellType


CELL_COLORS = {
    CellType.EMPTY: "#FFFFFF",
    CellType.ROAD: "#A0A0A0",
    CellType.LOAD: "#00FF00",
    CellType.DUMP: "#FF0000",
    CellType.OBSTACLE: "#000000",
}


def grid_to_color_matrix(grid: Grid) -> List[List[str]]:
    """Return a color representation of the grid."""
    matrix: List[List[str]] = []
    for y in range(grid.HEIGHT):
        row = []
        for x in range(grid.WIDTH):
            row.append(CELL_COLORS[grid.get_cell(x, y).type])
        matrix.append(row)
    return matrix


def render_grid(grid: Grid) -> None:
    """Render the grid using Streamlit."""
    matrix = grid_to_color_matrix(grid)
    for row in matrix:
        cols = st.columns(len(row))
        for col, color in zip(cols, row):
            col.button(" ", key=f"cell-{col}-{color}", help=color, disabled=True)
