# src/physics_manager.py

from settings import GRAVITY, MAX_FALL_SPEED

class PhysicsManager:
    def __init__(self, entity):
        self.entity = entity

    def apply_gravity(self):
        self.entity.vel.y += GRAVITY
        if self.entity.vel.y > MAX_FALL_SPEED:
            self.entity.vel.y = MAX_FALL_SPEED

    def move_and_collide(self, platforms):
        self.entity.rect.x += self.entity.vel.x
        self.check_collision(platforms, "horizontal")
        self.entity.rect.y += self.entity.vel.y
        self.entity.on_ground = False
        self.check_collision(platforms, "vertical")

    def check_collision(self, platforms, direction):
        for plat in platforms:
            if self.entity.rect.colliderect(plat):
                if direction == "horizontal":
                    if self.entity.vel.x > 0:
                        self.entity.rect.right = plat.left
                    elif self.entity.vel.x < 0:
                        self.entity.rect.left = plat.right
                    self.entity.vel.x = 0
                elif direction == "vertical":
                    if self.entity.vel.y > 0:
                        self.entity.rect.bottom = plat.top
                        self.entity.vel.y = 0
                        self.entity.on_ground = True
                    elif self.entity.vel.y < 0:
                        self.entity.rect.top = plat.bottom
                        self.entity.vel.y = 0