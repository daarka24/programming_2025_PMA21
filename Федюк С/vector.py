with open("input.txt", "r") as file:
    a = tuple(map(int, file.readline().strip("()\n ").split(",")))
    b = tuple(map(int, file.readline().strip("()\n ").split(",")))

    with open("scalar.txt", "r") as f:
        c = int(f.readline().strip())

plus = []
for i in range(len(a)):
    plus.append(a[i] + b[i])

minus = []
for i in range(len(a)):
    minus.append(a[i] - b[i])

multiply = []
for i in range(len(a)):
    multiply.append(a[i] * b[i])

divide = []
for i in range(len(a)):
    try:
        divide.append(a[i] / c)
    except ZeroDivisionError:
        divide.append(None)

result = f"Plus: {plus}\nMinus: {minus}\nMultiply: {multiply}\nDivide: {divide}"

with open("output.txt", "w") as file:
    file.write(result)
