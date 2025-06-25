from __future__ import annotations

import pygame
from pygame.surface import Surface

from .grid import Grid, CellType
from .simulation import Simulation
from .map_loader import load_grid
from .ui import CELL_COLORS, TRUCK_COLOR, hex_to_rgb

CELL_SIZE = 10
INFO_HEIGHT = 30


def cell_color(cell_type: CellType) -> tuple[int, int, int]:
    """Return the RGB color for a grid cell."""
    return hex_to_rgb(CELL_COLORS[cell_type])


def draw_grid(surface: Surface, grid: Grid) -> None:
    for y in range(grid.HEIGHT):
        for x in range(grid.WIDTH):
            color = cell_color(grid.get_cell(x, y).type)
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            surface.fill(color, rect)


def draw_trucks(surface: Surface, sim: Simulation) -> None:
    color = hex_to_rgb(TRUCK_COLOR)
    for truck in sim.trucks:
        x, y = truck.position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        surface.fill(color, rect)


def main() -> None:
    pygame.init()
    grid = load_grid("maps/simple_map.json")
    sim = Simulation(grid)
    width = grid.WIDTH * CELL_SIZE
    height = grid.HEIGHT * CELL_SIZE + INFO_HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Miney - Truck Simulator")
    font = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if sim.running:
                        sim.stop()
                    else:
                        sim.start()
                elif event.key == pygame.K_r:
                    sim.reset()
                elif event.key == pygame.K_a:
                    sim.add_truck()

        if sim.running:
            sim.step()

        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        draw_trucks(screen, sim)
        info_text = f"SPACE Start/Stop | R Reset | A Add Truck | Trucks: {len(sim.trucks)}"
        text_surf = font.render(info_text, True, (255, 255, 255))
        screen.blit(text_surf, (5, grid.HEIGHT * CELL_SIZE + 5))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
