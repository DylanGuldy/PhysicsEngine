#!./venv/bin/python3
from engine import Game
from pygame.math import Vector2
if __name__ == "__main__":
  print("Hello World")
  game = Game()
  game.main_loop()






  # first_line_point = Vector2(1, 1)
  # second_line_point = Vector2(0, 0)
  # line_vector = Vector2(first_line_point-second_line_point)
  # perpendicular_vector = Vector2(-line_vector.y, line_vector.x).normalize()
  # print(f"Perpendicular line is: {perpendicular_vector}")
  # test_vector = Vector2(2, 2)
  # print(f"Distance away from line: {abs(perpendicular_vector.dot(test_vector-first_line_point))}")
  # print(f"X component into the line: {perpendicular_vector.dot(test_vector)}")
  # y_detect_vector = Vector2(-perpendicular_vector.y, perpendicular_vector.x)
  # print(f"Y component into the line: {y_detect_vector.dot(test_vector)}")