from camera import camera
from bodies import sun, earth, mars, mercury, venus, jupiter, bodies
from physics import new_positions, update_positions
from display import screen, pygame, draw, scale
from constants import AU
from interactions import is_hitbox

running = True
pause = False
speed = 12
hours = 0
origin = sun
clock = pygame.time.Clock()

def handle_input():
    global scale, speed, origin
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            elif event.key == pygame.K_UP and scale + 20 <= 400:
                scale += 20
            elif event.key == pygame.K_DOWN and scale - 20 >= 20:
                scale -= 20
            elif event.key == pygame.K_RIGHT and speed < 182:
                speed += 1
            elif event.key == pygame.K_LEFT and speed > 1:
                speed -= 1
            elif event.key == pygame.K_RETURN:
                origin = sun
                camera.set_time(1)
            elif event.key == pygame.K_j:
                origin = jupiter
                camera.set_time(1)
            elif event.key == pygame.K_e:
                origin = earth
                camera.set_time(1)
            elif event.key == pygame.K_a:
                origin = mars
                camera.set_time(1)
            elif event.key == pygame.K_m:
                origin = mercury
                camera.set_time(1)
            elif event.key == pygame.K_v:
                origin = venus
                camera.set_time(1)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                for body in bodies:
                    if body != origin and is_hitbox(body, x, y):
                        origin = body
                        camera.set_time(1)

        elif event.type == pygame.QUIT:
            global running
            running = False

while running:
    time_lapse = f"Time since beginning of simulation: {hours // 8760} years {(hours % 8760) // 24} " \
                 f"days {hours % 24} hours"

    clock.tick(60)
    screen.fill((0, 0, 0))

    if not pause:
        for _ in range(speed):
            new_positions()
            update_positions()
            print(time_lapse)
        hours += int(speed)

    if camera.get_time != 0:
        camera.smoother(origin)
        draw(scale / AU)
    else:
        camera.set_target(origin)
        draw(scale / AU)

    handle_input()
    pygame.display.flip()
