from .shape import Shape

class Rectangle(Shape):
    def calculate_area(self) -> float:
        try:
            if len(self.shape_parameters) >= 2:
                a, b = self.shape_parameters[0], self.shape_parameters[1]
                if a > 0 and b > 0:
                    return a * b
            return 0.0
        except Exception:
            return 0.0

    def calculate_perimeter(self) -> float:
        try:
            if len(self.shape_parameters) >= 2:
                a, b = self.shape_parameters[0], self.shape_parameters[1]
                if a > 0 and b > 0:
                    return 2 * (a + b)
            return 0.0
        except Exception:
            return 0.0

    def get_shape_type(self) -> str:
        return "Rectangle"