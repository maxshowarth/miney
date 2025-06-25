from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class CellType(str, Enum):
    """Types of cells in the grid."""

    EMPTY = "empty"
    ROAD = "road"
    LOAD = "load"
    DUMP = "dump"
    OBSTACLE = "obstacle"


@dataclass
class Cell:
    """A single cell in the grid."""

    type: CellType = CellType.EMPTY


class Grid:
    """Representation of the mine as a 2D grid."""

    WIDTH: int = 50
    HEIGHT: int = 50

    def __init__(self) -> None:
        self._cells: List[List[Cell]] = [
            [Cell() for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)
        ]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.WIDTH and 0 <= y < self.HEIGHT

    def get_cell(self, x: int, y: int) -> Cell:
        if not self.in_bounds(x, y):
            raise IndexError("Coordinates out of bounds")
        return self._cells[y][x]

    def set_cell_type(self, x: int, y: int, cell_type: CellType) -> None:
        if not self.in_bounds(x, y):
            raise IndexError("Coordinates out of bounds")
        self._cells[y][x].type = cell_type

    def reset(self) -> None:
        for row in self._cells:
            for cell in row:
                cell.type = CellType.EMPTY
