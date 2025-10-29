from shape.shape import Shape

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        pi = 3.14159
        return pi * self.radius ** 2

    def perimeter(self):
        pi = 3.14159
        return 2 * pi * self.radius
