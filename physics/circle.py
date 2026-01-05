from physics.game_object import GameObject
from utils.utils import draw_text
import pygame

class Circle(GameObject):
  def __init__(self) -> None:
    super().__init__()
    # distance in # pixels?
    self.radius = 0

  def __init__(self, x_location, y_location, radius, pixel_width=1) -> None:
    super().__init__()
    self.position.x = x_location
    self.position.y = y_location
    self.radius = radius
    self.pixel_width = pixel_width

  def draw(self, surface:pygame.surface):
    pygame.draw.circle(surface, (0x55, 0x55, 0x55), (self.position.x,  self.position.y), self.radius, self.pixel_width)
    draw_text(f"{self.position.x},{self.position.y}",18, self.position.x+self.radius+20, self.position.y-self.radius/2, surface)
    
