import pygame
import sys
import random #type: ignore
from maps import debug_map
from enemy_npcs import zombie, zombie_color
# Define walls as an empty list or with your desired wall positions
walls = []

debug_map = walls
grid_size = 30
grid_width = 30
grid_height = 20
window_width = grid_size * grid_width
window_height = grid_size * grid_height

#map colors
bg_color = (30, 30, 30)
square_color = (0, 200, 255)
grid_color = (60, 60, 60)
wall_color = (120, 120, 120)
# class colors
warrior_color = (255, 0, 0)
mage_color = (0, 0, 255)
rogue_color = (0, 255, 0)
#stupid vars:

#currencies


#races

#classes


ranger_classes = ["26: archer", "27: marksman", "28: sniper", "29: gunslinger"]
rogue_classes = ["30: rogue", "31: assassin", "32: trickster", "33: bounty_hunter", "34: explorer", "35: scout", "36: survivalist"]
misc_classes = ["37: soulreaper", "38: cosmic_herald"]

def determ_intro():
    intro_num=random.randint(0, 10)

def draw_grid(surface):
    for x in range(0, window_width, grid_size):
        pygame.draw.line(surface, grid_color, (x, 0), (x, window_height))
    for y in range(0, window_height, grid_size):
        pygame.draw.line(surface, grid_color, (0, y), (window_width, y))

def pause_menu(screen, clock):
    while True:
        choice = menu_loop(screen, clock, ["Resume", "Main Menu", "Exit"], "Paused")
        if choice == 0:
            return  # Resume game
        elif choice == 1:
            main_menu(screen, clock)
            return
        elif choice == 2:
            pygame.quit()
            sys.exit()

def starting_map(screen, clock):
    global bot_speed
    # Player position in grid coordinates
    player_x, player_y = grid_width // 2, grid_height // 2

    # Zombie position (integer grid coordinates)
    zombie_x, zombie_y = 1, 1

    bot_move_timer = 0
    bot_move_delay = int(1 / bot_speed) if bot_speed > 0 else 1  # frames between bot moves 

    while True:
        global zombie_color
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

        bot_move_timer += 1
        if bot_move_timer >= bot_move_delay:
            bot_move_timer = 0
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

        screen.fill(bg_color)
        draw_grid(screen)
        # Draw walls
        for wx, wy in walls:
            wall_rect = pygame.Rect(wx * grid_size, wy * grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, wall_color, wall_rect)
        # Draw player square
        rect = pygame.Rect(player_x * grid_size, player_y * grid_size, grid_size, grid_size)
        pygame.draw.rect(screen, square_color, rect)
        # Draw zombie square
        zombie_rect = pygame.Rect(zombie_x * grid_size, zombie_y * grid_size, grid_size, grid_size)
        pygame.draw.rect(screen, zombie_color, zombie_rect)
        # Draw zombie name
        font = pygame.font.SysFont(None, 24)
        name_surf = font.render("Zombie", True, (255,255,255))
        name_rect = name_surf.get_rect(center=(zombie_x * grid_size + grid_size // 2, zombie_y * grid_size - 10))
        screen.blit(name_surf, name_rect)

        pygame.display.flip()
        clock.tick(60)

def draw_text_centered(surface, text, y, font, color=(255,255,255)):
    text_surf = font.render(text, True, color)
    rect = text_surf.get_rect(center=(window_width // 2, y))
    surface.blit(text_surf, rect)
    return rect  # Return rect for button hitbox

def menu_loop(screen, clock, menu_items, title="Menu"):
    font = pygame.font.SysFont(None, 40)
    title_font = pygame.font.SysFont(None, 60)
    button_rects = []
    while True:
        screen.fill(bg_color)
        draw_text_centered(screen, title, 80, title_font)
        button_rects.clear()
        mx, my = pygame.mouse.get_pos()
        for i, item in enumerate(menu_items):
            # Highlight button white if mouse is over it, else yellow
            rect = draw_text_centered(
                screen,
                item,
                180 + i*50,
                font,
                (255,255,255) if i == get_hovered_button(mx, my, button_rects) else (255,255,0)
            )
            button_rects.append(rect)
        # After all rects are created, update colors again for hover
        for i, rect in enumerate(button_rects):
            if rect.collidepoint(mx, my):
                # Redraw hovered button in white
                draw_text_centered(screen, menu_items[i], 180 + i*50, font, (255,255,255))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for idx, rect in enumerate(button_rects):
                    if rect.collidepoint(mx, my):
                        return idx
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
        clock.tick(30)

def get_hovered_button(mx, my, button_rects):
    for idx, rect in enumerate(button_rects):
        if rect.collidepoint(mx, my):
            return idx
    return -1

def main_menu(screen, clock):
    while True:
        choice = menu_loop(screen, clock, ["Start Game", "Settings", "Exit"], "Main Menu")
        if choice == 0:
            start_game_menu(screen, clock)
        elif choice == 1:
            settings_menu(screen, clock)
        elif choice == 2:
            pygame.quit()
            sys.exit()

def start_game_menu(screen, clock):
    while True:
        choice = menu_loop(screen, clock, ["Online Play", "Local Play", "Back"], "Start Game")
        if choice == 0:
            # Placeholder for online play
            menu_loop(screen, clock, ["Not implemented", "Back"], "Online Play")
        elif choice == 1:
            local_play_menu(screen, clock)
        elif choice == 2 or choice is None:
            return

def character_creator(screen, clock):
    font = pygame.font.SysFont(None, 40)
    input_active = True
    name = ""
    step = 0
    gender_options = ["Male", "Female", "Else"]
    class_options = ["Warrior", "Mage", "Rogue"]
    selected_gender = 0
    selected_class = 0
    while input_active:
        screen.fill(bg_color)
        button_rects = []
        mx, my = pygame.mouse.get_pos()

        if step == 0:
            draw_text_centered(screen, "Enter your name:", 120, font)
            draw_text_centered(screen, name + "_", 180, font)
        elif step == 1:
            draw_text_centered(screen, "Select Gender:", 120, font)
            for i, g in enumerate(gender_options):
                color = (255, 255, 255) if get_hovered_button(mx, my, button_rects) == i else (255, 255, 0)
                rect = draw_text_centered(screen, g, 180 + i*50, font, color)
                button_rects.append(rect)
        elif step == 2:
            draw_text_centered(screen, "Select Class:", 120, font)
            for i, c in enumerate(class_options):
                color = (255, 255, 255) if get_hovered_button(mx, my, button_rects) == i else (255, 255, 0)
                rect = draw_text_centered(screen, c, 180 + i*50, font, color)
                button_rects.append(rect)
        elif step == 3:
            draw_text_centered(screen, f"Name: {name}", 120, font)
            draw_text_centered(screen, f"Gender: {gender_options[selected_gender]}", 170, font)
            draw_text_centered(screen, f"Class: {class_options[selected_class]}", 220, font)
            draw_text_centered(screen, "Click to start!", 320, font)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif step == 0 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    step = 1
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return
                elif len(name) < 16 and event.unicode.isprintable() and event.unicode.strip():
                    name += event.unicode
            elif step == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(mx, my):
                            selected_gender = i
                            step = 2
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            elif step == 2:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(mx, my):
                            selected_class = i
                            step = 3
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            elif step == 3:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    input_active = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

        clock.tick(30)

    # After character creation, start the map
    starting_map(screen, clock)

def local_play_menu(screen, clock):
    while True:
        choice = menu_loop(screen, clock, ["New Save", "Load Save", "Back"], "Local Play")
        if choice == 0:
            character_creator(screen, clock)
        elif choice == 1:
            # Placeholder for load save
            menu_loop(screen, clock, ["Not implemented", "Back"], "Load Save")
        elif choice == 2 or choice is None:
            return

def settings_menu(screen, clock):
    menu_loop(screen, clock, ["Not implemented", "Back"], "Settings")

def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Aqua Story")
    clock = pygame.time.Clock()
    main_menu(screen, clock)

if __name__ == "__main__":  
    main()