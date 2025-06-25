from __future__ import annotations

from typing import List

from .grid import Grid
from .pathfinder import compute_loop_route
from .truck import Truck


class Simulation:
    """Manages trucks moving on a grid."""

    def __init__(self, grid: Grid, load_delay: int = 3, dump_delay: int = 3) -> None:
        self.grid = grid
        self.load_delay = load_delay
        self.dump_delay = dump_delay
        self.trucks: List[Truck] = []
        self.route, self.dump_index = compute_loop_route(grid)
        self._next_id = 1
        self.running = False

    def start(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def reset(self) -> None:
        self.trucks.clear()
        self._next_id = 1

    def add_truck(self) -> Truck:
        truck = Truck(
            id=self._next_id,
            route=self.route,
            dump_index=self.dump_index,
            load_delay=self.load_delay,
            dump_delay=self.dump_delay,
        )
        self.trucks.append(truck)
        self._next_id += 1
        return truck

    def step(self) -> None:
        if not self.running:
            return
        for truck in self.trucks:
            truck.step()
