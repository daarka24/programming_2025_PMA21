from vector import Vector

class VectorCalculator:
    def __init__(self, v1: "Vector", v2: "Vector"):
        self.v1 = v1
        self.v2 = v2

    @staticmethod
    def read_vectors(input_file):
        with open(input_file, 'r') as f:
            vectors = [list(map(int, line.strip().split())) for line in f]
        if len(vectors) < 2:
            raise ValueError("Input must contain at least two lines with numbers.")
        return Vector(vectors[0]), Vector(vectors[1])

    def compute_all(self):
        lines = []

        add_vec, add_steps = self.v1.add(self.v2)
        lines.append(f"Addition Steps: {add_steps}\n")
        lines.append(f"Addition: {add_vec.values}\n")

        sub_vec, sub_steps = self.v1.subtract(self.v2)
        lines.append(f"Subtraction Steps: {sub_steps}\n")
        lines.append(f"Subtraction: {sub_vec.values}\n")

        mul_vec, mul_steps = self.v1.multiply(self.v2)
        lines.append(f"Multiplication Steps: {mul_steps}\n")
        lines.append(f"Multiplication: {mul_vec.values}\n")

        div_res, div_steps = self.v1.divide(self.v2)
        lines.append(f"Division Steps: {div_steps}\n")
        lines.append(f"Division: {div_res}\n")

        dot_val, dot_steps = self.v1.dot(self.v2)
        lines.append(f"Dot Product Steps: {dot_steps}\n")
        lines.append(f"Dot Product: {dot_val}\n")

        return lines

    @staticmethod
    def write_results(output_file, lines):
        with open(output_file, 'w') as f:
            f.writelines(lines)