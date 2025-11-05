import math
from abc import ABC, abstractmethod
from color import Color


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def show_details(self, filename):
        with open(filename, 'a') as file:

            file.write(f"Shape {self.__class__.__name__}")
            file.write('\n')
            file.write(f"Color {self.color.apply_color()}")
            file.write('\n')

            file.write(f"Square: {self.area()}")
            file.write('\n')

            file.write(f"Perimeter: {self.perimeter()}")
            file.write('\n')



