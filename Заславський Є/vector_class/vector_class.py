class Vector:
    def __init__(self, coords):
        self.coords = coords

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.coords, other.coords)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.coords, other.coords)])

    def __mul__(self, other):
        return Vector([a * b for a, b in zip(self.coords, other.coords)])
#zip об’єднує їх поелементно в пари а і б
    def __truediv__(self, other):
        return Vector([a / b if b != 0 else None for a, b in zip(self.coords, other.coords)])

    def __str__(self):
        return "(" + ",".join(map(str, self.coords)) + ")"
