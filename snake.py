import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake and food properties
block_size = 20
snake = [(200, 200)]  # Starting position
direction = (0, 0)  # Start stationary
food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
speed = 10  # Slower for testing
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

# Game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, block_size):
                direction = (0, -block_size)
            elif event.key == pygame.K_DOWN and direction != (0, -block_size):
                direction = (0, block_size)
            elif event.key == pygame.K_LEFT and direction != (block_size, 0):
                direction = (-block_size, 0)
            elif event.key == pygame.K_RIGHT and direction != (-block_size, 0):
                direction = (block_size, 0)
            elif event.key == pygame.K_SPACE and game_over:  # Restart on spacebar
                snake = [(200, 200)]
                direction = (0, 0)
                food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
                game_over = False

    if not game_over:
        # Move the snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Check if snake ate food
        if snake[0] == food:
            food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
        else:
            snake.pop()

        # Check for collisions
        if (snake[0][0] < 0 or snake[0][0] >= width or
            snake[0][1] < 0 or snake[0][1] >= height or
            snake[0] in snake[1:]):
            game_over = True

    # Draw everything
    screen.fill(BLACK)
    if game_over:
        game_over_text = font.render("Game Over! Press Space", True, WHITE)
        screen.blit(game_over_text, (width//2 - 150, height//2 - 25))
    else:
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], block_size, block_size))
        pygame.draw.rect(screen, RED, (food[0], food[1], block_size, block_size))
    pygame.display.flip()

    # Control game speed
    clock.tick(speed)

pygame.quit()