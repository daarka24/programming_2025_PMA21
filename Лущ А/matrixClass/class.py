class Matrix:
    def __init__(self, data):
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Невірні дані матриці.")
        row_lengths = [len(row) for row in data]
        if len(set(row_lengths)) != 1:
            raise ValueError("Рядки матриці мають різну кількість елементів.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        return "\n".join(" ".join(str(int(x)) if x.is_integer() else str(x) for x in row) for row in self.data)

    def can_add_subtract(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def can_multiply(self, other):
        return self.cols == other.rows

    def is_square(self):
        return self.rows == self.cols

    def add(self, other):
        if not self.can_add_subtract(other):
            raise ValueError("Неможливо додати: матриці різні.")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def subtract(self, other):
        if not self.can_add_subtract(other):
            raise ValueError("Неможливо відняти: матриці різнs.")
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def multiply(self, other):
        if not self.can_multiply(other):
            raise ValueError("Неможливо помножити: кількість стовпців A не дорівнює кількості рядків B.")
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def inverse(self):
        if not self.is_square():
            raise ValueError("Матриця не квадратна — неможливо знайти обернену.")

        n = self.rows
        AM = [row[:] for row in self.data]
        I = [[float(i == j) for j in range(n)] for i in range(n)]

        for col in range(n):
            diag = AM[col][col]
            if diag == 0:
                raise ValueError("Матриця вироджена, немає оберненої.")
            for j in range(n):
                AM[col][j] /= diag
                I[col][j] /= diag
            for i in range(n):
                if i != col:
                    factor = AM[i][col]
                    for j in range(n):
                        AM[i][j] -= factor * AM[col][j]
                        I[i][j] -= factor * I[col][j]
        return Matrix(I)

    def divide(self, other):
        return self.multiply(other.inverse())



def parse_matrix(matrix_str):
    try:
        rows = matrix_str.strip().split("\n")
        data = [[float(x) for x in row.split()] for row in rows if row.strip()]
        return Matrix(data)
    except ValueError as e:
        print(f"Помилка: {e}\nМатриця:\n{matrix_str}\n")
        return None
    except Exception as e:
        print(f"Невідома помилка при читанні матриці:\n{matrix_str}\n{e}\n")
        return None



try:
    with open("matrices.txt", "r", encoding="utf-8") as f:
        content = f.read().strip()
except FileNotFoundError:
    print("Файл 'matrices.txt' не знайдено.")
    exit()

blocks = content.split("\n\n")
matrices = [parse_matrix(block) for block in blocks if block.strip()]
matrices = [m for m in matrices if m is not None]

with open("results.txt", "w", encoding="utf-8") as f:
    f.write("Результати обчислень матриць\n\n")

if len(matrices) < 2:
    print("У файлі має бути принаймні дві матриці.")
    exit()

A, B = matrices[0], matrices[1]

try:

    try:
        result_add = A.add(B)
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{A}\n+\n{B}\n=\n{result_add}\n\n")
    except ValueError as e:
        print(e)


    try:
        result_sub = A.subtract(B)
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{A}\n-\n{B}\n=\n{result_sub}\n\n")
    except ValueError as e:
        print(e)


    try:
        result_mul = A.multiply(B)
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{A}\n*\n{B}\n=\n{result_mul}\n\n")
    except ValueError as e:
        print(e)


    try:
        result_div = A.divide(B)
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{A}\n/\n{B}\n=\n{result_div}\n\n")
    except ValueError as e:
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{A}\n/\n{B}\n= неможливо ({e})\n\n")

except Exception as e:
    print("Помилка під час обчислень:", e)
