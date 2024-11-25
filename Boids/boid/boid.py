import pygame
import math
import random
# Need to store image when rotatin or when it blits it is the unrotated version
# Calculate velocity
# Orient to velocity
# Screen Wrap

class Boid:
    def __init__(self, screen: pygame.Surface, school):
        self.screen = screen
        self.school = school
        self.pos = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height())) 
        self.max_speed = 5.0
        self.min_speed = 3.0
        self.vel = pygame.Vector2(random.uniform(-2.0, 2.0), random.uniform(-2.0, 2.0))
        self.acc = pygame.Vector2()
        self.angle = 0
        self.perception_radius = 25
        self.max_alignment = 0.1

    def alignment(self):
        mate_velocities = []
        for boid in self.school:
            if self.pos.distance_to(boid.pos) > self.perception_radius:
                continue
            if boid == self:
                continue
            mate_velocities.append(boid.vel)
        if mate_velocities:
            avg_velocity = pygame.Vector2(0.0, 0.0)
            for vel in mate_velocities:
                avg_velocity += vel
            avg_velocity = avg_velocity / len(mate_velocities)
            accel = avg_velocity - self.vel
            if accel.magnitude() > 0:
                accel = accel.clamp_magnitude(self.max_alignment)
            return accel
        return pygame.Vector2(0.0, 0.0)

    def cohesion(self):
        pass

    def separation(self):
        pass

    def perception(self):
        pass
    
    def update(self):
        self.acc = self.alignment()
        self.vel = self.vel + self.acc
        self.vel = self.vel.clamp_magnitude(self.min_speed, self.max_speed)
        self.pos = self.pos + self.vel
        if self.pos.x > self.screen.get_width():
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.screen.get_width()
        if self.pos.y > self.screen.get_height():
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = self.screen.get_height()
        pygame.draw.circle(self.screen, (255, 255, 255), self.pos, 5)
        pass