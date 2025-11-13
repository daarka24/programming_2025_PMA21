from abc import ABC, abstractmethod
from color import Color


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

    def draw(self) -> str:
        return f"{self.__class__.__name__} with color: {self.color.apply_color()}"
