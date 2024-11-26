import pygame
import math
pygame.init()


ROWS = 15
COLUMNS = 20
MARGIN = 1
CELL_SIZE = 20 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = COLUMNS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pygame.time.Clock()
run = True
grid = []
for row in range(ROWS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(0)

grid[1][1] = 1

while run:
    screen.fill((255, 255, 255))
    next_grid = []
    for row in range(ROWS):
        next_grid.append([])
        for column in range(COLUMNS):
            next_grid[row].append(0)


    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == 1:
                if row+1 == ROWS:
                    next_grid[row][column] = 1
                    continue
                if grid[row+1][column] == 0:
                    next_grid[row+1][column] = 1
                    next_grid[row][column] = 0
            if next_grid[row][column] == 1:        
                color = WHITE
            else:
                color = BLACK
            
    for row in range(ROWS):
        for column in range(COLUMNS):        
            if next_grid[row][column] == 1:        
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, (color),[(CELL_SIZE * column) + MARGIN,
                                                (CELL_SIZE * row) + MARGIN,
                                                CELL_SIZE - (MARGIN * 2),
                                                CELL_SIZE - (MARGIN * 2)]) # X pos, Y pos, width, height
    grid = next_grid
    pygame.display.flip()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()