class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return f"({', '.join(str(int(x)) if x.is_integer() else str(x) for x in self.coordinates)})"

    def add(self, other):
        return Vector([self.coordinates[i] + other.coordinates[i] for i in range(len(self.coordinates))])

    def subtract(self, other):
        return Vector([self.coordinates[i] - other.coordinates[i] for i in range(len(self.coordinates))])

    def multiply(self, other):
        return Vector([self.coordinates[i] * other.coordinates[i] for i in range(len(self.coordinates))])

    def divide(self, other):
        return Vector([self.coordinates[i] / other.coordinates[i] for i in range(len(self.coordinates))])


def parse_vector(vector_str: str):
    try:
        vector_str = vector_str.strip().replace('(', '').replace(')', '')
        coordinates = [float(x.strip()) for x in vector_str.split(',')]
        return Vector(coordinates)
    except ValueError:
        print(f"Помилка: '{vector_str}' — вектор некоректний.")
        return None


try:
    with open("vectors.txt", "r", encoding="utf-8") as f:
        vectors = []
        for line in f:
            if line.strip():
                v = parse_vector(line)
                if v is not None:
                    vectors.append(v)
except FileNotFoundError:
    print("Файл 'vectors.txt' не знайдено.")
    exit()

with open("results.txt", "w", encoding="utf-8") as f:
    f.write("Результати обчислень векторів:\n")

if len(vectors) >= 2:
    v1, v2 = vectors[0], vectors[1]

    try:
        if len(v1.coordinates) != len(v2.coordinates):
            raise ValueError(f"Вектори мають різну кількість елементів ({len(v1.coordinates)} і {len(v2.coordinates)}).")

        if any(x == 0 for x in v2.coordinates):
            print("Попередження: у другому векторі є нулі (ділення може бути нескінченністю).")

        results = [
            f"{v1} + {v2} = {v1.add(v2)}",
            f"{v1} - {v2} = {v1.subtract(v2)}",
            f"{v1} * {v2} = {v1.multiply(v2)}",
            f"{v1} / {v2} = {v1.divide(v2)}"
        ]

        with open("results.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(results) + "\n")

    except ZeroDivisionError:
        print("Помилка: ділення на нуль у другому векторі.")
    except ValueError as e:
        print("Помилка:", e)
else:
    print("У файлі має бути хоча б два вектори.")
