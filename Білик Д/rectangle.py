import math
from classabstr import Figure, Color
class Rectangle(Figure):
    def __init__(self, color: Color, height: float, width: float):
        super().__init__(color)
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2 * (self.height + self.width)