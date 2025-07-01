import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
import asteroidfield
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
        main()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
running = True

shootable = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroidfield = pygame.sprite.Group()

AsteroidField.containers = (updatable,)
Asteroid.containers = (asteroids, updatable, drawable)


Player.containers = (updatable, drawable)
Shot.containers =(shootable, updatable, drawable)

roid_field = AsteroidField()
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000

    screen.fill("black")

    updatable.update(dt)

    for asteroid in asteroids:
        if asteroid.collision(player):
            print("Game over!")
            sys.exit()

    for asteroid in asteroids:
        for bullet in shootable:
            if asteroid.collision(bullet):
                asteroid.split()


    for item in drawable:
        item.draw(screen)

    pygame.display.flip()
