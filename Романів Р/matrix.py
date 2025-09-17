from matrix_class import Matrix

#допоміжні функції
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def check_operation(rows):
    undefined_operation = True
    for i in range(len(rows)):
        if rows[i] in "+-*/":
            undefined_operation = False

    if undefined_operation:
        raise ValueError("Undefined operation")


def from_str_to_list(row):
    return [float(el) for el in row.strip().split() if is_number(el)]


if __name__ == "__main__":
    with open("input_matrix.txt", "r") as file:
        readed = file.readlines()

    rows = [row.removesuffix("\n").strip() for row in readed]

    check_operation(rows)

    first, second, separated, operator = [], [], False, None
    for i in range(len(rows)):
        if rows[i] not in "+-*/":
            if not separated:
                first.append(rows[i])
            else:
                second.append(rows[i])
        else:
            operator = rows[i]
            separated = True

    first = Matrix([from_str_to_list(row) for row in first])
    second = Matrix([from_str_to_list(row) for row in second])

    result = []
    if operator == "+":
        result = first.sum(second)

    elif operator == "-":
        result = first.sub(second)

    elif operator == "*":
        result = first.mul(second)

    elif operator == "/":
        result = first.div(second)

    with open("output_matrix.txt", "w") as file:
        for row in result:
            file.write(str(row) + "\n")

    print("Результат записано: " + str(result))
