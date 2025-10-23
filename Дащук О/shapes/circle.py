import math
from .base import Shape

class Circle(Shape):
    def calculate_area(self) -> float:
        if len(self.shape_parameters) >= 1 and self.shape_parameters[0] > 0:
            r = self.shape_parameters[0]
            return math.pi * r * r
        return 0.0

    def calculate_perimeter(self) -> float:
        if len(self.shape_parameters) >= 1 and self.shape_parameters[0] > 0:
            r = self.shape_parameters[0]
            return 2 * math.pi * r
        return 0.0

    def get_shape_type(self) -> str:
        return "Circle"
