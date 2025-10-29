class Vector:
    def __init__(self, values):
        self.values = values

    def add(self, other):
        if len(self.values) != len(other.values):
            return "Error: Vectors have different lengths."
        result = [x + y for x, y in zip(self.values, other.values)]
        return Vector(result)

    def subtract(self, other):
        if len(self.values) != len(other.values):
            return "Error: Vectors have different lengths."
        result = [x - y for x, y in zip(self.values, other.values)]
        return Vector(result)

    def multiply(self, other):
        if len(self.values) != len(other.values):
            return "Error: Vectors have different lengths."
        result = [x * y for x, y in zip(self.values, other.values)]
        return Vector(result)

    def divide_by_scalar(self, scalar):
        if scalar == 0:
            return "Error: Cannot divide by zero scalar."
        result = [x / scalar for x in self.values]
        return Vector(result)

    def divide(self, other):
        if len(self.values) != len(other.values):
            return "Error: Vectors have different lengths."
        result = []
        for x, y in zip(self.values, other.values):
            if y == 0:
                return "Error: Division by zero in vector."
            result.append(x / y)
        return Vector(result)

    def __str__(self):
        return str(self.values)

def read_vector(file):
    line = file.readline().strip()
    if not line:
        return []
    parts = line.replace(",", " ").split()
    return list(map(int, parts))

with open("input.txt", "r") as file:
    a = read_vector(file)
    b = read_vector(file)

with open("scalar.txt", "r") as f:
    c = int(f.readline().strip())

v1 = Vector(a)
v2 = Vector(b)

plus = v1.add(v2)
minus = v1.subtract(v2)
multiply = v1.multiply(v2)
divide_scalar = v1.divide_by_scalar(c)
divide_vector = v1.divide(v2)

with open("output.txt", "w") as file:
    file.write("Plus: " + str(plus) + "\n")
    file.write("Minus: " + str(minus) + "\n")
    file.write("Multiply: " + str(multiply) + "\n")
    file.write("Divide by scalar: " + str(divide_scalar) + "\n")
    file.write("Divide by vector: " + str(divide_vector) + "\n")
