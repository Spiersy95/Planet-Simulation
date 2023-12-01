import pygame
from pygame_widgets.slider import Slider
from bodies import *


WIDTH, HEIGHT = 900, 900

screen = pygame.display.set_mode((HEIGHT, WIDTH))

slider = Slider(screen, 100, 100, 200, 20, min=1, max=300, step=5)

pygame.display.set_caption('Planets in Motion')


def draw_bodies(scale):
    for body in bodies:
        x = body.x * scale + WIDTH // 2
        y = body.y * scale + HEIGHT // 2
        pygame.draw.circle(screen, body.colour, (x, y), body.radius)


def correction():
    if sun.x != 0 or sun.y != 0:
        for body in bodies:
            body.x -= sun.x
            body.y -= sun.y


def draw_arcs(scale):
    for body in bodies:
        for i in range(len(body.arc) - 1):
            pygame.draw.line(screen, (100, 100, 0), (body.arc[i][0] * scale + WIDTH//2, body.arc[i][1] * scale + HEIGHT//2),
                             (body.arc[i+1][0] * scale + WIDTH//2, body.arc[i+1][1] * scale + HEIGHT//2))
