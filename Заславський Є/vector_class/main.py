from vector_class import Vector

def read_vectors(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [Vector([float(x) for x in line.split()]) for line in lines]

def write_result(filename, text):
    with open(filename, "a") as f:
        f.write(text + "\n")


def main():
    vectors = read_vectors("data.txt")

    v1 = vectors[0]
    v2 = vectors[1]

    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    choice = int(input("Оберіть дію: "))

    if choice == 1:
        result = v1 + v2
        operation = "+"
    elif choice == 2:
        result = v1 - v2
        operation = "-"
    elif choice == 3:
        result = v1 * v2
        operation = "*"
    elif choice == 4:
        result = v1 / v2
        operation = "/"
    else:
        print("Неправильний вибір!")
        return

    text = f"{v1} {operation} {v2} = {result}"
    print(text)
    write_result("result.txt", text)


if __name__ == "__main__":
    main()
