import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x,y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroid_field = AsteroidField()
    player
  
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


##Groups

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
#Containers
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)
##
if __name__ == "__main__":
    main()
