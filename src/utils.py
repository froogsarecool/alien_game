# src/utils.py

import pygame
import os
from settings import ASSETS_DIR, TILE_SIZE

def load_image(subpath, scale_to_tile=True):
    path = os.path.join(ASSETS_DIR, subpath)
    img = pygame.image.load(path).convert_alpha()
    if scale_to_tile:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    return img

def load_animation_folder(subpath, scale_to_tile=True):
    frames = []
    full_path = os.path.join(ASSETS_DIR, subpath)
    if not os.path.exists(full_path):
        return frames
    for filename in sorted(os.listdir(full_path)):
        if filename.endswith(".png"):
            frame_path = os.path.join(subpath, filename)
            frames.append(load_image(frame_path, scale_to_tile))
    return frames