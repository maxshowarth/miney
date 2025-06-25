import pytest
from miney.grid import Grid, CellType
from miney.ui import grid_to_rgb_array, CELL_COLORS, hex_to_rgb


def test_grid_initialization():
    grid = Grid()
    assert grid.WIDTH == 50
    assert grid.HEIGHT == 50
    for y in range(grid.HEIGHT):
        for x in range(grid.WIDTH):
            assert grid.get_cell(x, y).type == CellType.EMPTY


def test_set_and_get_cell():
    grid = Grid()
    grid.set_cell_type(1, 2, CellType.ROAD)
    assert grid.get_cell(1, 2).type == CellType.ROAD


def test_out_of_bounds():
    grid = Grid()
    with pytest.raises(IndexError):
        grid.set_cell_type(100, 100, CellType.ROAD)

def test_grid_to_rgb_array():
    grid = Grid()
    grid.set_cell_type(0, 0, CellType.LOAD)
    arr = grid_to_rgb_array(grid, cell_size=1)
    assert tuple(arr[0, 0]) == hex_to_rgb(CELL_COLORS[CellType.LOAD])
    assert arr.shape[0] == grid.HEIGHT
    assert arr.shape[1] == grid.WIDTH
