import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Init groups etc. below

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable) # groups updatable & drawable with Player class
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) # init Player variable
    clock = pygame.time.Clock() # time variable
    dt = 0 # init delta time

    Shot.containers = (shot, updatable, drawable) # group shot.py with updatable,drawable
    Asteroid.containers = (asteroids, updatable, drawable) # groups asteroids, updatable, drawable with Asteroids class
    AsteroidField.containers = (updatable,) # group updatable with AsteroidField class
    asteroidfield = AsteroidField()

    while True: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # key-press exit event
                return
        
        dt = clock.tick(60) / 1000 # cap FPS at 60

        updatable.update(dt) # update something
        for asteroid in asteroids: # loop through asteroids group
            if asteroid.collide(player): # check for collision with player
                print("Game over!")
                sys.exit() # exit game
        
            for s in shot: 
                if asteroid.collide(s):
                    asteroid.split()
                    s.kill()
        
        screen.fill((0,0,0)) # fill screen with color:black
        for d in drawable: # draw player
            d.draw(screen) # works if .draw() method exists
        pygame.display.flip() # flip display


if __name__ == "__main__":
    main()