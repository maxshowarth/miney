from __future__ import annotations

from collections import deque
from typing import Dict, List, Tuple

from .grid import Grid, CellType


def find_first_cell(grid: Grid, cell_type: CellType) -> Tuple[int, int]:
    """Return coordinates of the first cell of the given type."""
    for y in range(grid.HEIGHT):
        for x in range(grid.WIDTH):
            if grid.get_cell(x, y).type == cell_type:
                return x, y
    raise ValueError(f"Cell type {cell_type} not found")


def bfs_path(grid: Grid, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Simple BFS to find a path restricted to road/load/dump cells."""
    allowed = {CellType.ROAD, CellType.LOAD, CellType.DUMP}
    queue: deque[Tuple[int, int]] = deque([start])
    came_from: Dict[Tuple[int, int], Tuple[int, int] | None] = {start: None}
    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not grid.in_bounds(nx, ny):
                continue
            cell = grid.get_cell(nx, ny)
            if cell.type in allowed and (nx, ny) not in came_from:
                came_from[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    else:
        raise ValueError("No path found between points")

    path: List[Tuple[int, int]] = []
    current: Tuple[int, int] | None = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


def compute_loop_route(grid: Grid) -> Tuple[List[Tuple[int, int]], int]:
    """Compute a route from load -> dump -> load using BFS.

    Returns the full route and the index of the dump cell within that route.
    """
    start = find_first_cell(grid, CellType.LOAD)
    dump = find_first_cell(grid, CellType.DUMP)
    to_dump = bfs_path(grid, start, dump)
    route = to_dump + to_dump[-2::-1]
    dump_index = len(to_dump) - 1
    return route, dump_index
