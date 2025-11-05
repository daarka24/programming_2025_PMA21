import math
from .rectangle import Rectangle
from color import Color


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        super().__init__(side, side, color)
        self.side = side


