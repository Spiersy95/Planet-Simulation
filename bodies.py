from constants import AU


class CelestialBody:

    def __init__(self, x, y, colour, radius, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.colour = colour

        self.vel_x = 0
        self.vel_y = 0

        self.new_x = x
        self.new_y = y

        self.arc = []


class Planet(CelestialBody):
    def __init__(self, x, y, colour, radius, mass):
        super().__init__(x, y, colour, radius, mass)
        self.is_sun = False


class Sun(CelestialBody):
    def __init__(self, x, y, colour, radius, mass):
        super().__init__(x, y, colour, radius, mass)
        self.is_sun = True


sun = Sun(0, 0, (255, 255, 0), 30, 1.98892e30)

mercury = Planet(0.387 * AU, 0, (0, 202, 0), 8, 3.30e23)
mercury.vel_y = -47.4 * 1000

venus = Planet(0.72 * AU, 0, (255, 165, 0), 14, 4.867e24)
venus.vel_y = -35.02 * 1000

earth = Planet(-AU, 0, (100, 149, 237), 16, 5.972e24)
earth.vel_y = 29.73 * 1000

mars = Planet(-1.52 * AU, 0, (188, 39, 50), 12, 6.417e23)
mars.vel_y = 24.07 * 1000

jupiter = Planet(5.2 * AU, 0, (255, 140, 0), 25, 1.899e27)
jupiter.vel_y = -10 * 1000

saturn = Planet(-9.5 * AU, 0, (150, 75, 0), 20, 5.683e26)
saturn.vel_y = 9 * 1000

uranus = Planet(20 * AU, 0, (0, 0, 100), 18, 8.681e25)
uranus.vel_y = -8 * 1000

bodies = [sun, venus, earth, mars, mercury, jupiter]
