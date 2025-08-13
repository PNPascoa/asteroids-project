import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x,y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    player = Player(x,y, PLAYER_RADIUS)
  
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000




updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)


if __name__ == "__main__":
    main()
