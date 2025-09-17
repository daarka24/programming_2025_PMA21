


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def from_str_to_tuple(vector):
    return tuple([float(n) for n in vector.split() if is_number(n)])


def sum(x, y):
    if len(x) != len(y):
        print("The length of the two vectors must be equal")
        return

    return tuple([x[i] + y[i] for i in range(len(x))])


def sub(x, y):
    if len(x) != len(y):
        print("The length of the two vectors must be equal")
        return

    return tuple([x[i] - y[i] for i in range(len(x))])


def mul_scalar(x, y):
    if len(x) != len(y):
        print("The length of the two vectors must be equal")
        return

    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]
    return result

def mul_by_scalar(x, n):
    return tuple([el * n for el in x])

def div_by_scalar(x, n):
    return tuple([el / n for el in x])

def mul_vectors(x, y):
    if len(x) != len(y) != 3:
        print("The length of the two vectors must be equal")
        return

    return x[1] * y[2] - x[2] * y[1], -(x[0] * y[2] - x[2] * y[0]), x[0] * y[1] - x[1] * y[0]


if __name__ == "__main__":
    with open("input_vectors.txt", "r") as file:
        vectors = file.read().split("\n")

    vectors = [from_str_to_tuple(vector) for vector in vectors]

    print("""\t=== Menu ===
    1. Додати 
    2. Відняти
    3. Помножити на скаляр
    4. Поділити на скаляр
    5. Скалярний добуток
    6. Векторний добуток (для векторів з трьома координатами)""")

    while True:
        try:
            choice = int(input("Make a choice: "))
            if choice <= 0 or choice >= 7:
                print("Choice out of range, try again")
                continue
            break
        except ValueError:
            print("Choice must be an integer, try again")

    result = None
    if choice == 1:
        result = sum(vectors[0], vectors[1])

    elif choice == 2:
        result = sub(vectors[0], vectors[1])

    elif choice == 3:
        scalar = int(input("Виберіть число щоб помножити: "))
        result = mul_by_scalar(vectors[0], scalar)

    elif choice == 4:
        scalar = int(input("Виберіть число щоб поділити: "))
        result = div_by_scalar(vectors[0], scalar)

    elif choice == 5:
        result = mul_scalar(vectors[0], vectors[1])

    elif choice == 6:
        result = mul_vectors(vectors[0], vectors[1])


    with open("output_vectors.txt", "w") as file:
        file.write(f"{result}")






