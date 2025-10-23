from math import pi

class Color:
    def __init__(self, color: str):
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}"

class Pink(Color):
    def __init__(self):
        super().__init__("Pink")

class Blue(Color):
    def __init__(self):
        super().__init__("Blue")

class Green(Color):
    def __init__(self):
        super().__init__("Green")

class Shape:
    def __init__(self, sides: list, color: Color):
        self.sides = sides
        self.color = color

    def __str__(self):
        return f"Shape: {self.__class__.__name__}, Sides: {self.sides}, Perimeter: {self.perimeter}, Area: {self.area}, Color: {self.color}"

    @property
    def perimeter(self) -> float:
        return sum(self.sides)

    @property
    def area(self) -> None:
        return None

class Circle(Shape):
    def __init__(self, r: float, color: Color):
        self.radius = r
        super().__init__(None,color)

    def __str__(self):
        return f"Shape: {self.__class__.__name__}, Radius: {self.radius}, Perimeter: {self.perimeter}, Area: {self.area}, Color: {self.color}"

    @property
    def perimeter(self) -> float:
        return 2*pi*self.radius

    @property
    def area(self) -> float:
        return pi*(self.radius**2)

class Rectangle(Shape):
    def __init__(self,sides: list, color: Color ):
        if len(sides) != 2:
            raise ValueError("фігура не є прямокутником")
        super().__init__(sides*2, color)

    def __str__(self):
        return f"Shape: {self.__class__.__name__}, Sides: {self.sides[:2]}, Perimeter: {self.perimeter}, Area: {self.area}, Color: {self.color}"

    @property
    def area(self) -> float:
        return self.sides[0]*self.sides[1]

class Square(Rectangle):
    def __init__(self, sides: list, color: Color):
        if len(sides) != 1:
            raise ValueError("фігура не є квадратом")
        super().__init__(sides * 2, color)

    def __str__(self):
        return f"Shape: {self.__class__.__name__}, Side: {self.sides[0]}, Perimeter: {self.perimeter}, Area: {self.area}, Color: {self.color}"