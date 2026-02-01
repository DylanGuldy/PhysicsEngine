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
        

      self.stop_circle(objects[3], objects[0])
      self.stop_circle(objects[3], objects[1])
      self.stop_circle(objects[3], objects[2])

      slow_time_factor = 500
      time_between_frames = self.clock.tick(60) #/ slow_time_factor

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
      circle2 = Circle(self.window_width/2-80, 0, 20, 1)
      circle2.has_gravity = True
      circle3 = Circle(self.window_width/2+40, 0, 20, 1)
      circle3.has_gravity = True
      ground = Line((1, self.window_height-380), (self.window_width, self.window_height-10), 1)
      # ground = Line((1, self.window_height-20), (self.window_width, self.window_height-20), 1)
      objects.append(circle)
      objects.append(circle2)
      objects.append(circle3)
      objects.append(ground)
      return objects

  #####
  #####DEBUG
  def stop_circle(self, line:Line, circle: Circle):
    distance = line.get_distance_between_objects(circle)
    if(abs(distance) <= circle.radius):
      circle.has_gravity = False
      circle.velocity = Vector2()
      distance_past_line = circle.radius - abs(distance)
      x_to_move = distance_past_line * line.unit_normal.x
      y_to_move = distance_past_line * line.unit_normal.y
      circle.position.x -= x_to_move
      circle.position.y -= y_to_move
      
      draw_text(f"dot: {line.get_distance_between_objects(circle)}", 
                 18, circle.position.x+10, circle.position.y-10, self.screen)
      

  #####
  #####

if __name__ == "__main__":
  game = Game()
  game.main_loop()