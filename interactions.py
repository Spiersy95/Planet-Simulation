from camera import camera
from constants import AU
from display import WIDTH, HEIGHT
from display import scale


def is_hitbox(body, x, y):
    if - body.hitbox[2] < x - body.hitbox[0] * scale / AU - WIDTH // 2 + camera.x * scale / AU < body.hitbox[2] \
            and - body.hitbox[2] < y - body.hitbox[1] * scale / AU - HEIGHT // 2 + camera.y * scale / AU < body.hitbox[2]:
        return True
    return False