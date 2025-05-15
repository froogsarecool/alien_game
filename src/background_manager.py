import pygame
import random
from settings import TILE_SIZE, WORLD_WIDTH, WORLD_HEIGHT
from utils import load_image

class BackgroundManager:
    def __init__(self, spike_columns):
        self.surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT), pygame.SRCALPHA)
        self.ground_y = WORLD_HEIGHT - TILE_SIZE
        self.spike_columns = spike_columns
        self.decoration_columns = set()  # NEW: Track where decorations are placed
        self.build_background()

    def build_background(self):
        self.surface.fill((0, 0, 0))

        tree_positions = [200, 800, 1400, 2200, 3000]
        for x in tree_positions:
            self.draw_tree(x)

        decoration_options = [
            "background/unchangeable/flowers_1.png",
            "background/unchangeable/flowers_2.png",
            "background/unchangeable/bush_1.png",
            "background/unchangeable/mushroom_1.png"
        ]

        cols = WORLD_WIDTH // TILE_SIZE
        for col in range(cols):
            if any(abs(col - s) <= 1 for s in self.spike_columns):
                continue

            if random.random() < 0.6:
                choice = random.choice(decoration_options)
                img = load_image(choice)
                img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                x = col * TILE_SIZE
                y = self.ground_y - TILE_SIZE + (TILE_SIZE - img.get_height())
                self.surface.blit(img, (x, y))

                self.decoration_columns.add(col)  # NEW: Record decoration position

        arrow = load_image("background/unchangeable/arrow_sign.png")
        arrow = pygame.transform.scale(arrow, (TILE_SIZE, TILE_SIZE))
        self.surface.blit(arrow, (TILE_SIZE, self.ground_y - TILE_SIZE))

    def draw_tree(self, x):
        bot = load_image("background/changeable/tree_changeable_3.png")
        mid = load_image("background/changeable/tree_changeable_2.png")
        top = load_image("background/changeable/tree_changeable_1.png")

        bot = pygame.transform.scale(bot, (TILE_SIZE * 2, TILE_SIZE))
        mid = pygame.transform.scale(mid, (TILE_SIZE * 2, TILE_SIZE))
        top = pygame.transform.scale(top, (TILE_SIZE * 2, TILE_SIZE))

        base_y = self.ground_y - TILE_SIZE

        self.surface.blit(bot, (x, base_y))

        tree_height = random.choice([2, 3, 4])
        for i in range(tree_height - 2):
            self.surface.blit(mid, (x, base_y - TILE_SIZE * (i + 1)))

        self.surface.blit(top, (x, base_y - TILE_SIZE * (tree_height - 1)))

    def draw(self, surface, camera):
        surface.blit(self.surface, (-camera.x, -camera.y))