from pygame.math import Vector2

class GameObject:
  def __init__(self) -> None:
    self.has_gravity = False
    self.gravity = 0
    self.has_collision = False
    # [x component, y component] 
    self.velocity = Vector2()
    # [x component, y component]
    self.acceleration = Vector2() 
    # [x component, y component]
    self.force = Vector2()
    self._callbacks = []
    self.position = Vector2()
    self.pixel_width = 1

  def draw(self):
    pass

  def update(self, time_since_last_frame):
    if self.has_gravity:
      # sub the gravity from the y component
      self.force.y = self.force.y - self.gravity
    self.velocity = self.velocity + self.force # / mass <- if we decide to go with mass
    self.velocity = self.velocity * time_since_last_frame
    self.position = self.position + self.velocity * time_since_last_frame
    # reset force
    self.force = Vector2()
    print(f"Velocity {self.velocity}")
    print(f"position {self.position}")

  def add_collision_callback(self, callback: callable):
    self._callbacks.append(callback)

  def del_collision_callback(self, callback: callable):
    self._callbacks.remove(callback)
    
  def collision_event(self, other_object, **kwargs):
    for registered_callback in self._callbacks:
      registered_callback(other_object, kwargs)