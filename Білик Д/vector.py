class Vector:
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    @staticmethod
    def read(filename):
        vectors = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                nums = list(map(float, line.strip().split()))
                vectors.append(Vector(nums))
        return vectors

    def write(self, filename, text):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, other):
        return Vector([a * b for a, b in zip(self.data, other.data)])

    def __truediv__(self, other):
        return Vector([a / b if b != 0 else float("inf") for a, b in zip(self.data, other.data)])

    def __str__(self):
        return "(" + ",".join(str(int(x)) if float(x).is_integer() else str(x) for x in self.data) + ")"

vectors = Vector.read("number.txt")

if len(vectors) < 2:
    print("У файлі повинно бути як мінімум 2 вектори!")
else:
    v1, v2 = vectors[0], vectors[1]

    result_text = f"{v1} + {v2} = {v1 + v2}\n"
    result_text += f"{v1} - {v2} = {v1 - v2}\n"
    result_text += f"{v1} * {v2} = {v1 * v2}\n"
    result_text += f"{v1} / {v2} = {v1 / v2}\n"

    v1.write("result.txt", result_text)
