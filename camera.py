from bodies import sun


class Camera:

    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.time = 0
        self.target = target
        self.pan_speed = 500

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def set_target(self, target):
        self.set_x(target.get_x())
        self.set_y(target.get_y())
        self.target = target

    def get_target(self):
        return self.target

    def get_pan_speed(self):
            return self.pan_speed

    def smoother(self, target):
        self.time += 1
        if 0 < self.get_time() < self.get_pan_speed():
            self.set_x((((self.get_pan_speed() - self.get_time()) * self.get_x() + self.get_time() * target.get_x()) / self.get_pan_speed()))
            self.set_y((((self.get_pan_speed() - self.get_time()) * self.get_y() + self.get_time() * target.get_y()) / self.get_pan_speed()))
        else:
            self.set_time(0)
            self.set_target(target)


camera = Camera(sun.get_x(), sun.get_y(), sun)
