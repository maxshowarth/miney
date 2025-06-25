from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple


class TruckState(str, Enum):
    """Possible states for a truck."""

    IDLE = "idle"
    LOADING = "loading"
    HAULING = "hauling"
    DUMPING = "dumping"
    RETURNING = "returning"


@dataclass
class Truck:
    """A haul truck moving along a predefined route."""

    id: int
    route: List[Tuple[int, int]]
    dump_index: int
    load_delay: int = 3
    dump_delay: int = 3
    position: Tuple[int, int] = field(init=False)
    state: TruckState = field(init=False)
    _route_index: int = field(init=False, default=0)
    _wait_timer: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        self.position = self.route[0]
        self.state = TruckState.LOADING
        self._route_index = 0
        self._wait_timer = self.load_delay

    def step(self) -> None:
        """Advance the truck by one simulation tick."""
        if self.state == TruckState.LOADING:
            if self._wait_timer > 0:
                self._wait_timer -= 1
                return
            self.state = TruckState.HAULING
            self._route_index = 1

        if self.state == TruckState.DUMPING:
            if self._wait_timer > 0:
                self._wait_timer -= 1
                return
            self.state = TruckState.RETURNING
            self._route_index += 1

        if self.state in (TruckState.HAULING, TruckState.RETURNING):
            self.position = self.route[self._route_index]
            self._route_index += 1
            if self.state == TruckState.HAULING and self._route_index - 1 == self.dump_index:
                self.state = TruckState.DUMPING
                self._wait_timer = self.dump_delay
            elif self.state == TruckState.RETURNING and self._route_index == len(self.route):
                self.state = TruckState.LOADING
                self._wait_timer = self.load_delay
                self._route_index = 1
                self.position = self.route[0]
