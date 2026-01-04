from physics.game_object import GameObject
import pygame
from pygame.math import Vector2

class Line(GameObject):
    def __init__(self):
        super().__init__()
        self.has_gravity = False
        self.normal = Vector2()
        self.start_point = (0,0)
        self.end_point = (0,0)

    def __init__(self, start_point, end_point, pixel_width):
        super().__init__()
        self.has_gravity = False
        self.start_point = start_point
        self.end_point = end_point
        self.normal.x = -1*(end_point[0]- start_point[0])
        self.normal.y = end_point[1] - start_point[1]
        self.pixel_width = pixel_width

    def draw(self, surface:pygame.Surface):
        pygame.draw.line(surface, (0xff, 0xff, 0xff), self.start_point, self.end_point, self.pixel_width)