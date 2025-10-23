def read_vectors(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    operation = lines[0].strip()
    v1 = [float(x) for x in lines[1].split()]
    v2 = [float(x) for x in lines[2].split()]

    return operation, v1, v2


def add_vectors(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def sub_vectors(a, b):
    return [a[i] - b[i] for i in range(len(a))]


def mul_vectors(a, b):
    return [a[i] * b[i] for i in range(len(a))]


def div_vectors(a, b):
    return [a[i] / b[i] if b[i] != 0 else "error" for i in range(len(a))]


def write_result(filename, text):
    with open(filename, "w") as f:
        f.write(text)


operation, v1, v2 = read_vectors("data.txt")

if len(v1) != len(v2):
    text = "Помилка: вектори різного розміру."
else:
    result = None
    if operation == "+":
        result = add_vectors(v1, v2)
    elif operation == "-":
        result = sub_vectors(v1, v2)
    elif operation == "*":
        result = mul_vectors(v1, v2)
    elif operation == "/":
        result = div_vectors(v1, v2)

    text = f"{v1} {operation} {v2} = {result}"

print(text)
write_result("result.txt", text)
