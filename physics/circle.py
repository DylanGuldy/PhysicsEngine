from pysics.game_object import GameObject
import pygame

class Circle(GameObject):
  def __init__(self) -> None:
    super().__init__()
    # distance in # pixels?
    self.radius = 0
  def __init__(self, x_location, y_location, radius, pixel_width=1) -> None:
    super().__init__()
    self.x = x_location
    self.y = y_location
    self.radius = radius
    self.pixel_width = pixel_width

  def update(self):
    pass

  def draw(self, surface:pygame.surface):
    pygame.draw.circle(surface, (0x55, 0x55, 0x55), (self.x,  self.y), self.radius*2, self.pixel_width)
