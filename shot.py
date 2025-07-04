import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = velocity

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
