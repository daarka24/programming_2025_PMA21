from vector_class import Vector

def read_data(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    operation = lines[0].strip()
    v1 = Vector([float(x) for x in lines[1].split()])
    v2 = Vector([float(x) for x in lines[2].split()])

    return operation, v1, v2

def write_result(filename, text):
    with open(filename, "w") as f:
        f.write(text)

operation, v1, v2 = read_data("data.txt")

try:
    if operation == "+":
        result = v1 + v2
    elif operation == "-":
        result = v1 - v2
    elif operation == "*":
        result = v1 * v2
    elif operation == "/":
        result = v1 / v2
    else:
        raise ValueError("Невідома операція")

    text = f"{v1} {operation} {v2} = {result}"

except ValueError as e:
    text = f"Помилка: {e}"

print(text)
write_result("result.txt", text)
