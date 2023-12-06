from bodies import bodies
import math
from constants import G
from constants import TIMESTEP


def acceleration(body, other):
    if body == other:
        return 0, 0
    distance_x = body.get_x() - other.get_x()
    distance_y = body.get_y() - other.get_y()
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    theta = math.atan2(distance_y, distance_x)

    acceleration = -G * other.get_mass() / distance ** 2
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

        body.set_vel_x(body.get_vel_x() + total_ax * TIMESTEP)
        body.set_vel_y(body.get_vel_y() + total_ay * TIMESTEP)

        body.set_new_x(body.get_x() + body.get_vel_x() * TIMESTEP)
        body.set_new_y(body.get_y() + body.get_vel_y() * TIMESTEP)


def update_positions():
    for body in bodies:
        body.set_x(body.get_new_x())
        body.set_y(body.get_new_y())

        if len(body.arc) > 400:
            body.arc.pop(0)
            body.arc.append([body.get_x(), body.get_y()])
        else:
            body.arc.append([body.get_x(), body.get_y()])
