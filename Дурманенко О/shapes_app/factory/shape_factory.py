from shapes_app.colors.black_color import BlackColor
from shapes_app.colors.red_color import RedColor
from shapes_app.colors.white_color import WhiteColor

from shapes_app.shapes.circle import Circle
from shapes_app.shapes.rectangle import Rectangle
from shapes_app.shapes.square import Square

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, color_type: str, data_file_path: str):
        color_mapping = {
            'black': BlackColor(),
            'red': RedColor(),
            'white': WhiteColor()
        }
        shape_mapping = {
            'circle': Circle,
            'rectangle': Rectangle,
            'square': Square
        }
        try:
            color_instance = color_mapping.get(color_type.lower())
            if not color_instance:
                print(f"Unknown color: {color_type}, using default Black.")
                color_instance = BlackColor()
            shape_class = shape_mapping.get(shape_type.lower())
            if not shape_class:
                print(f"Unknown shape: {shape_type}, creation skipped.")
                return None
            return shape_class(color_instance, data_file_path)
        except Exception:
            print("An unexpected error occurred while creating the shape.")
            return None