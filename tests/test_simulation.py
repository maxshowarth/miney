from miney.map_loader import load_grid
from miney.simulation import Simulation
from miney.truck import TruckState


def test_add_truck_ids_unique():
    grid = load_grid('maps/simple_map.json')
    sim = Simulation(grid, load_delay=1, dump_delay=1)
    t1 = sim.add_truck()
    t2 = sim.add_truck()
    assert t1.id == 1
    assert t2.id == 2
    assert t1.position == sim.route[0]


def test_truck_complete_cycle():
    grid = load_grid('maps/simple_map.json')
    sim = Simulation(grid, load_delay=1, dump_delay=1)
    truck = sim.add_truck()
    sim.start()
    steps = len(sim.route)
    for _ in range(steps):
        sim.step()
    assert truck.position == sim.route[0]
    assert truck.state == TruckState.LOADING
