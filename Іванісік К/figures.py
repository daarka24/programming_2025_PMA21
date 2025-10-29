from abc import ABC, abstractmethod
import math
from colors import Color

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    def draw(self) -> str:
        # Зверни увагу: тут apply_color() викликається без аргументів
        return self.color.apply_color()

class Circle(Shape):
    def __init__(self, color: Color, radius: float):
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def get_name(self) -> str:
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, color: Color, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_name(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Shape):
    def __init__(self, color: Color, side: float):
        super().__init__(color)
        self.side = side

    def area(self) -> float:
        return self.side * self.side

    def perimeter(self) -> float:
        return 4 * self.side

    def get_name(self) -> str:
        return f"Square(side={self.side})"