from .rectangle import Rectangle

class Square(Rectangle):
    def calculate_area(self) -> float:
        if len(self.shape_parameters) >= 1:
            a = self.shape_parameters[0]
            return a * a if a > 0 else 0.0
        return 0.0

    def calculate_perimeter(self) -> float:
        if len(self.shape_parameters) >= 1:
            a = self.shape_parameters[0]
            return 4 * a if a > 0 else 0.0
        return 0.0

    def get_shape_type(self) -> str:
        return "Square"
