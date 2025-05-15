# src/player.py

import pygame
from settings import *
from utils import load_animation_folder
from animation_controller import AnimationController
from physics_manager import PhysicsManager

class Player:
    def __init__(self, x, y):
        self.spawn = pygame.Vector2(x, y)
        self.pos = self.spawn.copy()
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        self.facing_right = True
        self.dying = False
        self.death_timer = 0

        self.load_animations()
        self.anim_controller = AnimationController(self.animations["idle"])
        self.image = self.anim_controller.get_image()
        self.rect = self.image.get_rect(topleft=self.pos)

        self.physics = PhysicsManager(self)

    def load_animations(self):
        self.animations = {
            "idle": load_animation_folder("player/idle"),
            "walk": load_animation_folder("player/walk"),
            "jump": load_animation_folder("player/jump"),
            "die":  load_animation_folder("player/die"),
        }

    def reset(self):
        self.pos = self.spawn.copy()
        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False
        self.facing_right = True
        self.dying = False
        self.death_timer = 0
        self.rect.topleft = self.pos
        self.anim_controller.frames = self.animations["idle"]
        self.anim_controller.index = 0

    def start_death(self):
        if not self.dying:
            self.dying = True
            self.vel = pygame.Vector2(0, 5)
            self.death_timer = FPS  # 1 second before respawn
            self.anim_controller.frames = self.animations["die"]
            self.anim_controller.index = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel.x = max(self.vel.x - MOVE_ACCEL, -MAX_MOVE_SPEED)
            self.facing_right = False
        elif keys[pygame.K_RIGHT]:
            self.vel.x = min(self.vel.x + MOVE_ACCEL, MAX_MOVE_SPEED)
            self.facing_right = True
        else:
            if self.vel.x > 0:
                self.vel.x = max(self.vel.x - MOVE_DECEL, 0)
            elif self.vel.x < 0:
                self.vel.x = min(self.vel.x + MOVE_DECEL, 0)

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel.y = JUMP_VELOCITY
            self.on_ground = False

    def update_animation(self):
        if self.dying:
            frames = self.animations["die"]
        elif not self.on_ground:
            frames = self.animations["jump"]
        elif abs(self.vel.x) > 0.1:
            frames = self.animations["walk"]
        else:
            frames = self.animations["idle"]

        if self.anim_controller.frames != frames:
            self.anim_controller.frames = frames
            self.anim_controller.index = 0

        self.anim_controller.update()
        self.image = self.anim_controller.get_image()

    def update(self, platforms):
        if self.dying:
            self.physics.apply_gravity()
            self.physics.move_and_collide(platforms)
            self.update_animation()
            self.death_timer -= 1
            if self.death_timer <= 0 and self.on_ground:
                self.reset()
            return

        self.handle_input()
        self.physics.apply_gravity()
        self.physics.move_and_collide(platforms)
        self.update_animation()

        # Clamp to world bounds
        self.rect.x = max(0, min(self.rect.x, WORLD_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, WORLD_HEIGHT - self.rect.height))

    def draw(self, surface, camera):
        img = pygame.transform.flip(self.image, not self.facing_right, False)
        img = pygame.transform.scale(img, (int(img.get_width() * 1.2), int(img.get_height() * 1.2)))
        surface.blit(img, camera.apply(self.rect))