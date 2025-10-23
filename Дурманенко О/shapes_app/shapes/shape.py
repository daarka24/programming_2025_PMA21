from abc import ABC, abstractmethod
from typing import List
from shapes_app.colors.color import Color

class Shape(ABC):
    def __init__(self, color_implementation: Color, data_file_path: str):
        self.color_implementation = color_implementation
        self.data_file_path = data_file_path
        self.shape_parameters: List[float] = []
        self.load_shape_data()

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

    @abstractmethod
    def get_shape_type(self) -> str:
        pass

    def load_shape_data(self) -> None:
        try:
            with open(self.data_file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        numeric_value = float(line)
                        self.shape_parameters.append(numeric_value)
                    except ValueError:
                        print(f"Warning: Could not convert '{line}' to a number, skipping.")
        except Exception:
            print(f"Error: Could not read the file at {self.data_file_path}.")
            self.shape_parameters = []

    def display_shape_info(self) -> str:
        shape_info = [
            f"Shape Type: {self.get_shape_type()}",
            f"Color: {self.color_implementation.get_color_description()}",
        ]
        try:
            area = self.calculate_area()
            shape_info.append(f"Area: {area:.2f}")
        except Exception:
            shape_info.append("Area: Cannot be calculated.")
        try:
            perimeter = self.calculate_perimeter()
            shape_info.append(f"Perimeter: {perimeter:.2f}")
        except Exception:
            shape_info.append("Perimeter: Cannot be calculated.")
        return "\n".join(shape_info)