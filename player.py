from circleshape import *
from constants import *
from shot import *
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate((-1 * dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.position)
        self.position += self.update(forward * PLAYER_SPEED * dt)

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.draw(screen)
        # shot.draw(dt, screen)
        velocity = pygame.Vector2(0, 1)
        # self.rotate(dt * PLAYER_SHOOT_SPEED)
        self.position += velocity * PLAYER_SHOOT_SPEED * dt

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
