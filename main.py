from physics import new_positions
from physics import update_positions
from physics import AU
from display import screen
from display import pygame
from display import correction
from display import draw_bodies
from display import draw_arcs
from display import scale

running: bool = True
pause = False
speed = 5

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not pause:
                pause = True
            elif event.key == pygame.K_SPACE:
                pause = False
            if event.key == pygame.K_UP and scale + 20 <= 500:
                scale += 20
            if event.key == pygame.K_DOWN and scale - 20 >= 20:
                scale -= 20
            if event.key == pygame.K_RIGHT and speed < 12:
                speed += 1
            if event.key == pygame.K_LEFT and speed > 1:
                speed -= 1
        if event.type == pygame.QUIT:
            running = False

    if not pause:
        for i in range(speed):
            new_positions()
            update_positions()
            correction()

    draw_bodies(scale / AU)
    draw_arcs(scale / AU)

    pygame.display.update()
