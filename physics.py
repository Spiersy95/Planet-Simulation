from bodies import *
import math
from constants import G
from constants import TIMESTEP


def acceleration(body, other):
    if body == other:
        return 0, 0
    distance_x = body.x - other.x
    distance_y = body.y - other.y
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    theta = math.atan2(distance_y, distance_x)

    acceleration = -G * other.mass / distance ** 2
    acceleration_x = acceleration * math.cos(theta)
    acceleration_y = acceleration * math.sin(theta)

    return acceleration_x, acceleration_y


def new_positions():
    for body in bodies:
        total_ax = total_ay = 0
        for other in bodies:
            ax, ay = acceleration(body, other)
            total_ax += ax
            total_ay += ay

        body.vel_x += total_ax * TIMESTEP
        body.vel_y += total_ay * TIMESTEP

        body.new_x = body.x + body.vel_x * TIMESTEP
        body.new_y = body.y + body.vel_y * TIMESTEP


def update_positions():
    for body in bodies:
        body.x = body.new_x
        body.y = body.new_y

        if len(body.arc) > 10000:
            body.arc.pop(0)
            body.arc.append([body.x, body.y])
        else:
            body.arc.append([body.x, body.y])
