from miney.grid import CellType
from miney.pygame_ui import cell_color
from miney.ui import CELL_COLORS, hex_to_rgb


def test_cell_color_matches_ui_mapping():
    assert cell_color(CellType.LOAD) == hex_to_rgb(CELL_COLORS[CellType.LOAD])
