class Vector:

    def __init__(self, vector):
        self.vector = vector

    def __repr__(self):
        return repr(self.vector)

    def __str__(self):
        return str(self.vector)

    def __iter__(self):
        return iter(self.vector)


    def sum(self, other):
        if len(self.vector) != len(other.vector):
            print("The length of the two vectors must be equal")
            return None

        return tuple([self.vector[i] + other.vector[i] for i in range(len(self.vector))])


    def sub(self, other):
        if len(self.vector) != len(other.vector):
            print("The length of the two vectors must be equal")
            return None

        return tuple([self.vector[i] - other.vector[i] for i in range(len(self.vector))])


    def mul_scalar(self, other):
        if len(self.vector) != len(other.vector):
            print("The length of the two vectors must be equal")
            return None

        return sum([self.vector[i] * other.vector[i] for i in range(len(self.vector))])


    def mul_by_scalar(self, n):
        return tuple([el * n for el in self.vector])


    def div_by_scalar(self, n):
        return tuple([el / n for el in self.vector])


    def mul_vectors(self, other):
        x, y = self.vector, other.vector

        if len(x) != len(y) != 3:
            print("The length of the two vectors must be equal 3")
            return None

        return x[1] * y[2] - x[2] * y[1], -(x[0] * y[2] - x[2] * y[0]), x[0] * y[1] - x[1] * y[0]