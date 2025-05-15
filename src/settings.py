# settings.py

# Window
WIDTH, HEIGHT = 960, 540
FPS = 60

# Tile and Physics
TILE_SIZE = 32
GRAVITY = 0.6
JUMP_VELOCITY = -14
MOVE_ACCEL = 0.5
MOVE_DECEL = 0.6
MAX_MOVE_SPEED = 5
MAX_FALL_SPEED = 16

# World
WORLD_WIDTH = 4000  # SHORTER world
WORLD_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "../assets/images/")
