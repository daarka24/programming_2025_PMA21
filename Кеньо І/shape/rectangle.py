import math
from .shape import Shape
from color import Color


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: Color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)




