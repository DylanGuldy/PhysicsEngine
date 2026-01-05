import pygame
from pygame.math import Vector2
from physics.circle import Circle
from physics.line import Line
from utils.utils import draw_text

class Game:
  def __init__(self, window_width=800, window_height=600):
      self.window_width = window_width
      self.window_height = window_height
      pygame.init()
      self.screen = pygame.display.set_mode((self.window_width, self.window_height))
      self.clock = pygame.time.Clock()
      self.gravity = Vector2(0, 10)

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
        
      if(abs(objects[1].get_distance_between_objects(objects[0])) <= objects[0].radius):
         objects[0].has_gravity = False
         objects[0].velocity = Vector2()
         objects[0].position.y = objects[1].position.y - objects[0].radius
      draw_text(f"dot: {objects[1].get_distance_between_objects(objects[0])}", 
                18, objects[1].position.x+10, objects[1].position.y-10, self.screen)
      

      time_between_frames = self.clock.tick(60) / 1000

      pygame.display.flip()

    pygame.quit()

  def set_objects_gravity(self, objects):
      for obj in objects:
        if obj.has_gravity:
          obj.gravity = self.gravity

  def build_objects(self):
      objects = []
      circle = Circle(self.window_width/2-40, 0, 20, 1)
      circle.has_gravity = True
      ground = Line((1, self.window_height-240), (self.window_width, self.window_height-10), 1)
      objects.append(circle)
      objects.append(ground)
      return objects

if __name__ == "__main__":
  print("loop.py")