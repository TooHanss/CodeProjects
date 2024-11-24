import pygame

IMAGE_PATH = r'Boids\boid\image\Boid.png'

class Boid:
    def __init__(self):
        self.img = pygame.image.load(IMAGE_PATH).convert()
        self.scale = (0.1, 0.1)
        pygame.transform.scale(self.img, self.scale)
        self.pos = (100, 100)

    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def move(self):
        self.pos = (self.pos[0], self.pos[1] + 1)
