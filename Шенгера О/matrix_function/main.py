def read_file(file):
    with open(file, "r") as r:
        line = r.readlines()

    row_column = [int(x) for x in line[0].split()]
    matrix_nums = [float(x) for x in line[1].split()]

    if row_column[0] <= 0 or row_column[1] <= 0:
        raise ValueError("row and column must be greater that 0")
    if row_column[0] * row_column[1] != len(matrix_nums):
        raise ValueError("rows * columns must equal matrix numbers in sum.")

    if matrix_nums:
        n = 0
        matrix = []

        for i in range(row_column[0]):
            row = []
            for j in range(row_column[1]):
                row.append(matrix_nums[n])
                n+=1
            matrix.append(row)

        return matrix
    raise ValueError("no numbers in files are given.")

def is_equal_matrices(first_matrix, second_matrix) -> bool:
    # first matrix row, column
    f_row, f_column = len(first_matrix), len(first_matrix[0])
    # second matrix row, column
    s_row, s_column = len(second_matrix), len(second_matrix[0])

    if f_row == s_row and f_column == s_column:
        return True

    raise ValueError("matrices not equal.")


def add_matrix(first_matrix, second_matrix):
    row, column = len(first_matrix), len(first_matrix[0])
    new_matrix = [[0 for _ in range(column)] for _ in range(row)]
    for i in range(row):
        for j in range(column):
            new_matrix[i][j] = first_matrix[i][j] + second_matrix[i][j]
    return new_matrix

def subtract_matrix(first_matrix, second_matrix):
    row, column = len(first_matrix), len(first_matrix[0])
    new_matrix = [[0 for _ in range(column)] for _ in range(row)]
    for i in range(row):
        for j in range(column):
            new_matrix[i][j] = first_matrix[i][j] - second_matrix[i][j]
    return new_matrix

def multiply_matrix(first_matrix, second_matrix):
    row, column = len(first_matrix), len(first_matrix[0])
    new_matrix = [[0 for _ in range(column)] for _ in range(row)]
    for i in range(row):
        for j in range(column):
            for p in range(row):
                new_matrix[i][j] += first_matrix[i][p] * second_matrix[p][j]

    return new_matrix


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        submatrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1)**c) * matrix[0][c] * determinant(submatrix)
    return det


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def cofactor_matrix(matrix):
    size = len(matrix)
    cofactors = []
    for r in range(size):
        cofactor_row = []
        for c in range(size):
            submatrix = [row[:c] + row[c+1:] for i, row in enumerate(matrix) if i != r]
            cofactor_row.append(((-1) ** (r + c)) * determinant(submatrix))
        cofactors.append(cofactor_row)
    return cofactors


def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("second_matrix is singular, cannot invert.")

    cofactors = cofactor_matrix(matrix)
    adjugate = transpose(cofactors)
    size = len(matrix)

    inverse = [[adjugate[r][c] / det for c in range(size)] for r in range(size)]
    return inverse


def divide_matrix(first_matrix, second_matrix):
    # A * B^-1
    f_row, f_col = len(first_matrix), len(first_matrix[0])
    s_row, s_col = len(second_matrix), len(second_matrix[0])

    if s_row != s_col:
        raise ValueError("second_matrix must be square for classical division.")

    inv_B = inverse_matrix(second_matrix)

    if f_col != s_row:
        raise ValueError("matrices dimensions not aligned for A * B^-1")

    new_matrix = [[0 for _ in range(s_col)] for _ in range(f_row)]
    for i in range(f_row):
        for j in range(s_col):
            for k in range(f_col):
                new_matrix[i][j] += first_matrix[i][k] * inv_B[k][j]
    return new_matrix

def write_file(file, message, matrix):
    with open(file, "a") as a:
        a.write(message + str(matrix) + "\n")


if __name__=="__main__":
    try:
        first_matrix = read_file("first_matrix.txt")
        second_matrix = read_file("second_matrix.txt")
    except ValueError as e:
        print(f"error: {e}")
        exit(1)
    except IndexError:
        print("file must contain row and column fields.")
        exit(1)
    try:
        result = is_equal_matrices(first_matrix, second_matrix)
    except ValueError as e:
        print(f"error: {e}")
        exit(1)

    write_file("matrix_result", "add: ", add_matrix(first_matrix, second_matrix))
    write_file("matrix_result", "subtract: ", subtract_matrix(first_matrix, second_matrix))
    write_file("matrix_result", "multiply: ", multiply_matrix(first_matrix, second_matrix))
    write_file("matrix_result", "divide: ", divide_matrix(first_matrix, second_matrix))



