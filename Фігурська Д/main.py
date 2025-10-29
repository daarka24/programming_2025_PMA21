with open("starters.txt", "r") as file:
    lines = file.readlines()

v1 = [float(x) for x in lines[0].strip().split(",")]
v2 = [float(x) for x in lines[1].strip().split(",")]

if len(v1) != len(v2):
    print("need to be equal length")
    exit()

add = []
sub = []
mul = []
div = []

for i in range(len(v1)):
    try:

        add.append(v1[i] + v2[i])
        sub.append(v1[i] - v2[i])
        mul.append(v1[i] * v2[i])
        if v2[i] == 0:
            div = "can't do, zero"
            break
        else:
            div.append(v1[i] / v2[i])
    except Exception:
        print("Error")


results = [
    f"sum is: {add}",
    f"dif is: {sub}",
    f"multiply: {mul}",
    f" dividing: {div}",
]

with open("results.txt", "w") as f:
    for line in results:
        f.write(line + "\n")
