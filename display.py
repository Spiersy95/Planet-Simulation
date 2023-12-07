import pygame
from bodies import bodies
from camera import camera

WIDTH, HEIGHT = 900, 900
scale = 200

screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption('Planets in Motion')


def draw_bodies(scale):
    for body in bodies:
        x = body.x * scale + WIDTH // 2 - camera.x * scale
        y = body.y * scale + HEIGHT // 2 - camera.y * scale
        pygame.draw.circle(screen, body.get_colour(), (x, y), body.get_radius())


def draw_arcs(scale):
    for body in bodies:
        for (x1, y1), (x2, y2) in zip(body.arc, body.arc[1:]):
            x1 = int(x1 * scale + WIDTH // 2 - scale * camera.x)
            y1 = int(y1 * scale + HEIGHT // 2 - camera.y * scale)
            x2 = int(x2 * scale + WIDTH // 2 - scale * camera.x)
            y2 = int(y2 * scale + HEIGHT // 2 - camera.y * scale)
            pygame.draw.line(screen, (100, 100, 0), (x1, y1), (x2, y2))


def draw(scale):
    draw_arcs(scale)
    draw_bodies(scale)
