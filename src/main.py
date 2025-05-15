import pygame
import sys
from settings import *
from player import Player
from camera import Camera
from world import World
from background_manager import BackgroundManager
from grass_manager import GrassManager
from spike_manager import SpikeManager
from enemy import Enemy

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("True Platformer Engine")
clock = pygame.time.Clock()

# Create game objects
player = Player(100, HEIGHT - TILE_SIZE * 3)
world = World()
spike_manager = SpikeManager(world.platforms)
background_manager = BackgroundManager(spike_manager.spike_columns)
grass_manager = GrassManager(
    world.width,
    spike_manager.spike_columns,
    background_manager.decoration_columns,
    spike_manager.get_spike_rects(),  # << NEW
    player.spawn.x
)
enemies = world.spawn_enemies()
camera = Camera(world.width, world.height)

# Main game loop
running = True
try:
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not player.dying:
            player.update(world.platforms)

            for enemy in enemies[:]:
                if not enemy.update():
                    enemies.remove(enemy)

            spike_manager.check_collisions(player)

            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    if player.vel.y > 0 and 0 < player.rect.bottom - enemy.rect.top < 10:
                        enemy.start_death()
                        player.vel.y = JUMP_VELOCITY / 2
                    else:
                        player.start_death()
        else:
            player.update(world.platforms)

        camera.update(player.rect)

        # Draw everything
        screen.fill(BLACK)
        background_manager.draw(screen, camera)
        world.draw(screen, camera)
        spike_manager.draw(screen, camera)

        for enemy in enemies:
            enemy.draw(screen, camera)

        player.draw(screen, camera)
        grass_manager.draw(screen, player, camera)

        pygame.display.flip()

finally:
    pygame.quit()
    sys.exit()