from .base import Shape

class Rectangle(Shape):
    def calculate_area(self) -> float:
        if len(self.shape_parameters) >= 2:
            w, h = self.shape_parameters[:2]
            return w * h if w > 0 and h > 0 else 0.0
        elif len(self.shape_parameters) == 1:
            a = self.shape_parameters[0]
            return a * a if a > 0 else 0.0
        return 0.0

    def calculate_perimeter(self) -> float:
        if len(self.shape_parameters) >= 2:
            w, h = self.shape_parameters[:2]
            return 2 * (w + h) if w > 0 and h > 0 else 0.0
        elif len(self.shape_parameters) == 1:
            a = self.shape_parameters[0]
            return 4 * a if a > 0 else 0.0
        return 0.0

    def get_shape_type(self) -> str:
        return "Rectangle"
