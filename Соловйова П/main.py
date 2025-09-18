with open("input.txt", "r") as file:
    lines = file.readlines()
if len(lines) < 2:
    print("У файлі має бути щонайменше два рядки")
    exit()
v1 = [float(x) for x in lines[0].strip().split()]
v2 = [float(x) for x in lines[1].strip().split()]
if len(v1) != len(v2):
    print("Вектори повинні бути однакової довжини")
    exit()
add = [v1[i] + v2[i] for i in range(len(v1))]
sub = [v1[i] - v2[i] for i in range(len(v1))]
mul = [v1[i] * v2[i] for i in range(len(v1))]
div = []
division_valid = False
for i in range(len(v1)):
    if v2[i] != 0:
        div.append(v1[i] / v2[i])
        division_valid = True
    else:
        div.append(None)
def format_vector(v):
    formatted = []
    for x in v:
        if x is None:
            continue
        if x == int(x):
            formatted.append(str(int(x)))
        else:
            formatted.append(str(x))
    return "(" + ", ".join(formatted) + ")"
with open("output.txt", "w") as out:
    out.write("Додавання: " + format_vector(add) + "\n")
    out.write("Віднімання: " + format_vector(sub) + "\n")
    out.write("Множення: " + format_vector(mul) + "\n")

    if division_valid:
        out.write("Ділення: " + format_vector(div) + "\n")
