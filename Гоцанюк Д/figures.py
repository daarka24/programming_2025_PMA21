from abc import ABC, abstractmethod
import math
from colors import BaseColor

class Figure(ABC):
    def __init__(self, color_obj: BaseColor):
        self.color_obj = color_obj

    @abstractmethod
    def calc_area(self) -> float:
        pass

    @abstractmethod
    def calc_perimeter(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def get_color_info(self) -> str:
        return self.color_obj.fill()

class Circle(Figure):
    def __init__(self, color_obj: BaseColor, r: float):
        super().__init__(color_obj)
        self.r = r

    def calc_area(self) -> float:
        return math.pi * (self.r ** 2)

    def calc_perimeter(self) -> float:
        return 2 * math.pi * self.r

    def __str__(self) -> str:
        return f"Circle(radius={self.r})"

class Rectangle(Figure):
    def __init__(self, color_obj: BaseColor, w: float, h: float):
        super().__init__(color_obj)
        self.w = w
        self.h = h

    def calc_area(self) -> float:
        return self.w * self.h

    def calc_perimeter(self) -> float:
        return 2 * (self.w + self.h)

    def __str__(self) -> str:
        return f"Rectangle(width={self.w}, height={self.h})"

class Square(Figure):
    def __init__(self, color_obj: BaseColor, s: float):
        super().__init__(color_obj)
        self.s = s

    def calc_area(self) -> float:
        return self.s * self.s

    def calc_perimeter(self) -> float:
        return 4 * self.s

    def __str__(self) -> str:
        return f"Square(side={self.s})"