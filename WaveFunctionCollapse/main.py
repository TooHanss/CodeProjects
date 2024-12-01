from wfc import Wfc
import pygame as pg
from utils.grid.grid import Grid
import random
# what am i doing...
# could be like img: [n, e ,s, w]
pg.init()
IMG_SIZE = 32
GRID_ROWS = 20
GRID_COLS = 30
GRID = Grid(GRID_ROWS, GRID_COLS, 0)
SCREEN_WIDTH = GRID_COLS * IMG_SIZE
SCREEN_HEIGHT = GRID_ROWS * IMG_SIZE
COLLAPSED = False
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pg.time.Clock()
run = True

# test_img_1 = pg.image.load(r'WaveFunctionCollapse\source_images\road_02_b.png')
# test_img_2 = pg.image.load(r'WaveFunctionCollapse\source_images\road_02_c.png')
# test_img_3 = pg.image.load(r'WaveFunctionCollapse\source_images\road_02_d.png')
# test_img_4 = pg.image.load(r'WaveFunctionCollapse\source_images\road_02.png')
# test_img_5 = pg.image.load(r'WaveFunctionCollapse\source_images\road_05.png')
# socket_to_img = {
#     (1, 0, 0, 1): test_img_1, 
#     (1, 1, 0, 0): test_img_2,
#     (0, 1, 1, 0): test_img_3,
#     (0, 0, 1, 1): test_img_4,
#     (0, 0, 0, 0): test_img_5,
#     }
# sockets = list(socket_to_img.keys())
# for row in range(GRID_ROWS):
#     for col in range(GRID_COLS):
#         GRID.set_value((row, col), sockets)

screen.fill((0, 0, 0))
wfc = Wfc(GRID, r'WaveFunctionCollapse\source_images')

#-------------------- ^^ init shit ^^ clean ip up later


while run:
    if not wfc.is_collapsed:
        
        
        wfc.advance()
        img, tile, rot = wfc.next_img_to_tile
        loaded_img = pg.image.load(img) 
        img = pg.transform.rotate(loaded_img, -90*rot)
        screen.blit(img, (tile[1] * IMG_SIZE, tile[0] * IMG_SIZE))
        #screen.blit(socket_to_img[wfc.last_collapsed[1]], (wfc.last_collapsed[0][1] * IMG_SIZE, wfc.last_collapsed[0][0] * IMG_SIZE))
    pg.display.flip()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()