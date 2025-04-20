import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, dt):
        angle = random.uniform(20, 50)
        one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)# + rotate
        two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)# - rotate
        one.velocity = 1.2 * self.velocity.rotate(angle) 
        two.velocity = 1.2 * self.velocity.rotate(-angle)
        self.kill()
