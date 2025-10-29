class Vector:
    def __init__(self, vector_components=None):
        if vector_components is None:
            self.vector_components = []
        else:
            self.vector_components = list(vector_components)

    def __add__(self, other_vector):
        return self.add_vector(other_vector)

    def __sub__(self, other_vector):
        return self.subtract_vector(other_vector)

    def __mul__(self, other_vector):
        return self.multiply_by_coords(other_vector)

    def __truediv__(self, other_vector):
        return self.divide_by_coords(other_vector)

    def check_size(self, other_vector):
        if len(self.vector_components) != len(other_vector.vector_components):
            raise ValueError("Vectors have different lengths. Operation is impossible.")

    def add_vector(self, other_vector):
        self.check_size(other_vector)

        new_vector_components = []
        for a, b in zip(self.vector_components, other_vector.vector_components):
            new_vector_components.append(a + b)

        return Vector(new_vector_components)

    def subtract_vector(self, other_vector):
        self.check_size(other_vector)

        new_vector_components = []
        for a, b in zip(self.vector_components, other_vector.vector_components):
            new_vector_components.append(a - b)

        return Vector(new_vector_components)

    def multiply_by_coords(self, other_vector):
        self.check_size(other_vector)

        new_vector_components = []
        for a, b in zip(self.vector_components, other_vector.vector_components):
            new_vector_components.append(a * b)

        return Vector(new_vector_components)

    def divide_by_coords(self, other_vector):
        self.check_size(other_vector)

        if any(b == 0 for b in other_vector.vector_components):
            raise ZeroDivisionError("Неможливо виконати ділення: один або кілька компонентів другого вектора дорівнюють нулю.")

        new_vector_components = []
        for a, b in zip(self.vector_components, other_vector.vector_components):
            new_vector_components.append(a / b)

        return Vector(new_vector_components)

    def __repr__(self):
        return str(self.vector_components)

    def get_string_representation(self):
        return str(self.vector_components)