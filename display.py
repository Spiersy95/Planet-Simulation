import pygame
from bodies import bodies

WIDTH, HEIGHT = 900, 900

screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption('Planets in Motion')

scale = 200


def draw_bodies(camera, scale):
    for body in bodies:
        x = body.get_x() * scale + WIDTH // 2 - camera.get_x() * scale
        y = body.get_y() * scale + HEIGHT // 2 - camera.get_y() * scale
        pygame.draw.circle(screen, body.get_colour(), (x, y), body.get_radius())


def draw_arcs(camera, scale):
    for body in bodies:
        for i in range(len(body.arc) - 1):
            pygame.draw.line(screen, (100, 100, 0), (body.arc[i][0] * scale + WIDTH // 2 - scale * camera.get_x(),
                                                     body.arc[i][1] * scale + HEIGHT // 2 - camera.get_y() * scale),
                             (body.arc[i + 1][0] * scale + WIDTH // 2 - scale * camera.get_x(),
                              body.arc[i + 1][1] * scale + HEIGHT // 2 - camera.get_y() * scale))
