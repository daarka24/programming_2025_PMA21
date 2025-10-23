from typing import Optional, Type
from Abstraction.colors.black import BlackColor
from Abstraction.colors.red import RedColor
from Abstraction.colors.white import WhiteColor
from Abstraction.colors.base import Color
from Abstraction.shapes.base import Shape
from Abstraction.shapes.circle import Circle
from Abstraction.shapes.rectangle import Rectangle
from Abstraction.shapes.square import Square

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, color_type: str, data_file_path: str) -> Optional[Shape]:
        color_mapping: dict[str, Color] = {
            'black': BlackColor(),
            'red': RedColor(),
            'white': WhiteColor()
        }
        shape_mapping: dict[str, Type[Shape]] = {
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
