import pygame
from settings import TILE_SIZE
from utils import load_image

class SpikeManager:
    def __init__(self, platforms):
        self.img_ground = load_image("spikes/spikes_ground.png", scale_to_tile=True)
        self.img_platform = load_image("spikes/spikes_platforms.png", scale_to_tile=True)

        self.spikes = []
        self.spike_columns = set()

        ground = platforms[0]
        for x in [300, 1500]:
            rect = pygame.Rect(x, ground.y - TILE_SIZE, TILE_SIZE, TILE_SIZE)
            self.spikes.append({"rect": rect, "orient": "up"})
            self.spike_columns.add(x // TILE_SIZE)

        for plat in platforms[1:]:
            mid_x = plat.centerx - TILE_SIZE // 2
            rect = pygame.Rect(mid_x, plat.bottom - 16, TILE_SIZE, TILE_SIZE)
            self.spikes.append({"rect": rect, "orient": "down"})
            self.spike_columns.add(mid_x // TILE_SIZE)

    def check_collisions(self, player):
        for s in self.spikes:
            if player.rect.colliderect(s["rect"]):
                player.start_death()

    def draw(self, surface, camera):
        for s in self.spikes:
            img = self.img_ground if s["orient"] == "up" else self.img_platform
            surface.blit(img, camera.apply(s["rect"]))

    def get_spike_rects(self):
        return [s["rect"] for s in self.spikes]