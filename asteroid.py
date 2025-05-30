from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ran_angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(ran_angle)
            vec2 = self.velocity.rotate(-ran_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroids1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroids1.velocity = vec1*1.2
            new_asteroids2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroids2.velocity = vec2*1.2