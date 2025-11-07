import pygame
from logger import log_state
from player import Player
from asteroid import Asteroid
from constants import (SCREEN_HEIGHT, 
                       SCREEN_WIDTH,)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (astroids, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
