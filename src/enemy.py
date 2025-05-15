# src/enemy.py

import pygame
from settings import *
from utils import load_animation_folder
from animation_controller import AnimationController
from physics_manager import PhysicsManager

class Enemy:
    def __init__(self, platform):
        self.platform = platform
        self.spawn_x = platform.centerx - TILE_SIZE // 2
        self.pos = pygame.Vector2(self.spawn_x, platform.top - TILE_SIZE)
        self.vel = pygame.Vector2(2, 0)
        self.dying = False
        self.death_timer = 0

        self.load_animations()
        self.anim_controller = AnimationController(self.animations["walk"])
        self.image = self.anim_controller.get_image()
        self.rect = self.image.get_rect(topleft=self.pos)

        self.physics = PhysicsManager(self)

    def load_animations(self):
        self.animations = {
            "idle": load_animation_folder("enemy/basic/idle"),
            "walk": load_animation_folder("enemy/basic/walk"),
            "die":  load_animation_folder("enemy/basic/die"),
        }

    def start_death(self):
        if not self.dying:
            self.dying = True
            self.vel.x = 0
            self.death_timer = FPS
            self.anim_controller.frames = self.animations["die"]
            self.anim_controller.index = 0

    def update(self):
        if self.dying:
            self.death_timer -= 1
            self.anim_controller.update()
            self.image = self.anim_controller.get_image()
            return self.death_timer > 0

        self.pos.x += self.vel.x
        if self.rect.left <= self.platform.left:
            self.vel.x = abs(self.vel.x)
        if self.rect.right >= self.platform.right:
            self.vel.x = -abs(self.vel.x)

        self.rect.x = int(self.pos.x)

        self.anim_controller.frames = self.animations["walk"]
        self.anim_controller.update()
        self.image = self.anim_controller.get_image()

        return True

    def draw(self, surface, camera):
        img = pygame.transform.flip(self.image, self.vel.x < 0, False)
        img = pygame.transform.scale(img, (int(img.get_width() * 1.2), int(img.get_height() * 1.2)))
        surface.blit(img, camera.apply(self.rect))