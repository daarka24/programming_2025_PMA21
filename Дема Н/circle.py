from shape import Shape
import math
from color import Color
class Circle(Shape):
    def __init__(self, color: Color, radius: float):
        super().__init__(color)
        self.radius = radius
    def area(self) -> float:
        return math.pi * self.radius * self.radius
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    def name(self):
        return f"Circle(radius - {self.radius})"