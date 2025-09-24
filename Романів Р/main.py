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
        data = file.read().split("\n")

    operation = ""
    flag = False

    for row in data:
        if row.strip() in ["+","-","*","/","**","***"]:
            operation = row.strip()
            flag = True
            break
    if not flag:
        print("невідома операція")

    vectors = [Vector(from_str_to_tuple(vector)) for vector in data[::2]]

    try:
        scalar = int(data[3])

    except (ValueError, IndexError):

        print("Неправильний запис інформації")
        flag = False


    if flag:
        result = None
        if operation == "+":
            result = vectors[0].sum(vectors[1])

        elif operation == "-":
            result = vectors[0].sub(vectors[1])

        elif operation == "*":
            result = vectors[0].mul_by_scalar(scalar)

        elif operation == "/":
            result = vectors[0].div_by_scalar(scalar)

        elif operation == "**":
            result = vectors[0].mul_scalar(vectors[1])

        elif operation == "***":
            result = vectors[0].mul_vectors(vectors[1])

        with open("output_vectors.txt", "w") as file:
            file.write(f"{result}")
        print("Результат записано:", result)