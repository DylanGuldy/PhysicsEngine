import pygame

class GameObject:
  def __init__(self) -> None:
    self.has_gravity = False
    self.has_collision = False
    self.speed = 0
    self.acceleration = 0 
    self._callbacks = []
    self.x = 0
    self.y = 0
    self.pixel_width = 1

  def draw(self):
    pass

  def add_collision_callback(self, callback: callable):
    self._callbacks.append(callback)

  def del_collision_callback(self, callback: callable):
    self._callbacks.remove(callback)
    
  def collision_event(self, other_object, **kwargs):
    for registered_callback in self._callbacks:
      registered_callback(other_object, kwargs)