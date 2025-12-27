import pygame
from physics.circle import Circle

class Game:
  def __init__(self, window_width=800, window_height=600):
      self.window_width = window_width
      self.window_height = window_height
      pygame.init()
      self.screen = pygame.display.set_mode((self.window_width, self.window_height))
      self.clock = pygame.time.Clock()

  def main_loop(self) -> None:

    running = True
    objects = []
    circle = Circle(self.window_width/2, self.window_height/2, 10, 1)
    objects.append(circle)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      # Black screen
      self.screen.fill((0,0,0))

      for object in objects:
        object.draw(self.screen)
        
      pygame.draw.line(self.screen, (255, 255, 255), (1, self.window_height-10), (self.window_width, self.window_height-10))

      pygame.display.flip()
      self.clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
  print("loop.py")