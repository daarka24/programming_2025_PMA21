import math
from classabstr import Figure, Color
from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, color: Color, side: float):
        super().__init__(color, height=side, width=side)