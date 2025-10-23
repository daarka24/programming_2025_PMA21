from .rectangle import Rectangle
from shapes_app.colors.color import Color

class Square(Rectangle):
    def __init__(self, color_implementation: Color, data_file_path: str):
        super().__init__(color_implementation, data_file_path)
        if len(self.shape_parameters) > 0:
            self.shape_parameters = [self.shape_parameters[0], self.shape_parameters[0]]

    def get_shape_type(self) -> str:
        return "Square"