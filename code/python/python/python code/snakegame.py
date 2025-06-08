import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Font
font = pygame.font.SysFont("bahnschrift", 25)

# Function to draw the snake
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, green, [block[0], block[1], snake_block, snake_block])

# Function to display the score
def show_score(score):
    value = font.render(f"Score: {score}", True, green)
    win.blit(value, [0, 0])

# Game loop
def game_loop():
    game_over = False
    game_close = False
    
    x, y = width / 2, height / 2
    x_change, y_change = 0, 0
    
    snake_list = []
    snake_length = 1
    
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()
    score = 0

    while not game_over:
        prev_x_change, prev_y_change = x_change, y_change
        while game_close:
            win.fill(black)
            msg = font.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            win.blit(msg, [width / 6, height / 3])
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and prev_x_change != snake_block:
                    x_change = -snake_block
                    y_change = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and prev_x_change != -snake_block:
                    x_change = snake_block
                    y_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and prev_y_change != snake_block:
                    y_change = -snake_block
                    x_change = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and prev_y_change != -snake_block:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, snake_block, snake_block])

        snake_list.append([x, y])
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == [x, y]:
                game_close = True
 
        draw_snake(snake_list)
        show_score(score)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()