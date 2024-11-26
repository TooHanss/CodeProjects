import pygame
import math
pygame.init()


ROWS = 15
COLUMNS = 20
MARGIN = 1
CELL_SIZE = 20 
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

while run:
    screen.fill((255, 255, 255))
    for row in range(ROWS):
        for column in range(COLUMNS):
            pygame.draw.rect(screen, (0, 0, 0),[(CELL_SIZE * column) + MARGIN,
                                                (CELL_SIZE * row) + MARGIN,
                                                CELL_SIZE - (MARGIN * 2),
                                                CELL_SIZE - (MARGIN * 2)]) # X pos, Y pos, width, height
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()