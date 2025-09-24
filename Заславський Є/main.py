from matrix_class import Matrix

def read_matrices(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    first = []
    second = []
    current = 1

    for line in lines:
        line = line.strip()
        if not line:
            current = 2
            continue
        numbers = [float(x) for x in line.split()]
        if current == 1:
            first.append(numbers)
        else:
            second.append(numbers)

    return Matrix(first), Matrix(second)

def save_matrix(matrix, filename):
    with open(filename, 'a') as f:
        f.write(str(matrix) + "\n")

def main():
    print("1 - Додавання")
    print("2 - Віднімання")
    print("3 - Множення")
    print("4 - Ділення")
    choice = input("Оберіть операцію 1-4: ")

    A, B = read_matrices("data2.txt")

    print("\nПерша матриця:")
    print(A)
    print("\nДруга матриця:")
    print(B)

    if choice == '1':
        result = A + B
        op = "+"
    elif choice == '2':
        result = A - B
        op = "-"
    elif choice == '3':
        result = A * B
        op = "*"
    elif choice == '4':
        result = A / B
        op = "/"
    else:
        print("Невірний вибір")
        return

    print("\nРезультат:")
    print(result)

    save_matrix(result, "result2.txt")
    print("\nРезультат збережено у файл result2.txt")

if __name__ == "__main__":
    main()
