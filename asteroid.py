import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import (ASTEROID_MIN_RADIUS,
                       ASTEROID_ACCELERATION)


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white ", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity_asteroid_one = self.velocity.rotate(angle)
            velocity_asteroid_two = self.velocity.rotate(-angle)
            asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_one.velocity = velocity_asteroid_one * ASTEROID_ACCELERATION
            asteroid_two.velocity = velocity_asteroid_two * ASTEROID_ACCELERATION
            self.kill()