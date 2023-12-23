from bodies import sun


class Camera:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.time = 0
        self.target = target
        self.pan_speed = 500

    def get_pan_speed(self):
        return self.pan_speed

    def set_pan_speed(self, value):
        self.pan_speed = value

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_target(self):
        return self.target

    def set_target(self, target):
        self.x = target.x
        self.y = target.y
        self.target = target

    def smoother(self, target):
        self.time += 1
        if 0 < self.time < self.pan_speed:
            self.x = (((self.pan_speed - self.time) * self.x + self.time * target.x) / self.pan_speed)
            self.y = (((self.pan_speed - self.time) * self.y + self.time * target.y) / self.pan_speed)
            self.time += 1
        else:
            self.time = 0
            self.set_target(target)


camera = Camera(sun.x, sun.y, sun)
