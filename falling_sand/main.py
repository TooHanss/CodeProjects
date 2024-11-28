import pygame
import sys
print(sys.path)
from utils.grid import Grid
import math
import numpy
pygame.init()


ROWS = 150
COLUMNS = 200
MARGIN = 0
CELL_SIZE = 5 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = COLUMNS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pygame.time.Clock()
run = True
grid = Grid(ROWS, COLUMNS, 0)
grid.set(1, 1, 1)

while run:
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) / CELL_SIZE
    mouse_pos = (numpy.clip(int(mouse_pos.y), 1, 149), numpy.clip(int(mouse_pos.x), 1, 199))
    screen.fill((255, 255, 255))
    if pygame.mouse.get_pressed()[0]:
            grid.set(mouse_pos[0], mouse_pos[1], 1)
    next_grid = Grid(ROWS, COLUMNS, 0) 
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid.get(row, column) == 1:
                # if we are on the bottom row, do nothing
                if row+1 == ROWS:
                    next_grid.set(row, column, 1)
                    continue
                # if the row underneath is empty
                if grid.get(row+1, column) == 0:
                    next_grid.set(row+1, column, 1)
                    next_grid.set(row, column, 0)
                # if the row underneath is full
                if grid.get(row+1, column) == 1:
                    # if we are not on the left edge
                    if column == 0:
                        if grid.get(row+1, column+1) == 0:
                            next_grid.set(row+1, column+1, 1)
                        else:
                            next_grid.set(row, column, 1)
                    # if we are on the right edge
                    if column == COLUMNS-1:
                        if grid.get(row+1, column-1) == 0:
                            next_grid.set(row+1, column-1, 1)
                        else:
                            next_grid.set(row, column, 1)
                    # if we are not on an edge
                    else:
                        if grid.get(row+1, column+1) == 0:
                            next_grid.set(row+1, column+1, 1)
                        elif grid.get(row+1, column-1) == 0:
                            next_grid.set(row+1, column-1, 1)
                        else:
                            next_grid.set(row, column, 1)
            if next_grid.get(row, column) == 1:        
                color = WHITE
            else:
                color = BLACK
            
    for row in range(ROWS):
        for column in range(COLUMNS):        
            if next_grid.get(row, column) == 1:        
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, (color),[(CELL_SIZE * column) + MARGIN,
                                                (CELL_SIZE * row) + MARGIN,
                                                CELL_SIZE - (MARGIN * 2),
                                                CELL_SIZE - (MARGIN * 2)]) # X pos, Y pos, width, height
    grid = next_grid
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()