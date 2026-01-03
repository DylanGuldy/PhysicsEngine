import pygame
from physics.circle import Circle
from physics.line import Line

class Game:
  def __init__(self, window_width=800, window_height=600):
      self.window_width = window_width
      self.window_height = window_height
      pygame.init()
      self.screen = pygame.display.set_mode((self.window_width, self.window_height))
      self.clock = pygame.time.Clock()
      self.gravity = -10

  def main_loop(self) -> None:
    running = True

    objects = self.build_objects()
    
    self.set_objects_gravity(objects)

    time_between_frames = 1
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      # Black screen
      self.screen.fill((0,0,0))

      for object in objects:
        object.update(time_between_frames)
        object.draw(self.screen)
        
      time_between_frames = self.clock.tick(60) / 1000
      pygame.display.flip()      

    pygame.quit()

  def set_objects_gravity(self, objects):
      for obj in objects:
        if obj.has_gravity:
          obj.gravity = self.gravity

  def build_objects(self):
      objects = []
      circle = Circle(self.window_width/2, 0, 10, 1)
      circle.has_gravity = True
      ground = Line((1, self.window_height-10), (self.window_width, self.window_height-10), 1)
      objects.append(circle)
      objects.append(ground)
      return objects



if __name__ == "__main__":
  print("loop.py")