import pygame
import os
from settings import *
from platform_manager import PlatformManager
from utils import load_image

class World:
    def __init__(self):
        self.width = WORLD_WIDTH
        self.height = WORLD_HEIGHT

        self.platform_manager = PlatformManager()
        self.platform_manager.create_ground()
        self.platform_manager.create_manual_platforms()
        self.platforms = self.platform_manager.get_platforms()
        self.load_ground_tiles()

    def load_ground_tiles(self):
        ground_path = os.path.join(ASSETS_DIR, "ground")
        self.ground_tiles = []
        for file in sorted(os.listdir(ground_path)):
            if file.endswith(".png"):
                img = load_image(os.path.join("ground", file))
                self.ground_tiles.append(img)

    def draw(self, surface, camera):
        ground = self.platforms[0]
        num_tiles = ground.width // TILE_SIZE
        for i in range(num_tiles):
            tile_img = self.ground_tiles[i % len(self.ground_tiles)]
            x = ground.x + i * TILE_SIZE
            y = ground.y
            surface.blit(tile_img, camera.apply(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)))

        self.platform_manager.draw_platform(surface, camera)

    def spawn_enemies(self):
        from enemy import Enemy
        return [Enemy(plat) for plat in self.platforms[1:]]