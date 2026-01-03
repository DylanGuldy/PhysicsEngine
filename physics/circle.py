from physics.game_object import GameObject
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
    pygame.draw.circle(surface, (0x55, 0x55, 0x55), (self.position.x,  self.position.y), self.radius*2, self.pixel_width)
    text_font = pygame.font.Font(None, 18)
    text = text_font.render(f"{self.position.x},{self.position.y}", True, (255,255,255))
    surface.blit(text, (self.position.x+self.radius+20, self.position.y-self.radius/2))
    
