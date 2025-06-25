import numpy as np
from miney.map_loader import load_grid
from miney.simulation import Simulation
from miney.ui import simulation_to_rgb_array, TRUCK_COLOR, hex_to_rgb


def test_simulation_array_overlays_truck():
    grid = load_grid('maps/simple_map.json')
    sim = Simulation(grid, load_delay=1, dump_delay=1)
    truck = sim.add_truck()
    arr = simulation_to_rgb_array(sim, cell_size=1)
    x, y = truck.position
    assert tuple(arr[y, x]) == hex_to_rgb(TRUCK_COLOR)
