import pygame
from settings import TILE_SIZE
from utils import load_image

class PlatformManager:
    def __init__(self):
        self.platforms = []
        self.left_img = load_image("platforms/changeable/platform_changeable_1.png")
        self.mid_img = load_image("platforms/changeable/platform_changeable_2.png")
        self.right_img = load_image("platforms/changeable/platform_changeable_3.png")

    def create_ground(self):
        ground = pygame.Rect(0, 600 - TILE_SIZE, 4000, TILE_SIZE)
        self.platforms.append(ground)

    def create_manual_platforms(self):
        self.platforms.append(pygame.Rect(450, 600 - TILE_SIZE * 5, TILE_SIZE * 4, TILE_SIZE))
        self.platforms.append(pygame.Rect(700, 600 - TILE_SIZE * 4, TILE_SIZE * 3, TILE_SIZE))
        self.platforms.append(pygame.Rect(1000, 600 - TILE_SIZE * 4, TILE_SIZE * 5, TILE_SIZE))
        self.platforms.append(pygame.Rect(1300, 600 - TILE_SIZE * 5, TILE_SIZE * 4, TILE_SIZE))
        self.platforms.append(pygame.Rect(1700, 600 - TILE_SIZE * 4, TILE_SIZE * 3, TILE_SIZE))

    def get_platforms(self):
        return self.platforms

    def draw_platform(self, surface, camera):
        for plat in self.platforms[1:]:
            num_tiles = plat.width // TILE_SIZE
            for i in range(num_tiles):
                if i == 0:
                    img = self.left_img
                elif i == num_tiles - 1:
                    img = self.right_img
                else:
                    img = self.mid_img
                x = plat.x + i * TILE_SIZE
                y = plat.y
                surface.blit(img, camera.apply(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)))