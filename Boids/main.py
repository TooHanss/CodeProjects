import pygame
import math
from boid.boid import Boid
pygame.init()

IMAGE_PATH = r'Boids\boid\image\Boid.png'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BOID = Boid() 

clock = pygame.time.Clock()
run = True
pos = (100.0, 100.0)
while run:
    screen.fill((0, 0, 0))
    dx = 1.0
    dy = 1.0
    img = pygame.image.load(IMAGE_PATH).convert()
    
    magnitude = math.sqrt(dx**2 + dy**2)
    dx /= magnitude
    dy /= magnitude

    # Calculate the angle (in degrees)
    angle = math.degrees(math.atan2(-dy, dx)) - 90
    
    img = pygame.transform.rotate(img, angle)

    pos = (pos[0] + dx, pos[1] + dy)
    screen.blit(img, (pos))
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()