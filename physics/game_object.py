from pygame.math import Vector2

class GameObject:
  def __init__(self) -> None:
    self.has_gravity = False
    self.gravity = Vector2()
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

    # slow mo, 1 is no slow down
    self.slow_down = .01

  def draw(self):
    pass

  def update(self, time_since_last_frame):
    if self.has_gravity:
      # below changes to force * mass * gravity if we add mass
      self.force = self.force + self.gravity
    # below line should change to force / mass * dt <- if we decide to go with mass
    self.velocity = self.velocity + self.force * time_since_last_frame
    self.position = self.position + self.velocity * self.slow_down
    # reset force
    self.force = Vector2()
    print(f"Velocity {self.velocity}")
    print(f"position {self.position}")

  def get_distance_between_objects(self, other_obj) -> int:
    pass

  def add_collision_callback(self, callback: callable):
    self._callbacks.append(callback)

  def del_collision_callback(self, callback: callable):
    self._callbacks.remove(callback)
    
  def collision_event(self, other_object, **kwargs):
    for registered_callback in self._callbacks:
      registered_callback(other_object, kwargs)