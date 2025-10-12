def read_matrix(filename):
    with open(filename, "r") as file:
        return [[float(num) for num in line.strip().split()] for line in file if line.strip()]
def write_result(filename, content):
    with open(filename, "w") as file:
        file.write(content)
def same_size(a, b):
    return len(a) == len(b) and len(a[0]) == len(b[0])
def can_multiply(a, b):
    return len(a[0]) == len(b)
def can_divide(a, b):
    return len(b) == len(b[0]) and len(a[0]) == len(b)
def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def invert(matrix):
    size = len(matrix)
    identity = [[float(i == j) for j in range(size)] for i in range(size)]
    copy = [row[:] for row in matrix]
    for i in range(size):
        if copy[i][i] == 0:
            for k in range(i + 1, size):
                if copy[k][i] != 0:
                    copy[i], copy[k] = copy[k], copy[i]
                    identity[i], identity[k] = identity[k], identity[i]
                    break
            else:
                return None
        pivot = copy[i][i]
        if pivot == 0:
            return None
        try:
            for j in range(size):
                copy[i][j] /= pivot
                identity[i][j] /= pivot
        except ZeroDivisionError:
            return None
        for k in range(size):
            if k != i:
                factor = copy[k][i]
                for j in range(size):
                    copy[k][j] -= factor * copy[i][j]
                    identity[k][j] -= factor * identity[i][j]
    return identity
def divide(a, b):
    inverse_b = invert(b)
    return multiply(a, inverse_b) if inverse_b else None
def format(matrix):
    return "\n".join(" ".join(str(round(val, 2)) for val in row) for row in matrix)

matrix_a = read_matrix("matrix1.txt")
matrix_b = read_matrix("matrix2.txt")

result = ""

if same_size(matrix_a, matrix_b):
    result += "A + B:\n" + format(add(matrix_a, matrix_b)) + "\n\n"
else:
    result += "A + B:\nCannot perform addition — matrices are different in size.\n\n"
if same_size(matrix_a, matrix_b):
    result += "A - B:\n" + format(subtract(matrix_a, matrix_b)) + "\n\n"
else:
    result += "A - B:\nCannot perform subtraction — matrices are different in size.\n\n"
if can_multiply(matrix_a, matrix_b):
    result += "A * B:\n" + format(multiply(matrix_a, matrix_b)) + "\n\n"
else:
    result += "A * B:\nCannot perform multiplication — incompatible matrix dimensions.\n\n"
if can_divide(matrix_a, matrix_b):
    try:
        division = divide(matrix_a, matrix_b)
        if division:
            result += "A / B:\n" + format(division) + "\n"
        else:
            result += "A / B:\nCannot divide — matrix B is not invertible.\n"
    except ZeroDivisionError:
        result += "A / B:\nCannot divide — division by zero.\n"
else:
    result += "A / B:\nCannot perform division — matrix B is not square or incompatible dimensions.\n"

write_result("result.txt", result)
