from physics.game_object import GameObject
import pygame
from pygame.math import Vector2

class Line(GameObject):
    def __init__(self):
        super().__init__()
        self.has_gravity = False
        self.normal = Vector2()

    def __init__(self, x_location, y_location, pixel_width):
        super().__init__()
        self.has_gravity = False
        self.position.x = x_location
        self.position.y = y_location
        self.pixel_width = pixel_width

    def draw(self, surface:pygame.Surface):
        pygame.draw.line(surface, (0xff, 0xff, 0xff), self.position.x, self.position.y, self.pixel_width)