def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    operation = lines[0].strip()

    first_matrix = []
    second_matrix = []
    current_matrix = 1

    for line in lines[1:]:
        line = line.strip()
        if not line:
            current_matrix = 2
        elif line:
            numbers = [float(x) for x in line.split()]
            if current_matrix == 1:
                first_matrix.append(numbers)
            else:
                second_matrix.append(numbers)

    return operation, first_matrix, second_matrix


def save_matrix(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(str(x) for x in row) + '\n')


def print_matrix(matrix):
    for row in matrix:
        print(row)


def add(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def subtract(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result


def multiply(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_val = 0
            for k in range(len(B)):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val)
        result.append(row)
    return result


def is_zero_matrix(matrix):
    for row in matrix:
        for val in row:
            if val != 0:
                return False
    return True


def inverse(matrix):
    if is_zero_matrix(matrix):
        raise ValueError("Помилка: Ділення на нульовий елемент")

    n = len(matrix)

    aug = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        pivot = aug[i][i]
        if pivot == 0:
            raise ValueError("Матриця необернена")

        aug[i] = [x / pivot for x in aug[i]]

        for k in range(n):
            if k != i:
                factor = aug[k][i]
                aug[k] = [aug[k][j] - factor * aug[i][j] for j in range(2 * n)]

    return [row[n:] for row in aug]


def divide(A, B):
    B_inv = inverse(B)
    return multiply(A, B_inv)


def check_matrix_dimensions(A, B, operation):
    for m, name in [(A, 'A'), (B, 'B')]:
        if not all(len(row) == len(m[0]) for row in m):
            raise ValueError(f"Помилка: матриця {name} має рядки різної довжини")

    rows_A = len(A)
    cols_A = len(A[0]) if A else 0
    rows_B = len(B)
    cols_B = len(B[0]) if B else 0

    if operation in ['+', '-']:
        if rows_A != rows_B or cols_A != cols_B:
            raise ValueError("Помилка: різні розміри")

    elif operation == '*':
        if cols_A != rows_B:
            raise ValueError("Помилка: різні розміри")

    elif operation == '/':
        if rows_B != cols_B or cols_A != rows_B:
            raise ValueError("Помилка: різні розміри")


try:
    operation, first_matrix, second_matrix = read_data('data2.txt')

    check_matrix_dimensions(first_matrix, second_matrix, operation)

    if operation == '+':
        result = add(first_matrix, second_matrix)
    elif operation == '-':
        result = subtract(first_matrix, second_matrix)
    elif operation == '*':
        result = multiply(first_matrix, second_matrix)
    elif operation == '/':
        result = divide(first_matrix, second_matrix)

    save_matrix(result, 'result2.txt')
    print("Записано у result2.txt")

except ValueError as e:
    print(e)
    exit(1)
except Exception as e:
    print(f"Помилка: {e}")
    exit(1)
