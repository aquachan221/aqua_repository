import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Character Customization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HIGHLIGHT = (100, 100, 100)

# Font settings
font = pygame.font.Font(None, 36)

# Player name storage
player_names = ["Shadow", "Pixel", "Nova", "Echo", "Glitch", "Bolt", "Zenith"]

# Input box settings
input_box = pygame.Rect(200, 150, 200, 50)
dice_icon = pygame.Rect(160, 150, 40, 50)  # Dice icon next to input box

input_text = ""  # Holds the player's name

def get_random_name():
    return random.choice(player_names)

def add_custom_name(name):
    if name and name not in player_names:
        player_names.append(name)

def name_entry_screen():
    global input_text
    while True:
        screen.fill(WHITE)

        # Draw input box
        pygame.draw.rect(screen, GRAY, input_box)
        name_surface = font.render(input_text, True, BLACK)
        screen.blit(name_surface, (input_box.x + 10, input_box.y + 10))

        # Draw dice icon
        pygame.draw.rect(screen, HIGHLIGHT, dice_icon)
        dice_surface = font.render("🎲", True, BLACK)  # Dice icon placeholder
        screen.blit(dice_surface, (dice_icon.x + 10, dice_icon.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text:
                    add_custom_name(input_text)
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dice_icon.collidepoint(event.pos):  # If dice is clicked
                    input_text = get_random_name()

# Run name entry system
player_name = name_entry_screen()
print(f"Selected Name: {player_name}")  # This will later transition into gameplay