import math
from .shape import Shape

class Circle(Shape):
    def calculate_area(self) -> float:
        try:
            if len(self.shape_parameters) > 0 and self.shape_parameters[0] > 0:
                radius = self.shape_parameters[0]
                return math.pi * radius * radius
            return 0.0
        except Exception:
            return 0.0

    def calculate_perimeter(self) -> float:
        try:
            if len(self.shape_parameters) > 0 and self.shape_parameters[0] > 0:
                radius = self.shape_parameters[0]
                return 2 * math.pi * radius
            return 0.0
        except Exception:
            return 0.0

    def get_shape_type(self) -> str:
        return "Circle"