from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)

    def describe(self):
        return self.color.apply_color("\nSquare")