class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return "(" + ", ".join(str(c) for c in self.coordinates) + ")"

    def __add__(self, other):
        try:
            return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])
        except:
            return None

    def __sub__(self, other):
        try:
            return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])
        except:
            return None

    def __mul__(self, other):
        try:
            if isinstance(other, Vector):
                return Vector([a * b for a, b in zip(self.coordinates, other.coordinates)])
            elif isinstance(other, (int, float)):
                return Vector([a * other for a in self.coordinates])
            else:
                return None
        except:
            return None

    def __truediv__(self, other):
        try:
            if isinstance(other, Vector):
                return Vector([a / b if b != 0 else float('inf') for a, b in zip(self.coordinates, other.coordinates)])
            elif isinstance(other, (int, float)):
                return Vector([a / other if other != 0 else float('inf') for a in self.coordinates])
            else:
                return None
        except:
            return None


class VectorApp:
    def __init__(self, vector_file, scalar_file, result_file):
        self.vector_file = vector_file
        self.scalar_file = scalar_file
        self.result_file = result_file

    def read_vectors(self):
        vectors = []
        try:
            with open(self.vector_file, 'r') as file:
                for line in file:
                    line = line.strip().replace("(", "").replace(")", "")
                    if line:
                        parts = [float(x.strip()) for x in line.split(',')]
                        vectors.append(Vector(parts))
        except:
            return []
        return vectors

    def read_scalar(self):
        try:
            with open(self.scalar_file, 'r') as file:
                line = file.readline().strip()
                if line:
                    return float(line)
        except:
            return None
        return None

    def write_result(self, operation, v1, v2, result):
        try:
            with open(self.result_file, 'a') as file:
                file.write(f"{v1} {operation} {v2} = {result}\n")
        except:
            pass

    def write_error(self, message):
        try:
            with open(self.result_file, 'a') as file:
                file.write(message + "\n")
        except:
            pass

    def calculate(self):
        try:
            with open(self.result_file, 'w') as file:
                file.write("Операції з векторами\n\n")
        except:
            return

        vectors = self.read_vectors()
        scalar = self.read_scalar()

        if not vectors or scalar is None:
            self.write_error("Не вдалося прочитати вектори або скаляр")
            return

        if len(vectors) % 2 != 0:
            self.write_error("Кількість векторів має бути парною")
            return

        for i in range(0, len(vectors), 2):
            v1 = vectors[i]
            v2 = vectors[i + 1]

            if len(v1.coordinates) != len(v2.coordinates):
                self.write_error(f"Вектори {v1} і {v2} мають різну розмірність")
                continue

            operations = [
                ('+', v1 + v2),
                ('-', v1 - v2),
                ('*', v1 * v2),
                ('*', v1 * scalar),
                ('/', v1 / scalar)
            ]

            for op, result in operations:
                if result:
                    self.write_result(op, v1, v2 if op in ['+', '-', '*'] else scalar, result)
                else:
                    self.write_error(f"Не вдалося виконати операцію {op} між {v1} і {v2 if op in ['+', '-', '*'] else scalar}")

app = VectorApp("vector.txt", "scalar.txt", "result.txt")
app.calculate()
