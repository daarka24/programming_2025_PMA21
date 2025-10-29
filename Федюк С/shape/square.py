from shape.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, rect, color):
        side = rect.width + rect.height
        super().__init__(side, side, color)
