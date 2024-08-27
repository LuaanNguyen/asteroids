import pygame 
from constants import * 
from player import *

def main():
    #Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    time_clock= pygame.time.Clock()
    dt = 0 #delta time 
     
    #game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
            
        screen.fill((0, 0, 0))
        player.draw(screen)    
        pygame.display.flip()
        
        #limit the framerate to 60FPS
        tick = time_clock.tick(60)
        dt = tick / 1000
        
        
        
if __name__ == "__main__":
    main()
    
    
    