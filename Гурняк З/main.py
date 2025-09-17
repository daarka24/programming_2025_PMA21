def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def write_log(operation, matrix_a, matrix_b, result, log_file='matrix_log.txt'):
    with open(log_file, 'a') as file:
        file.write(f"Operation: {operation}\n")
        file.write("Matrix A:\n")
        for row in matrix_a:
            file.write(' '.join(map(str, row)) + '\n')
        file.write("Matrix B:\n")
        for row in matrix_b:
            file.write(' '.join(map(str, row)) + '\n')
        file.write("Result:\n")
        for row in result:
            file.write(' '.join(map(str, row)) + '\n')
        file.write('\n')

def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    write_log("Addition", matrix_a, matrix_b, result)
    return result

def subtract_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    result = [[matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    write_log("Subtraction", matrix_a, matrix_b, result)
    return result

def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
    result = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b))) for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]
    write_log("Multiplication", matrix_a, matrix_b, result)
    return result

def inverse_matrix(matrix):
    n = len(matrix)
    augmented = [matrix[i] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        diag_element = augmented[i][i]
        if diag_element == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        for j in range(2 * n):
            augmented[i][j] /= diag_element
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
    return [row[n:] for row in augmented]

def divide_matrices(matrix_a, matrix_b):
    inverse_b = inverse_matrix(matrix_b)
    result = multiply_matrices(matrix_a, inverse_b)
    write_log("Division", matrix_a, matrix_b, result)
    return result

# Example usage
if __name__ == "__main__":
    matrix1 = read_matrix('matrix1.txt')
    matrix2 = read_matrix('matrix2.txt')

    result_add = add_matrices(matrix1, matrix2)
    result_sub = subtract_matrices(matrix1, matrix2)
    result_mul = multiply_matrices(matrix1, matrix2)
    result_div = divide_matrices(matrix1, matrix2)

    print("Results logged in 'matrix_log.txt'")
