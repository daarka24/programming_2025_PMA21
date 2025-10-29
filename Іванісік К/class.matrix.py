class Matrix:
    def __init__(self, data):
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Некоректна матриця — рядки різної довжини або порожня")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        try:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Матриці різних розмірів — додавання неможливе")
            res = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(res)
        except Exception as e:
            return Matrix([[f"Помилка при додаванні: {e}"]])

    def __sub__(self, other):
        try:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Матриці різних розмірів — віднімання неможливе")
            res = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(res)
        except Exception as e:
            return Matrix([[f"Помилка при відніманні: {e}"]])

    def __matmul__(self, other):
        try:
            if self.cols != other.rows:
                raise ValueError("Множення неможливе — кількість стовпців A ≠ кількості рядків B")
            result = [[0] * other.cols for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result[i][j] += self.data[i][k] * other.data[k][j]
            return Matrix(result)
        except Exception as e:
            return Matrix([[f"Помилка при множенні: {e}"]])

    def inverse(self):
        if self.rows != self.cols:
            raise ValueError("Матриця повинна бути квадратною для обернення")
        n = self.rows
        A = [row[:] for row in self.data]
        I = [[float(i == j) for j in range(n)] for i in range(n)]

        for i in range(n):
            if A[i][i] == 0:
                raise ZeroDivisionError("Ділення на нуль при оберненні матриці")
            div = A[i][i]
            for j in range(n):
                A[i][j] /= div
                I[i][j] /= div
            for k in range(n):
                if k != i:
                    factor = A[k][i]
                    for j in range(n):
                        A[k][j] -= factor * A[i][j]
                        I[k][j] -= factor * I[i][j]
        return Matrix(I)

    def divide(self, other):
        try:
            inv_B = other.inverse()
            return self @ inv_B
        except ZeroDivisionError:
            return Matrix([["Помилка: ділення на нуль — визначник B = 0, оберненої матриці не існує!"]])
        except ValueError as e:
            return Matrix([[f"Помилка при діленні: {e}"]])
        except Exception as e:
            return Matrix([[f"Непередбачена помилка при діленні: {e}"]])

    def to_file(self, f, text=""):
        f.write(text + "\n")
        for row in self.data:
            formatted_row = []
            for x in row:
                if isinstance(x, (int, float)):
                    x = round(x, 2)
                    if isinstance(x, float) and x.is_integer():
                        formatted_row.append(str(int(x)))
                    else:
                        formatted_row.append(str(x))
                else:
                    formatted_row.append(str(x))
            f.write(" ".join(formatted_row) + "\n")
        f.write("\n")

    def __bool__(self):
        return bool(self.data)

def read_matrix(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            data = [[int(x) for x in line.split()] for line in lines]
            return Matrix(data)
    except FileNotFoundError:
        return Matrix([[f"Файл {filename} не знайдено!"]])
    except ValueError as e:
        return Matrix([[f"Помилка у файлі {filename}: {e}"]])
    except Exception as e:
        return Matrix([[f"Непередбачена помилка при читанні {filename}: {e}"]])
try:
    A = read_matrix("matrixA.txt")
    B = read_matrix("matrixB.txt")

    with open("result.txt", "w", encoding="utf-8") as f:
        (A + B).to_file(f, "A + B:")
        (A - B).to_file(f, "A - B:")
        (A @ B).to_file(f, "A * B:")
        (A.divide(B)).to_file(f, "A / B:")

    print("Результати обчислень збережено у файл result.txt")

except Exception as e:
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"Критична помилка виконання програми: {e}\n")
    print(f"Критична помилка: {e}")
