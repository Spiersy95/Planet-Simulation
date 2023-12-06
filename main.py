from camera import camera
from bodies import sun, earth, mars, mercury, venus
from bodies import jupiter

from physics import new_positions
from physics import update_positions
from display import screen
from display import pygame
from display import draw_bodies
from display import draw_arcs
from display import scale

from constants import AU

running: bool = True
pause = False

origin = camera.get_target()

speed = 12
hours = 0

clock = pygame.time.Clock()

while running:
    camera.set_target(origin)
    clock.tick(60)
    screen.fill((0, 0, 0))

    if not pause:
        for i in range(speed):
            new_positions()
            update_positions()

        hours += int(speed)
        print(hours)


    if camera.get_time() != 0:
        camera.smoother(origin)
        draw_arcs(camera, scale / AU)
        draw_bodies(camera, scale / AU)
    else:
        print("done smoothing")
        draw_arcs(camera, scale / AU)
        draw_bodies(camera, scale / AU)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not pause:
                pause = True
            elif event.key == pygame.K_SPACE:
                pause = False
            if event.key == pygame.K_UP and scale + 20 <= 400:
                scale += 20
            if event.key == pygame.K_DOWN and scale - 20 >= 20:
                scale -= 20
            if event.key == pygame.K_RIGHT and speed < 30:
                speed += 1
            if event.key == pygame.K_LEFT and speed > 1:
                speed -= 1
            if event.key == pygame.K_RETURN:
                origin = sun
                camera.set_time(1)
            if event.key == pygame.K_j:
                origin = jupiter
                camera.set_time(1)
            if event.key == pygame.K_e:
                origin = earth
                camera.set_time(1)
            if event.key == pygame.K_a:
                origin = mars
                camera.set_time(1)
            if event.key == pygame.K_m:
                origin = mercury
                camera.set_time(1)
            if event.key == pygame.K_v:
                origin = venus
                camera.set_time(1)

        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
