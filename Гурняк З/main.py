from abc import ABC, abstractmethod
import math


class Color(ABC):
    @abstractmethod
    def apply_color(self) -> str:
        pass


class Red(Color):
    def apply_color(self) -> str:
        return "Red"


class Blue(Color):
    def apply_color(self) -> str:
        return "Blue"


class Green(Color):
    def apply_color(self) -> str:
        return "Green"


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


class Circle(Shape):
    def __init__(self, radius: float, color: Color):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: Color):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        super().__init__(side, side, color)
        self.side = side


if __name__ == "__main__":
    red = Red()
    blue = Blue()
    green = Green()

    circle = Circle(5, red)
    rectangle = Rectangle(4, 6, blue)
    square = Square(3, green)

    shapes = [circle, rectangle, square]

    for shape in shapes:
        print(shape.draw())
        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")
        print()
