import pygame 
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #Initialize Pygame
    pygame.init()
    pygame.display.set_caption('Asteroids')
    time_clock= pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group() #all objects that can be updated
    drawable = pygame.sprite.Group() #all objects that can be drawned
    asteroids = pygame.sprite.Group()
    
    #add to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroids_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0 #delta time 
     
    #game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
            
        screen.fill((0, 0, 0))
        
        for object in updatable:
            object.update(dt)
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        #limit the framerate to 60FPS
        tick = time_clock.tick(60)
        dt = tick / 1000
        
        
        
if __name__ == "__main__":
    main()
    
    
    