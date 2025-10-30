from abc import ABC, abstractmethod
from color import Color
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
    def area(self) -> float:
        pass
    def perimeter(self) -> float:
        pass
    def name(self)-> str:
        pass
    def draw(self)-> str:
        return self.color.apply_color(self.name())