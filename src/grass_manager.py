import pygame
import random
from settings import *
from utils import load_image

class GrassManager:
    def __init__(self, width, spike_columns, decoration_columns, spike_rects, player_spawn_x):
        self.img_static = load_image("background/unchangeable/grass_unmoved.png", scale_to_tile=True)
        self.img_move = load_image("background/unchangeable/grass_moved.png", scale_to_tile=True)
        self.ground_y = HEIGHT - TILE_SIZE + 33
        self.width = width
        self.spike_columns = spike_columns
        self.decoration_columns = decoration_columns
        self.spike_rects = spike_rects
        self.player_spawn_col = player_spawn_x // TILE_SIZE

        self.grass_columns = set()

        cols = self.width // TILE_SIZE
        for col in range(cols):
            if col == self.player_spawn_col:
                continue
            if col in self.decoration_columns:
                continue

            x = col * TILE_SIZE
            grass_rect = pygame.Rect(x, self.ground_y, TILE_SIZE, TILE_SIZE)
    
            collision_with_spike = any(grass_rect.colliderect(spike_rect) for spike_rect in self.spike_rects)
            if collision_with_spike:
                continue

            if random.random() < 0.5:
                self.grass_columns.add(col)

    def draw(self, surface, player, camera):
        for col in self.grass_columns:
            x = col * TILE_SIZE
            rect = pygame.Rect(x, self.ground_y, TILE_SIZE, TILE_SIZE)
            img = self.img_move if player.rect.colliderect(rect) else self.img_static
            surface.blit(img, camera.apply(rect))