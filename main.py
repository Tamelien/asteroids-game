import pygame
from sys import exit
from logger import (log_state,
                    log_event)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (SCREEN_HEIGHT, 
                       SCREEN_WIDTH,)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astroidfield = AsteroidField()

    dt = 0
    clock = pygame.time.Clock() 

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black", rect=None, special_flags=0)
        
        
        for drawing in drawable:
            drawing.draw(screen)
        
        updatable.update(dt)
                
        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                log_event("player_hit")
                print("Game over!")
                exit()
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
