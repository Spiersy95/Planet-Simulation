import pygame_widgets
from physics import *
from display import *

running: bool = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()

    new_positions()
    update_positions()
    correction()
    draw_bodies(slider.getValue() / AU)
    draw_arcs(slider.getValue() / AU)
    events = pygame.event.get()

    pygame_widgets.update(events)

    pygame.display.update()
