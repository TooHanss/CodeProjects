import pygame
from boid.boid import Boid
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BOID = Boid() 

clock = pygame.time.Clock()
run = True
while run:
    screen.fill((0,0,0))
    BOID.draw(screen=screen)
    BOID.move()
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()