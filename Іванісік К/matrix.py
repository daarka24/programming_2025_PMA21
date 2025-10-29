def read_matrix(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            matrix = [list(map(int, line.split())) for line in f]

        if matrix and not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError(f"Некоректна матриця у файлі {filename}: рядки різної довжини!")

        return matrix

    except FileNotFoundError:
        return [[f"Файл {filename} не знайдено!"]]
    except ValueError as e:
        return [[str(e)]]
    except Exception as e:
        return [[f"Помилка при читанні {filename}: {e}"]]

def write_matrix(f, matrix, title):
    f.write(title + "\n")
    for row in matrix:
        f.write(" ".join(map(str, row)) + "\n")
    f.write("\n")

def same_size(A, B):
    if not A or not B:
        return False
    return len(A) == len(B) and all(len(rowA) == len(rowB) for rowA, rowB in zip(A, B))

def add_matrices(A, B):
    try:
        if not same_size(A, B):
            return [["Матриці різних розмірів — додавання неможливе"]]
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    except Exception as e:
        return [[f"Помилка при додаванні: {e}"]]

def sub_matrices(A, B):
    try:
        if not same_size(A, B):
            return [["Матриці різних розмірів — віднімання неможливе"]]
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    except Exception as e:
        return [[f"Помилка при відніманні: {e}"]]

def mul_matrices(A, B):
    try:
        if not A or not B:
            return [["Множення неможливе — порожня матриця"]]
        if len(A[0]) != len(B):
            return [["Множення неможливе — кількість стовпців A ≠ кількості рядків B"]]
        result = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    except Exception as e:
        return [[f"Помилка при множенні: {e}"]]

def inverse_matrix_2x2(M):
    if len(M) != 2 or len(M[0]) != 2 or len(M[1]) != 2:
        raise ValueError("Обернена матриця підтримується лише для 2x2!")
    det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    if det == 0:
        raise ZeroDivisionError("Ділення на нуль — визначник = 0, оберненої матриці не існує!")
    inv_det = 1 / det
    return [
        [ M[1][1] * inv_det, -M[0][1] * inv_det],
        [-M[1][0] * inv_det,  M[0][0] * inv_det]
    ]

def div_matrices(A, B):
    try:
        B_inv = inverse_matrix_2x2(B)
        if len(A[0]) != len(B_inv):
            return [["Ділення неможливе — кількість стовпців A ≠ кількості рядків B⁻¹"]]
        return mul_matrices(A, B_inv)
    except (ZeroDivisionError, ValueError) as e:
        return [[str(e)]]
    except Exception as e:
        return [[f"Помилка при діленні: {e}"]]

A = read_matrix("matrixA.txt")
B = read_matrix("matrixB.txt")

with open("result.txt", "w", encoding="utf-8") as f:
    write_matrix(f, add_matrices(A, B), "A + B:")
    write_matrix(f, sub_matrices(A, B), "A - B:")
    write_matrix(f, mul_matrices(A, B), "A * B:")
    write_matrix(f, div_matrices(A, B), "A / B:")
