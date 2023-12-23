from camera import camera
from bodies import sun, earth, mars, mercury, venus, jupiter, bodies
from physics import new_positions, update_positions
from display import screen, pygame, draw, scale
from constants import AU
from interactions import is_hitbox

running: bool = True
pause = False

speed = 12

hours = 0

origin = sun

clock = pygame.time.Clock()

while running:
    time_lapse = f"Time since beginning of simulation: {hours // 8760} years {(hours % 8760) // 24} " \
                 f"days {hours % 24} hours"

    clock.tick(60)
    screen.fill((0, 0, 0))

    if not pause:
        for i in range(speed):
            new_positions()
            update_positions()
           # print(time_lapse)
        hours += int(speed)

    if camera.get_time() != 0:
        print("smoothing")
        camera.smoother(origin)
        draw(scale / AU)
    else:
        print("not smoothing")
        camera.set_target(origin)
        draw(scale / AU)

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
            if event.key == pygame.K_RIGHT and speed < 182:
                speed += 1
            if event.key == pygame.K_LEFT and speed > 1:
                speed -= 1
            if event.key == pygame.K_RETURN:
                origin = sun
                camera.time = 1
            if event.key == pygame.K_j:
                origin = jupiter
                camera.time = 1
            if event.key == pygame.K_e:
                origin = earth
                camera.time = 1
            if event.key == pygame.K_a:
                origin = mars
                camera.time = 1
            if event.key == pygame.K_m:
                origin = mercury
                camera.time = 1
            if event.key == pygame.K_v:
                origin = venus
                camera.time = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                for body in bodies:
                    if body != origin:
                        if is_hitbox(body, x, y, scale):
                            origin = body
                            camera.time = 1

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
