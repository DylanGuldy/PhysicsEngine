from pygame.math import Vector2
from circle import Circle
from line import Line

def does_collide(Line: line_object, Circle: circle_object) -> bool:
  line_object.unit_normal.dot(line_object.position - circle_object.position)
  return False