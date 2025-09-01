import pygame, sys, random

# Init
pygame.init()
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 🐍")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Snake setup
snake = [(100, 50), (90, 50), (80, 50)]
snake_dir = "RIGHT"
cell = 10

# Food
food = (random.randrange(1, WIDTH//cell) * cell,
        random.randrange(1, HEIGHT//cell) * cell)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != "DOWN": snake_dir = "UP"
    if keys[pygame.K_DOWN] and snake_dir != "UP": snake_dir = "DOWN"
    if keys[pygame.K_LEFT] and snake_dir != "RIGHT": snake_dir = "LEFT"
    if keys[pygame.K_RIGHT] and snake_dir != "LEFT": snake_dir = "RIGHT"

    # Move snake
    x, y = snake[0]
    if snake_dir == "UP": y -= cell
    if snake_dir == "DOWN": y += cell
    if snake_dir == "LEFT": x -= cell
    if snake_dir == "RIGHT": x += cell
    new_head = (x, y)

    snake.insert(0, new_head)  # add new head

    # Check food
    if snake[0] == food:
        food = (random.randrange(1, WIDTH//cell) * cell,
                random.randrange(1, HEIGHT//cell) * cell)
        # don’t pop tail → snake grows
    else:
        snake.pop()  # remove tail → keeps length

    # Check collisions
    if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or len(snake) != len(set(snake))):
        pygame.quit(); sys.exit()

    # Draw everything
    win.fill(BLACK)
    for s in snake:
        pygame.draw.rect(win, GREEN, (*s, cell, cell))
    pygame.draw.rect(win, RED, (*food, cell, cell))

    pygame.display.update()
    clock.tick(10)  # game speed

