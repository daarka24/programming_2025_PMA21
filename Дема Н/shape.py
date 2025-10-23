from abc import ABC, abstractmethod
import math
from color import Color
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
    def area(self) -> float:
        pass
    def perimeter(self) -> float:
        pass
    def name(self)-> str:
        pass
    def draw(self)-> str:
        return self.color.apply_color(self.name())

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
class Rectangle(Shape):
    def __init__(self, color: Color, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    def name(self):
        return f"Rectangle(width - {self.width}, height - {self.height})"

class Square(Rectangle):
    def __init__(self, color: Color, side: float):
        super().__init__(color, height = side, width = side)
        self.side = side
    def name(self):
        return f"Square(side - {self.side})"