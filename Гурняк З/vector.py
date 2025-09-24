class Vector:
    def __init__(self, values):
        self.values = list(values)

    def _check_same_length(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be the same length.")

    def add(self, other):
        self._check_same_length(other)
        res = [a + b for a, b in zip(self.values, other.values)]
        steps = [f"{a} + {b} = {a + b}" for a, b in zip(self.values, other.values)]
        return Vector(res), steps

    def subtract(self, other):
        self._check_same_length(other)
        res = [a - b for a, b in zip(self.values, other.values)]
        steps = [f"{a} - {b} = {a - b}" for a, b in zip(self.values, other.values)]
        return Vector(res), steps

    def multiply(self, other):
        self._check_same_length(other)
        res = [a * b for a, b in zip(self.values, other.values)]
        steps = [f"{a} * {b} = {a * b}" for a, b in zip(self.values, other.values)]
        return Vector(res), steps

    def divide(self, other):
        self._check_same_length(other)
        res, steps = [], []
        for a, b in zip(self.values, other.values):
            if b == 0:
                res.append("Division by zero")
                steps.append(f"{a} / {b} = Division by zero")
            else:
                val = a / b
                res.append(val)
                steps.append(f"{a} / {b} = {val}")
        return res, steps

    def dot(self, other):
        self._check_same_length(other)
        products = [a * b for a, b in zip(self.values, other.values)]
        total = sum(products)
        steps = [f"{a} * {b} = {a * b}" for a, b in zip(self.values, other.values)]
        steps.append(f"{' + '.join(str(p) for p in products)} = {total}")
        return total, steps