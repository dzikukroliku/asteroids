import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (0xFF, 0xFF, 0xFF), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill() # kill original asteroid object
        if self.radius <= ASTEROID_MIN_RADIUS: # do nothing if smallest asteroid size achieved
            return

        random_angle = random.uniform(20, 50) # generate random new angle for new asteroids
        new_vector1 = self.velocity.rotate(random_angle) # create new vector w. random angle for new asteroid
        new_vector2 = self.velocity.rotate(-random_angle) # same as above
        new_radius = (self.radius - ASTEROID_MIN_RADIUS) # set new radius variable

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) # spawn new asteroid object 1 w. new paramenters on old asteroid position.
        asteroid1.velocity = new_vector1 * 1.2 # give new vector & velocity increase to new asteroid 1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius) # repeat above code for asteroid obj. 2.
        asteroid2.velocity = new_vector2 * 1.2 # same as above but for asteroid obj. 2.