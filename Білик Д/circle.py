import math
from classabstr import Figure, Color
class Circle(Figure):
    def __init__(self, color: Color, radius: float):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return math.pi * pow(self.radius, 2)
    def perimeter(self):
        return math.pi * (self.radius * 2)