class Vector:

    def __init__(self, vector):
        self.vector = vector

    def check_length(self, other):
        if len(self.vector) != len(other.vector):
            print("The length of the two vectors must be equal")
            return False
        return True
    def sum_of_vectors(self, other):
        if not self.check_length(other):
            print("The length of the two vectors must be equal")
            return
        return [self.vector[i] + other.vector[i] for i in range(len(self.vector))]

    def sub_of_vectors(self, other):
        if not self.check_length(other):
            print("The length of the two vectors must be equal")
            return
        return [self.vector[i] - other.vector[i] for i in range(len(self.vector))]

    def multiply_vectors(self, other):
        if not self.check_length(other):
            print("The length of the two vectors must be equal")
            return
        return [self.vector[i] * other.vector[i] for i in range(len(self.vector))]


    def find_scalar(self, other):
        if not self.check_length(other):
            print("The length of the two vectors must be equal")
            return
        return sum([self.vector[i] * other.vector[i] for i in range(len(self.vector))])

    def mul_by_n(self, other, n):

        return f'{[self.vector[i]*n for i in range(len(self.vector))]}\n{[other.vector[i]*n for i in range(len(other.vector))]}'

    def div_by_n(self, other, n):

        return f'{[self.vector[i]/n for i in range(len(self.vector))]}\n{[other.vector[i]*n for i in range(len(other.vector))]}'


