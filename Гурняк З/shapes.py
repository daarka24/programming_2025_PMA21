import math
from shape import Shape
from color import Color


class Circle(Shape):
    def __init__(self, radius: float, color: Color):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: Color):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        super().__init__(side, side, color)
