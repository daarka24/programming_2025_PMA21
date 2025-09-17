def read_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        if line.strip():
            numbers = [float(x) for x in line.split()]
            matrix.append(numbers)
    return matrix


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


def inverse(matrix):
    n = len(matrix)
    aug = []
    for i in range(n):
        row = matrix[i][:] + [0] * n
        row[n + i] = 1
        aug.append(row)


    for i in range(n):
        pivot = aug[i][i]
        for j in range(2 * n):
            aug[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(2 * n):
                    aug[k][j] -= factor * aug[i][j]

    inv = []
    for i in range(n):
        inv.append(aug[i][n:])
    return inv


def divide(A, B):
    B_inv = inverse(B)
    return multiply(A, B_inv)


def main():
    print("1 - Додавання")
    print("2 - Віднімання")
    print("3 - Множення")
    print("4 - Ділення")

    choice = input("Оберіть операцію 1-4: ")


    with open('data2.txt', 'r') as f:
        lines = f.readlines()


    first_matrix = []
    second_matrix = []
    current_matrix = 1

    for line in lines:
        line = line.strip()
        if not line:
            current_matrix = 2
        elif line:
            numbers = [float(x) for x in line.split()]
            if current_matrix == 1:
                first_matrix.append(numbers)
            else:
                second_matrix.append(numbers)

    print("\nПерша матриця:")
    print_matrix(first_matrix)
    print("\nДруга матриця:")
    print_matrix(second_matrix)

    if choice == '1':
        result = add(first_matrix, second_matrix)
        print("\nРезультат додавання:")
    elif choice == '2':
        result = subtract(first_matrix, second_matrix)
        print("\nРезультат віднімання:")
    elif choice == '3':
        result = multiply(first_matrix, second_matrix)
        print("\nРезультат множення:")
    elif choice == '4':
        result = divide(first_matrix, second_matrix)
        print("\nРезультат ділення:")

    print_matrix(result)
    save_matrix(result, '../result2.txt')
    print("\nРезультат збережено у файл result2.txt")


if __name__ == "__main__":
    main()