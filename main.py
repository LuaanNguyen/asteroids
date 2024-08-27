import pygame 
from constants import * 

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
    
    #game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
        tick = time_clock.tick(60)
        dt = tick / 1000
        
if __name__ == "__main__":
    main()
    
    
    