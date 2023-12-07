from camera import camera
from constants import AU
from display import WIDTH, HEIGHT
from display import scale


def is_hitbox(body, x, y):
    distance = (body.x * scale / AU - camera.x * scale / AU + WIDTH // 2 - x) ** 2 \
               + (body.y * scale / AU - camera.y * scale / AU + HEIGHT // 2 - y) ** 2
    if distance < body.get_radius() ** 2:
        return True
    return False
