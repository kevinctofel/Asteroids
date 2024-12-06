import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)
    player = Player(x, y)
    asteroid = AsteroidField()
    # shot = shots_group()
    clock = pygame.time.Clock()
    dt = 0
    ("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for asteroid_object in asteroids_group:
            for bullet_object in shots_group:
                if bullet_object.collision_check(asteroid_object):
                    bullet_object.kill()
                    asteroid_object.kill()
            if asteroid_object.collision_check(player):
                print("Game over")
                sys.exit()

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        # player.update(dt)
        pygame.display.flip()
        # print(pygame.Color.r, player.x, player.y)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
