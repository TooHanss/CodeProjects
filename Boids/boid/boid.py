import pygame
import math
# Need to store image when rotatin or when it blits it is the unrotated version
# Calculate velocity
# Orient to velocity
# Screen Wrap
IMAGE_PATH = r'Boids\boid\image\Boid.png'

class Boid:
    def __init__(self):
        self.img = pygame.image.load(IMAGE_PATH).convert()
        self.scale = (0.1, 0.1)
        pygame.transform.scale(self.img, self.scale)
        self.pos = (100, 100)
        self.speed = (1.0)
        self.dir = (1.0, 1.0)
        self.angle = 0

    def draw(self, screen):
        screen.blit(self.img, self.pos)

    def move(self):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])

    def update(self, screen):
        self.move()
        self.update_angle()
        self.draw(screen=screen)
        

    def update_angle(self):
        magnitude = math.sqrt(self.dir[0]*2 + self.dir[1]*2)
        mag_x = self.dir[0] / magnitude
        mag_y = self.dir[1] / magnitude

        # Calculate the angle (in degrees)
        self.angle = math.degrees(math.atan2(-mag_x, mag_y)) - 90
        print(self.angle)
        pygame.transform.rotate(self.img, self.angle)
