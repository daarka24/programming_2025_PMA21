class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def describe(self):
        return f"{self.__class__.__name__} має колір {self.color.fill()}"
