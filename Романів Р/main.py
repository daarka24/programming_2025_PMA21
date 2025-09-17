from vector_class import Vector

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def from_str_to_tuple(vector):
    return tuple([float(n) for n in vector.split() if is_number(n)])


if __name__ == "__main__":
    with open("input_vectors.txt", "r") as file:
        vectors = file.read().split("\n")

    vectors = [Vector(from_str_to_tuple(vector)) for vector in vectors]

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
        result = vectors[0].sum(vectors[1])

    elif choice == 2:
        result = vectors[0].sub(vectors[1])

    elif choice == 3:
        scalar = int(input("Виберіть число щоб помножити: "))
        result = vectors[0].mul_by_scalar(scalar)

    elif choice == 4:
        scalar = int(input("Виберіть число щоб поділити: "))
        result = vectors[0].div_by_scalar(scalar)

    elif choice == 5:
        result = vectors[0].mul_scalar(vectors[1])

    elif choice == 6:
        result = vectors[0].mul_vectors(vectors[1])

    with open("output_vectors.txt", "w") as file:
        file.write(f"{result}")
    print("Результат записано:", result)
