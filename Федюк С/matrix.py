def read_matrix(filename):
    matrix = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                if line.strip():
                    try:
                        row = [float(x) for x in line.strip().split()]
                    except ValueError:
                        return f"Помилка: некоректні дані у рядку {line_num} файлу '{filename}'."
                    matrix.append(row)
    except FileNotFoundError:
        return f"Помилка: файл '{filename}' не знайдено."
    except Exception as e:
        return f"Помилка при читанні файлу '{filename}': {e}"

    if not matrix:
        return f"Помилка: файл '{filename}' порожній."

    row_length = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != row_length:
            return f"Помилка: різна кількість елементів у рядках (рядок {i+1})."
        if all(x == 0 for x in row):
            return f"Помилка: рядок {i+1} містить лише нулі — матриця некоректна."

    return matrix

def add_matrices(mat1, mat2):
    if isinstance(mat1, str):
        return f"Сума: {mat1}"
    if isinstance(mat2, str):
        return f"Сума: {mat2}"
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Сума: матриці різного розміру — додавання неможливе."
    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

def sub_matrices(mat1, mat2):
    if isinstance(mat1, str):
        return f"Віднімання: {mat1}"
    if isinstance(mat2, str):
        return f"Віднімання: {mat2}"
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Віднімання: матриці різного розміру — віднімання неможливе."
    result = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

def multiply_matrices(mat1, mat2):
    if isinstance(mat1, str):
        return f"Множення: {mat1}"
    if isinstance(mat2, str):
        return f"Множення: {mat2}"
    if len(mat1[0]) != len(mat2):
        return "Множення: кількість стовпців першої матриці не дорівнює кількості рядків другої."
    result = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2[0])):
            total = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
            new_row.append(total)
        result.append(new_row)
    return result

def invert_matrix(mat):
    if isinstance(mat, str):
        return f"Обернення: {mat}"
    n = len(mat)
    if any(len(row) != n for row in mat):
        return "Обернення: матриця не квадратна — обернення неможливе."
    inv_mat = [[float(i == j) for j in range(n)] for i in range(n)]
    temp_mat = [row[:] for row in mat]
    for i in range(n):
        if temp_mat[i][i] == 0:
            for j in range(i+1, n):
                if temp_mat[j][i] != 0:
                    temp_mat[i], temp_mat[j] = temp_mat[j], temp_mat[i]
                    inv_mat[i], inv_mat[j] = inv_mat[j], inv_mat[i]
                    break
            else:
                return "Обернення: матриця необернена (детермінант = 0)."
        factor = temp_mat[i][i]
        for j in range(n):
            temp_mat[i][j] /= factor
            inv_mat[i][j] /= factor
        for k in range(n):
            if k != i:
                f = temp_mat[k][i]
                for j in range(n):
                    temp_mat[k][j] -= f * temp_mat[i][j]
                    inv_mat[k][j] -= f * inv_mat[i][j]
    return inv_mat

def divide_matrices(mat1, mat2):
    if isinstance(mat1, str):
        return f"Ділення: {mat1}"
    if isinstance(mat2, str):
        return f"Ділення: {mat2}"
    inv_mat = invert_matrix(mat2)
    if isinstance(inv_mat, str):
        return f"Ділення: {inv_mat}"
    return multiply_matrices(mat1, inv_mat)

matrix_a = read_matrix("matrix1.txt")
matrix_b = read_matrix("matrix2.txt")

sum_result = add_matrices(matrix_a, matrix_b)
diff_result = sub_matrices(matrix_a, matrix_b)
prod_result = multiply_matrices(matrix_a, matrix_b)
div_result = divide_matrices(matrix_a, matrix_b)

with open("result.txt", "w", encoding="utf-8") as file:
    def write_matrix(res, title):
        if isinstance(res, str):
            file.write(res + "\n")
        else:
            file.write(title + "\n")
            for r in res:
                file.write(" ".join(str(round(x, 2)) for x in r) + "\n")

    write_matrix(sum_result, "Сума:")
    write_matrix(diff_result, "Різниця:")
    write_matrix(prod_result, "Множення:")
    write_matrix(div_result, "Ділення:")
