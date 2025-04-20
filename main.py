import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    AsteroidField()
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        updatable.update(dt)
        screen.fill(color='black')
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ =="__main__":
    main()