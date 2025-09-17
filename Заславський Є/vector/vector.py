def read_vectors(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    vectors = []
    for line in lines:
        nums = [float(x) for x in line.split()]
        vectors.append(nums)
    return vectors


def add_vectors(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def sub_vectors(a, b):
    return [a[i] - b[i] for i in range(len(a))]


def mul_vectors(a, b):
    return [a[i] * b[i] for i in range(len(a))]


def div_vectors(a, b):
    return [a[i] / b[i] if b[i] != 0 else "∞" for i in range(len(a))]


def write_result(filename, text):
    with open(filename, "w") as f:
        f.write(text)



vectors = read_vectors("data.txt")

v1 = vectors[0]
v2 = vectors[1]

print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

choice = int(input("Оберіть дію: "))

result = None
operation = ""

if choice == 1:
    result = add_vectors(v1, v2)
    operation = "+"
elif choice == 2:
    result = sub_vectors(v1, v2)
    operation = "-"
elif choice == 3:
    result = mul_vectors(v1, v2)
    operation = "*"
elif choice == 4:
    result = div_vectors(v1, v2)
    operation = "/"

text = f"{v1} {operation} {v2} = {result}"
print(text)

write_result("../result.txt", text)
