# Game of life
import pygame
import patterns

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 200, 200
CELL_SIZE = WIDTH // COLS

# Colors
C1 = (255, 255, 255)
C2 = (0, 0, 0)

# Initialize screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game of Life')

# Create grid
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Randomize grid
patterns.randomize_grid(grid)


# Main loop
running = True
while running:
    screen.fill(C1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update grid
    next_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if 0 <= i + x < ROWS and 0 <= j + y < COLS:
                        neighbors += grid[i + x][j + y]
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = 1
            else:
                if neighbors == 3:
                    next_grid[i][j] = 1

    grid = next_grid

    # Draw grid
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, C2, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    # Quit on escape key press event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
