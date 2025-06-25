from miney.map_loader import load_grid
from miney.grid import CellType


def test_load_grid():
    grid = load_grid('maps/simple_map.json')
    assert grid.get_cell(0, 25).type == CellType.LOAD
    assert grid.get_cell(49, 25).type == CellType.DUMP
    for x in range(50):
        assert grid.get_cell(x, 25).type in {CellType.ROAD, CellType.LOAD, CellType.DUMP}
