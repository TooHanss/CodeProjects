import pygame
import math
from boid.boid import Boid
pygame.init()

IMAGE_PATH = r'Boids\boid\image\Boid.png'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
SCHOOL = []
NUM_BOIDS = 100
for i in range(NUM_BOIDS):
    boid = Boid(screen, SCHOOL)
    SCHOOL.append(boid) 

clock = pygame.time.Clock()
run = True
pos = (100.0, 100.0)

while run:
    screen.fill((0, 0, 0))
    for boid in SCHOOL:
        boid.update()
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()