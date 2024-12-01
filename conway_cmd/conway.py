# TODO: Figure out how to handle the lists better ya scrub
import subprocess
import os
import time

RUN = True
TICK_SPEED = .2
start = time.time()
TEST = 1

GRID = []
for row in range(20):
    GRID.append([])
    for col in range(20):
        GRID[row].append(0)


GRID[10][10] = 1
GRID[11][10] = 1
GRID[12][10] = 1
GRID[11][9] = 1
GRID[12][11] = 1

dirs = [
    [-1, 0],
    [-1, +1],
    [0, +1],
    [+1, +1],
    [+1, 0],
    [-1, -1],
    [0, -1],
    [+1, -1],
]
#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
def get_neighbor_count(grid, x, y):
    num_neighbors = 0
    for dir in dirs:
        row = x + dir[0]
        col = y + dir[1]
        if row < 0 or row >= len(grid):
            continue

        if col < 0 or col >= len(grid):
            continue

        if grid[row][col] == 1:
            num_neighbors += 1

    return num_neighbors

def advance(grid):
    os.system('cls')
    
    new_grid = []
    
    for row in range(20):
        new_grid.append([])
        for col in range(20):
            if grid[row][col] == 1:
                new_grid[row].append(1)
            else:
                new_grid[row].append(0)

    #for row in new_grid:
    #    print(' '.join(map(str, row)))

    for row in range(20):
        for col in range(20):
            count = get_neighbor_count(grid, row, col)
            if count < 2:
                new_grid[row][col] = 0
            if count > 3:
                new_grid[row][col] = 0
            if count == 3:
                new_grid[row][col] = 1
    
    display = []
    
    for row in range(len(new_grid)):
        display.append([])
        for col in range(len(new_grid)):
            if new_grid[row][col] == 0:
                display[row].append(' ')
            else:
                display[row].append('X')
    
    for row in display:    
        print(' '.join(map(str, row)))

    return new_grid


while RUN:
    if time.time() >= start+TICK_SPEED:
        GRID = advance(GRID)
        start = time.time()