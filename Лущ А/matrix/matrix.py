def parse_matrix(matrix_str):
    try:
        rows = matrix_str.strip().split("\n")
        matrix = [[float(x) for x in row.split()] for row in rows]

        row_lengths = [len(row) for row in matrix]
        if len(set(row_lengths)) != 1:
            raise ValueError("Рядки матриці мають різну кількість елементів.")

        return matrix
    except ValueError as e:
        print(f"Помилка: {e}\nМатриця:\n{matrix_str}\n")
        return None
    except Exception as e:
        print(f"Невідома помилка при обробці матриці:\n{matrix_str}\n{e}\n")
        return None


def matrix_to_string(M):
    return "\n".join(" ".join(str(int(x)) if x.is_integer() else str(x) for x in row) for row in M)


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def multiply_matrices(A, B):
    rows, cols = len(A), len(B[0])
    res = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]
    return res


def inverse_matrix(M):
    n = len(M)
    AM = [row[:] for row in M]
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
    return I


def divide_matrices(A, B):
    B_inv = inverse_matrix(B)
    return multiply_matrices(A, B_inv)



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

    if len(A) == len(B) and len(A[0]) == len(B[0]):
        result_add = add_matrices(A, B)
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{matrix_to_string(A)}\n+\n{matrix_to_string(B)}\n=\n{matrix_to_string(result_add)}\n\n")
    else:
        print("Неможливо додати: матриці різних різні.")


    if len(A) == len(B) and len(A[0]) == len(B[0]):
        result_sub = subtract_matrices(A, B)
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{matrix_to_string(A)}\n-\n{matrix_to_string(B)}\n=\n{matrix_to_string(result_sub)}\n\n")
    else:
        print("Неможливо відняти: матриці різні.")


    if len(A[0]) == len(B):
        result_mul = multiply_matrices(A, B)
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(f"{matrix_to_string(A)}\n*\n{matrix_to_string(B)}\n=\n{matrix_to_string(result_mul)}\n\n")
    else:
        print("Неможливо помножити: кількість стовпців A не дорівнює кількості рядків B.")


    if len(B) == len(B[0]):
        try:
            result_div = divide_matrices(A, B)
            with open("results.txt", "a", encoding="utf-8") as f:
                f.write(f"{matrix_to_string(A)}\n/\n{matrix_to_string(B)}\n=\n{matrix_to_string(result_div)}\n\n")
        except ValueError:
            with open("results.txt", "a", encoding="utf-8") as f:
                f.write(f"{matrix_to_string(A)}\n/\n{matrix_to_string(B)}\n= неможливо (немає оберненої)\n\n")
    else:
        print("Матриця B не квадратна неможливо знайти обернену.")
except Exception as e:
    print("Помилка під час обчислень:", e)
