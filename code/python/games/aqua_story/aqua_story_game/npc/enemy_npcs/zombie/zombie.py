import pygame
import sys
from aqua_story_game.aqua_story_ver_prerelease import screen
from aqua_story_game.aqua_story_ver_prerelease import clock
from aqua_story_game.aqua_story_ver_prerelease import pause_menu
from aqua_story_game.aqua_story_ver_prerelease import screen
from debug_map import *
global zombie_color
walls = debug_map
#zombie vars:#type: bruh
zombie_speed = 0.07
zombie_color = (0, 200, 0)
#zombie behavior:

zombie_move_timer = 0
zombie_move_delay = int(1 / zombie_speed) if zombie_speed > 0 else 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_menu(screen, clock)
                continue  # Redraw after pause
            move_amount = 2 if pygame.key.get_mods() & pygame.KMOD_SHIFT else 1
            new_x, new_y = player_x, player_y
            if event.key == pygame.K_a:
                    new_x = max(0, player_x - move_amount)
            elif event.key == pygame.K_d:
                new_x = min(grid_width - 1, player_x + move_amount)
            elif event.key == pygame.K_w:
                new_y = max(0, player_y - move_amount)
            elif event.key == pygame.K_s:
                new_y = min(grid_height - 1, player_y + move_amount)
                # Prevent moving into zombie or wall
            if (new_x, new_y) != (zombie_x, zombie_y) and (new_x, new_y) not in walls:
                player_x, player_y = new_x, new_y
        zombie_move_timer += 1
        if zombie_move_timer >= zombie_move_delay:
            zombie_move_timer = 0
            dx = player_x - zombie_x
            dy = player_y - zombie_y
            move_x, move_y = 0, 0
            if abs(dx) > abs(dy):
                move_x = 1 if dx > 0 else -1 if dx < 0 else 0
            elif dy != 0:
                move_y = 1 if dy > 0 else -1 if dy < 0 else 0
            next_zombie_x = zombie_x + move_x
            next_zombie_y = zombie_y + move_y
            # Prevent zombie from moving into player's cell or a wall
            if (next_zombie_x, next_zombie_y) != (player_x, player_y) and (next_zombie_x, next_zombie_y) not in walls:
                zombie_x, zombie_y = next_zombie_x, next_zombie_y
            # If direct move would collide, try alternate axis
            elif move_x != 0 and dy != 0:
                alt_zombie_y = zombie_y + (1 if dy > 0 else -1)
                if (zombie_x, alt_zombie_y) != (player_x, player_y) and (zombie_x, alt_zombie_y) not in walls:
                    zombie_y = alt_zombie_y
            elif move_y != 0 and dx != 0:
                alt_zombie_x = zombie_x + (1 if dx > 0 else -1)
                if (alt_zombie_x, zombie_y) != (player_x, player_y) and (alt_zombie_x, zombie_y) not in walls:
                    zombie_x = alt_zombie_x