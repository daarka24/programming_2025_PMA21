from shape import Shape
from color import Color
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