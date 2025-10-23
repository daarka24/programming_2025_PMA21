def check_length_of_matrices(matrix_one, matrix_two):
    if len(matrix_one) != len(matrix_two):
        return False

    for i in range(len(matrix_one)):
        if len(matrix_one[i]) != len(matrix_two[i]):
            return False
    return True


def mat_plus_mat(matrix_one, matrix_two):
    if not check_length_of_matrices(matrix_one, matrix_two):
        print("the length of the matrices must be equal")
        return
    result = [[0 for _ in range(len(matrix_two[0]))] for _ in range(len(matrix_one))]
    for i in range(len(matrix_one)):
        for j in range(len(matrix_two[0])):
            result[i][j] = matrix_one[i][j] + matrix_two[i][j]
    return result

def mat_minus_mat(matrix_one, matrix_two):
    if not check_length_of_matrices(matrix_one, matrix_two):
        print("the length of the matrices must be equal")
        return
    result = [[0 for _ in range(len(matrix_two[0]))] for _ in range(len(matrix_one))]
    for i in range(len(matrix_one)):
        for j in range(len(matrix_two[0])):
            result[i][j] = matrix_one[i][j] - matrix_two[i][j]
    return result

def mat_multi_mat(matrix_one, matrix_two):
    if not check_length_of_matrices(matrix_one, matrix_two):
        print("the length of the matrices must be equal")
        return
    result = [[0 for _ in range(len(matrix_two[0]))] for _ in range(len(matrix_one))]
    for i in range(len(matrix_one)):
        for j in range(len(matrix_two[0])):
            for k in range(len(matrix_two)):
                result[i][j] += matrix_one[i][k] * matrix_two[k][j]
    return result

def inverse_matrix(matrix):
    n = len(matrix)
    augmented = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        diag_element = augmented[i][i]
        if diag_element == 0:
            print("Error: Matrix is singular and cannot be inverted.")
            return None

        for j in range(2 * n):
            augmented[i][j] /= diag_element

        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]

    return [row[n:] for row in augmented]

def divide_matrices(matrix_one, matrix_two):
    if not check_length_of_matrices(matrix_one, matrix_two):
        print("the length of the matrices must be equal")
        return
    inverse_b = inverse_matrix(matrix_one)
    if inverse_b is None:
        return None
    result = mat_multi_mat(matrix_two, inverse_b)
    return result

matrix_one = []
matrix_two = []

try:
    with open("file.txt") as f:
        for line in f:
            matrix_one.append([float(x) for x in line.split()])
except FileNotFoundError:
    print("file.txt is not found")
try:
    with open("file_2.txt") as f:
        for line in f:
            matrix_two.append([float(x) for x in line.split()])
except FileNotFoundError:
    print("file_2.txt is not found")

with open("result.txt", "w") as file:
    sum_result = mat_plus_mat(matrix_one, matrix_two)
    file.write("\nAddition:\n")
    if sum_result:
        for row in sum_result:
            file.write(str(row) + "\n")
    else:
        file.write("Cannot add matrices\n")

    subtraction_result = mat_minus_mat(matrix_one, matrix_two)
    file.write("\nSubtraction:\n")
    if subtraction_result:
        for row in subtraction_result:
            file.write(str(row) + "\n")
    else:
        file.write("Cannot subtract matrices\n")

    multiplication_result = mat_multi_mat(matrix_one, matrix_two)
    file.write("\nMultiplication:\n")
    if multiplication_result:
        for row in multiplication_result:
            file.write(str(row) + "\n")
    else:
        file.write("Cannot multiply matrices\n")

    division_result = divide_matrices(matrix_one, matrix_two)
    file.write("\nDivision:\n")
    if division_result:
        for row in division_result:
            file.write(str(row) + "\n")
    else:
        file.write("Cannot divide matrices\n")