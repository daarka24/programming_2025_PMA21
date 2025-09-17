
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
div = [v1[i] / v2[i] if v2[i] != 0 else float('inf') for i in range(len(v1))]

def format_vector(v):
    return "(" + ", ".join(str(int(x)) if x == int(x) else str(x) for x in v) + ")"

add_str = format_vector(add)
sub_str = format_vector(sub)
mul_str = format_vector(mul)
div_str = format_vector(div)

with open("output.txt", "w") as out:
    out.write("Додавання: " + add_str + "\n")
    out.write("Віднімання: " + sub_str + "\n")
    out.write("Множення: " + mul_str + "\n")
    out.write("Ділення: " + div_str + "\n")

print("Результати записано у 'result.txt'")
