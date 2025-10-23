class Vector:
    def __init__(self, coords):
        self.coords = coords

    def __check_size(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError("Різний розмір векторів")

    def __add__(self, other):
        self.__check_size(other)
        result = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]
        return Vector(result)

    def __sub__(self, other):
        self.__check_size(other)
        result = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        return Vector(result)

    def __mul__(self, other):
        self.__check_size(other)
        result = [self.coords[i] * other.coords[i] for i in range(len(self.coords))]
        return Vector(result)

    def __truediv__(self, other):
        self.__check_size(other)
        if any(x == 0 for x in other.coords):
            raise ValueError("Ділення на нульовий елемент")
        result = [self.coords[i] / other.coords[i] for i in range(len(self.coords))]
        return Vector(result)

    def __str__(self):
        return "(" + ", ".join(str(x) for x in self.coords) + ")"
