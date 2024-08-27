import pygame 
from constants import * 
from player import *

#Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteroids')

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    time_clock= pygame.time.Clock()
    dt = 0 #delta time 
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    #game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
            
        screen.fill((0, 0, 0))
        player.draw(screen)    
        pygame.display.flip()
        tick = time_clock.tick(60)
        dt = tick / 1000
        
if __name__ == "__main__":
    main()
    
    
    