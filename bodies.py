from constants import AU


class CelestialBody:

    def __init__(self, x, y, colour, radius, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.colour = colour
        self.hitbox = (self.x, self.y, self.radius)

        self.vel_x = 0
        self.vel_y = 0

        self.new_x = x
        self.new_y = y

        self.arc = []

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass

    def get_colour(self):
        return self.colour

    def get_vel_x(self):
        return self.vel_x

    def set_vel_x(self, vel_x):
        self.vel_x = vel_x

    def get_vel_y(self):
        return self.vel_y

    def set_vel_y(self, vel_y):
        self.vel_y = vel_y

    def get_new_x(self):
        return self.new_x

    def set_new_x(self, new_x):
        self.new_x = new_x

    def get_new_y(self):
        return self.new_y

    def set_new_y(self, new_y):
        self.new_y = new_y

class Planet(CelestialBody):
    def __init__(self, x, y, colour, radius, mass):
        super().__init__(x, y, colour, radius, mass)



class Sun(CelestialBody):
    def __init__(self, x, y, colour, radius, mass):
        super().__init__(x, y, colour, radius, mass)



sun = Sun(0, 0, (255, 255, 0), 30, 1.98892e30)

mercury = Planet(0.387 * AU, 0, (0, 202, 0), 8, 3.30e23)
mercury.set_vel_y(-47.4 * 1000)

venus = Planet(0.72 * AU, 0, (255, 165, 0), 14, 4.867e24)
venus.set_vel_y(-35.02 * 1000)

earth = Planet(-AU, 0, (100, 149, 237), 16, 5.972e24)
earth.set_vel_y(29.73 * 1000)

mars = Planet(-1.52 * AU, 0, (188, 39, 50), 12, 6.417e23)
mars.set_vel_y(24.07 * 1000)

jupiter = Planet(5.2 * AU, 0, (255, 140, 0), 25, 1.899e27)
jupiter.set_vel_y(-10 * 1000)

saturn = Planet(-9.5 * AU, 0, (150, 75, 0), 20, 5.683e26)
saturn.set_vel_y(9 * 1000)

uranus = Planet(20 * AU, 0, (0, 0, 100), 18, 8.681e25)
uranus.set_vel_y(-8 * 1000)

bodies = [mercury, mars, venus, earth, jupiter, sun]
