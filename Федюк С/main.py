class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __str__(self):
        result = ""
        for i in range(self.rows):
            for j in range(self.cols):
                result += "{0:.2f}".format(self.data[i][j])
                if j != self.cols - 1:
                    result += " "
            result += "\n"
        return result

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Помилка: матриці різного розміру — додавання неможливе.")
            return None
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Помилка: матриці різного розміру — віднімання неможливе.")
            return None
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def multiply(self, other):
        if self.cols != other.rows:
            print("Помилка: кількість стовпців першої матриці не дорівнює кількості рядків другої.")
            return None
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

    def inverse(self):
        if self.rows != self.cols:
            print("Помилка: матриця не квадратна — обернення неможливе.")
            return None
        n = self.rows

        a = [row[:] for row in self.data]

        inv = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

        for i in range(n):
            if a[i][i] == 0:
                found = False
                for j in range(i + 1, n):
                    if a[j][i] != 0:
                        a[i], a[j] = a[j], a[i]
                        inv[i], inv[j] = inv[j], inv[i]
                        found = True
                        break
                if not found:
                    print("Помилка: матриця необернена (детермінант = 0).")
                    return None

            factor = a[i][i]
            if factor == 0:
                print("Помилка: обернення неможливе (нульовий діагональний елемент).")
                return None

            for j in range(n):
                a[i][j] /= factor
                inv[i][j] /= factor

            for k in range(n):
                if k != i:
                    f = a[k][i]
                    for j in range(n):
                        a[k][j] -= f * a[i][j]
                        inv[k][j] -= f * inv[i][j]

        return Matrix(inv)

    def divide(self, other):
        if other.rows != other.cols:
            print("Помилка: матриця B не квадратна — обернення неможливе.")
            return None

        inv_b = other.inverse()
        if inv_b is None:
            print("Помилка: матриця B необернена (детермінант = 0).")
            return None

        result = self.multiply(inv_b)
        if result is None:
            print("Помилка: множення A × B⁻¹ неможливе (розміри не збігаються).")
            return None

        return result

def read_matrix(filename):
    matrix = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                if line.strip():
                    try:
                        row = [float(x) for x in line.strip().split()]
                    except ValueError:
                        print(f"Помилка: некоректні дані у рядку {line_num} файлу '{filename}'.")
                        return None
                    matrix.append(row)
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при читанні файлу '{filename}': {e}")
        return None

    if not matrix:
        print(f"Помилка: файл '{filename}' порожній.")
        return None

    row_length = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != row_length:
            print(f"Помилка: різна кількість елементів у рядках (рядок {i + 1}).")
            return None
        if all(x == 0 for x in row):
            print(f"Помилка: рядок {i + 1} містить лише нулі — матриця некоректна.")
            return None

    return Matrix(matrix)

matrix_a = read_matrix("matrix1.txt")
matrix_b = read_matrix("matrix2.txt")

if matrix_a and matrix_b:
    sum_result = matrix_a.add(matrix_b)
    diff_result = matrix_a.subtract(matrix_b)
    prod_result = matrix_a.multiply(matrix_b)
    div_result = matrix_a.divide(matrix_b)

    with open("result.txt", "w", encoding="utf-8") as file:
        if sum_result:
            file.write("Sum:\n" + str(sum_result))
        if diff_result:
            file.write("\nDifference:\n" + str(diff_result))
        if prod_result:
            file.write("\nProduct:\n" + str(prod_result))
        if div_result:
            file.write("\nDivision:\n" + str(div_result))
        elif div_result is None:
            file.write("\nDivision:\nНеможливо (матриця B не квадратна або необернена)\n")

    print("Результати збережено у result.txt")
else:
    print("Обчислення неможливе через помилки у зчитуванні матриць.")
