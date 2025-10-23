from math import pi
from shape_base import Shape
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius

    def describe(self):
        return self.color.apply_color("Circle")