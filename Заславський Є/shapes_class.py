from math import pi

class Color:
    def apply_color(self):
        return "no color"


class Red(Color):
    def apply_color(self):
        return "red"


class Blue(Color):
    def apply_color(self):
        return "blue"


class Green(Color):
    def apply_color(self):
        return "green"

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0

    def perimeter(self):
        return 0

    def describe(self):
        return f"{self.__class__.__name__} color {self.color.apply_color()}"


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = float(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)
