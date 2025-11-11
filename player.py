import pygame
import math
from shot import Shot
from circleshape import CircleShape
from constants import (PLAYER_RADIUS, 
                       PLAYER_TURN_SPEED,
                       PLAYER_SPEED,
                       PLAYER_SHOOT_SPEED,
                       PLAYER_SHOOT_COOLDOWN)

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * dt

    def strafe(self, dt: float) -> None:
        right = pygame.Vector2(1, 0)
        self.position += right * PLAYER_SPEED * dt

    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= dt

        click = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dircection = pygame.Vector2(mouse_x, mouse_y) - self.position
        self.rotation = -math.degrees(math.atan2(dircection.x, dircection.y))

        if keys[pygame.K_a]:
            self.strafe(dt * (-1))
        if keys[pygame.K_d]:
            self.strafe(dt)
        if keys[pygame.K_w]:
            self.move(dt * (-1))
        if keys[pygame.K_s]:
            self.move(dt)
        if click[0]:
            if self.shot_cooldown_timer < 0:
                self.shoot()
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN
        
        