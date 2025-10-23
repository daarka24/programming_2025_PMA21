from abc import ABC, abstractmethod
from colors.colors import Color

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    def get_info(self):
        return f"{self.__class__.__name__} ({self.color.get_color_name()}) - Периметр: {self.calculate_perimeter():.2f}, Площа: {self.calculate_area():.2f}"
