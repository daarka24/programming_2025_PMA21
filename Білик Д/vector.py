def fun(vec):
    vectors = []
    with open(vec, "r") as f:
        for line in f:
            nums = list(map(float, line.strip().split()))
            vectors.append(nums)
    return vectors
def add(v1, v2):
    return [a + b for a, b in zip(v1, v2)]
def sub(v1, v2):
    return [a - b for a, b in zip(v1, v2)]
def mul(v1, v2):
    return [a * b for a, b in zip(v1, v2)]
def dil(v1, v2):
    return [a / b if b != 0 else float("inf") for a, b in zip(v1, v2)]
def vector_to_str(v):
    return "(" + ",".join(str(int(x)) if x.is_integer() else str(x) for x in v) + ")"
def save(vec, v1, v2):
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": dil
    }
    with open(vec, "w") as f:
        for symbol, func in operations.items():
            result = func(v1, v2)
            f.write(f"{vector_to_str(v1)} {symbol} {vector_to_str(v2)} = {vector_to_str(result)}\n")

vectors = fun("number.txt")

if len(vectors) < 2:
    print("У файлі повинно бути як мінімум 2 вектори!")
else:
    v1, v2 = vectors[0], vectors[1]
    save("result.txt", v1, v2)

