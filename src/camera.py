# src/camera.py

from settings import WIDTH, HEIGHT

class Camera:
    def __init__(self, world_width, world_height):
        self.x = 0
        self.y = 0
        self.world_width = world_width
        self.world_height = world_height

    def update(self, target_rect):
        self.x = target_rect.centerx - WIDTH // 2
        self.y = target_rect.centery - HEIGHT // 2

        self.x = max(0, min(self.x, self.world_width - WIDTH))
        self.y = max(0, min(self.y, self.world_height - HEIGHT))

    def apply(self, rect):
        return rect.move(-self.x, -self.y)