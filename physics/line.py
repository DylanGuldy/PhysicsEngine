from physics.game_object import GameObject
from physics.circle import Circle
from utils.utils import draw_text
import pygame
from pygame.math import Vector2

class Line(GameObject):
    def __init__(self):
        super().__init__()
        self.has_gravity = False
        self.unit_normal = Vector2()
        self.start_point = (0,0)
        self.end_point = (0,0)

    def __init__(self, start_point:tuple[int, int], end_point:tuple[int, int], pixel_width):
        super().__init__()
        self.has_gravity = False
        self.start_point = start_point
        self.end_point = end_point
        self.unit_normal = Vector2(-(end_point[1]-start_point[1]), (end_point[0]-start_point[0])).normalize()
        self.position = Vector2(int((end_point[0]+start_point[0])/2), 
                                int((end_point[1]+start_point[1])/2))
        print(f"unit normal is: {self.unit_normal}")
        self.pixel_width = pixel_width

    def draw(self, surface:pygame.Surface):
        pygame.draw.line(surface, (0xff, 0xff, 0xff), self.start_point, self.end_point, self.pixel_width)
       
    def get_distance_between_objects(self, other_object: Circle):
        return self.unit_normal.dot(other_object.position - self.position)