from __future__ import annotations

from typing import List

import numpy as np
import streamlit as st

from .grid import Grid, CellType


CELL_COLORS = {
    CellType.EMPTY: "#D2B48C",
    CellType.ROAD: "#A0A0A0",
    CellType.LOAD: "#00FF00",
    CellType.DUMP: "#FF0000",
    CellType.OBSTACLE: "#000000",
}

TRUCK_COLOR = "#FFFF00"


def grid_to_color_matrix(grid: Grid) -> List[List[str]]:
    """Return a color representation of the grid."""
    matrix: List[List[str]] = []
    for y in range(grid.HEIGHT):
        row = []
        for x in range(grid.WIDTH):
            row.append(CELL_COLORS[grid.get_cell(x, y).type])
        matrix.append(row)
    return matrix


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert a hex color string to an RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def grid_to_rgb_array(grid: Grid, cell_size: int = 10) -> np.ndarray:
    """Return a scaled RGB array representing the grid."""
    arr = np.zeros((grid.HEIGHT, grid.WIDTH, 3), dtype=np.uint8)
    for y in range(grid.HEIGHT):
        for x in range(grid.WIDTH):
            arr[y, x] = hex_to_rgb(CELL_COLORS[grid.get_cell(x, y).type])
    if cell_size > 1:
        arr = np.kron(arr, np.ones((cell_size, cell_size, 1), dtype=np.uint8))
    return arr


def render_grid(grid: Grid) -> None:
    """Render the grid using Streamlit."""
    arr = grid_to_rgb_array(grid, cell_size=10)
    st.image(arr, use_container_width=True)


def simulation_to_rgb_array(sim, cell_size: int = 10) -> np.ndarray:
    """Return an RGB array representing the grid with trucks overlaid."""
    arr = grid_to_rgb_array(sim.grid, cell_size=1)
    truck_rgb = np.array(hex_to_rgb(TRUCK_COLOR), dtype=np.uint8)
    for truck in sim.trucks:
        x, y = truck.position
        if 0 <= x < sim.grid.WIDTH and 0 <= y < sim.grid.HEIGHT:
            arr[y, x] = truck_rgb
    if cell_size > 1:
        arr = np.kron(arr, np.ones((cell_size, cell_size, 1), dtype=np.uint8))
    return arr


def render_simulation(sim) -> None:
    """Render the simulation with trucks."""
    arr = simulation_to_rgb_array(sim, cell_size=10)
    st.image(arr, use_container_width=True)
