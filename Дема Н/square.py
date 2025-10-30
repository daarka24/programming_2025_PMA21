from rectangle import Rectangle
from color import Color
class Square(Rectangle):
    def __init__(self, color: Color, side: float):
        super().__init__(color, height = side, width = side)
        self.side = side
    def name(self):
        return f"Square(side - {self.side})"